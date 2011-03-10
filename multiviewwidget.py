"""
/***************************************************************************
 MultiViewWidget
                                 A QGIS plugin          
 This plugin shows multitemporal data on an multi
                             -------------------
        begin                : 2010-12-19
        copyright            : (C) 2011 by bernawebdesign.ch
        email                : marco@bernawebdesign.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from panemitmaptool import PanEmitMapTool

from ui_multiview import Ui_MultiView
from temporalrasterloaderdialog import TemporalRasterLoaderDialog

#import visualizations
from visualizations.rawvaluewidget import RawValueWidget
from visualizations.timeplotwidget import TimePlotWidget
from visualizations.helixwidget import HelixWidget

# create the widget
class MultiViewWidget(QDialog):
    def __init__(self, iface, parent):
        QWidget.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MultiView()
        self.ui.setupUi(self)
        self.setWindowTitle("MultiView")
        
        self.iface = iface
        self.mainWindow = self.iface.mainWindow()
        self.mapCanvas = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()
        self.mapTool = self.mapCanvas.mapTool()
        self.proj = QgsProject.instance()
        self.parent = parent 
        
        #create visualizations
        self.visualizations = [TimePlotWidget(self), HelixWidget(self), RawValueWidget(self)]
        for v in self.visualizations:
            self.ui.visualizations.addTab(v, v.name())
        self.selectedVisualization = self.visualizations[0] 
        QObject.connect(self.ui.visualizations, SIGNAL("currentChanged ( int )"), self.updateSelectedVisualization)
        
        #init the coordinate
        self.coords = None
        
        #get the globe plug-in instance
        self.globe = self.mainWindow.findChild(QObject, "globePlugin")
        
        #create the maptool
        self.previousMapTool = self.mapCanvas.mapTool();
        self.previousCursor = self.mapCanvas.cursor();
        self.mapTool = PanEmitMapTool(self.mapCanvas)
        self.mapCanvas.setMapTool(self.mapTool)
        self.mapCanvas.setCursor(self.mapTool.cursor)
        self.ui.trackRightClick.setChecked (True)
        
        #create the available variables checkbox group
        self.ui.availableVariablesGroup = QButtonGroup()
        self.ui.availableVariablesGroup.setExclusive(False)
#        self.readProjectActivatedVariables()
        self.activatedVariables = []
        self.updateAvailableVariables()
        
        #clear plugin projects settings when a new project is loaded
#        QObject.connect(self.iface, SIGNAL("projectRead()"), self.removeProjectSettings)
#        QObject.connect(self.iface, SIGNAL("newProjectCreated()"), self.removeProjectSettings)
#        self.removeProjectSettings()
        
        #update the variable list if layers or groups are changed or a new project is loaded
        QObject.connect(self.mapCanvas, SIGNAL("layersChanged()"), self.refreshAll)
        QObject.connect(self.legend, SIGNAL("groupIndexChanged( int, int )"), self.refreshAll)
        QObject.connect(self.iface, SIGNAL("projectRead()"), self.refreshAll)
        QObject.connect(self.iface, SIGNAL("newProjectCreated()"), self.refreshAll)
        
        #a layer has been clicked
        QObject.connect(self.ui.availableVariablesGroup, SIGNAL("buttonClicked( QAbstractButton * )"), self.updateMultiVariables)
        
        self.redraw()
    
    #runs just before the widget is closed
    def closeEvent(self, event):
#        self.saveProjectActivatedVariables()
        self.mapCanvas.setMapTool(self.previousMapTool)
        self.mapCanvas.setCursor(self.previousCursor)    
             
    def test(self, title, text):
        QMessageBox.information(self.mainWindow, str(title), str(text))
        print "TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST"
        print str(text)
        
    def updateMultiVariables(self, button):
        #TODO this assumes unique layerGroup names
        varName = button.text()
        #variable has been turned ON
        
        if button.isChecked():
            try:
                self.activatedVariables.index(varName)
            except:
                self.activatedVariables.append(varName)
        else:
            try:
                self.activatedVariables.remove(varName)
            except:
                QMessageBox.warning(self.mainWindow, "Turn OFF exception",
                    "It seems that you have layers that have not unique names [layername: " + varName + "]")
        self.redraw()
    
    def redraw(self):
        if len(self.activatedVariables) is 0:
            self.ui.warningDisplay.setText("<font color='red'>please select at least a variable</font>")
            self.selectedVisualization.reset()
        elif self.coords is None:
            self.ui.warningDisplay.setText("<font color='red'>Please click on the map canvas to select coordinates</font>")
            self.selectedVisualization.reset()
        else:
            self.ui.warningDisplay.setText("")
            self.selectedVisualization.redraw(self.drill())
        
    def drill(self):
        values = {}
        groups = self.legend.groupLayerRelationship()
        self.maxValue = 0
        for group in groups:
            groupName = str(group[0])
            groupLayers = group[1]
            groupValues = {}
            #Group is selected in widget
            if groupName in self.activatedVariables:
                for layerName in groupLayers:
                    #print "\t"+layerName
                    layer = QgsMapLayerRegistry.instance().mapLayer(layerName)
                    #Only GrayOrUndefined rasters (no multiband or palette rasters)
                    if layer and layer.type() == QgsMapLayer.RasterLayer \
                        and layer.rasterType() == QgsRasterLayer.GrayOrUndefined:
                        
                        #getting layer maximal value if needed update absolute max value
                        layerMaxValue =  layer.bandStatistics(1).maximumValue
                        if layerMaxValue > self.maxValue:
                            self.maxValue = layerMaxValue
                            
                        extent = layer.extent()
                        if self.pointInExtent(self.coords, extent):
                            ident = layer.identify(self.coords)
                            time = int(layer.name())
                            value = float(ident[1].values()[0])
                            groupValues[time] = value
                values[groupName] = groupValues
             
        return values

#    def readProjectActivatedVariables(self):
#        #init the activated variables list
#        try:
#            self.activatedVariables = self.parent.activatedVariables
#        except:
#            self.activatedVariables = []
#            try:
#               for v in self.proj.readListEntry("MultiView", "activatedVariables")[0]:
#                   if v in self.legend.groups():
#                       self.activatedVariables.append(v)
#            except:
#                pass
#        #self.test("readEnd",self.activatedVariables)
#        
#    def saveProjectActivatedVariables(self):
#        # store values
#        self.proj.writeEntry("MultiView", "activatedVariables ", self.activatedVariables)
#     
#    def removeProjectSettings(self):
#        try:
#            del self.activatedVariables
#        except:
#            pass
    
    def refreshAll(self):
        self.updateAvailableVariables()
        self.selectedVisualization.reset()
        
    def updateAvailableVariables(self):
        #clear the colors dictionary
        self.colors = {}

        #remove the old checkboxes
        try:
            for b in self.ui.availableVariablesGroup.buttons():
                self.ui.availableVariablesGroup.removeButton(b)
                self.ui.availableVariables.removeWidget(b)
                b.hide()
        except:
            pass

        #add the updated checkboxes
        i = 0
        #TODO better solution
        maxColors = 10
        for layerGroupName in self.legend.groups():
            layerGroupName = layerGroupName
            if self.hasTemporalRasters(layerGroupName):
                #create a legend color
                self.colors[layerGroupName] = QColor.fromHsv( int(360 / maxColors * i), 255, 255 )
                #create the checkbox
                cb = QCheckBox(layerGroupName)
                self.ui.availableVariablesGroup.addButton(cb)
                isOn = layerGroupName in self.activatedVariables 
                cb.setChecked(bool(isOn))
                #color the checkbox
                cb.setStyleSheet("background-color: rgb(" + str(self.colors[layerGroupName].red()) + ", " 
                                + str(self.colors[layerGroupName].green()) + ", " + str(self.colors[layerGroupName].blue()) + ");\n")
                self.ui.availableVariables.addWidget(cb)
                i += 1
                
    def updateSelectedVisualization(self, index):
        self.selectedVisualization = self.visualizations[index]
    
    def resetCoords(self):
          self.selectedVisualization.reset()
    
    def updateCoords(self, coords):
        self.coords = coords
        self.redraw()
    
    def updateCoordsMouse(self, point, mouseButton):
        if mouseButton == Qt.RightButton:
            self.updateCoords(point)
  
    def hasTemporalRasters(self, layersGroupName):
        #checks if a layer group contains rasters that have the customProperty("isTemporalRaster") set to True
        groups = self.legend.groupLayerRelationship()
        for group in groups:
            groupName = str(group[0])
            groupLayers = group[1]
            if layersGroupName == groupName:
                for layerId in groupLayers:
                    layer = QgsMapLayerRegistry.instance().mapLayer(layerId)
                    if layer and layer.customProperty("isTemporalRaster", False).toBool():
                        return True
        return False
  
    def pointInExtent(self, point, extent):
        return \
        point.x() > extent.xMinimum() and \
        point.x() < extent.xMaximum() and \
        point.y() > extent.yMinimum() and \
        point.y() < extent.yMaximum()
    
    @pyqtSlot(bool)
    def on_trackMouseMove_toggled(self, active):
        self.resetCoords()
        if active:
            QObject.connect(self.mapCanvas, SIGNAL("xyCoordinates( QgsPoint )"), self.updateCoords)
        else:
            QObject.disconnect(self.mapCanvas, SIGNAL("xyCoordinates( QgsPoint )"), self.updateCoords)
    
    @pyqtSlot(bool)
    def on_trackRightClick_toggled(self, active):
        self.resetCoords()
        if active:
            #connecting to a python emitted signal is different
            QObject.connect(self.mapTool, SIGNAL("canvasClicked"), self.updateCoordsMouse)
            try:
                QObject.connect(self.globe, SIGNAL("newCoordinatesSelected( QgsPoint )"), self.updateCoords)
            except:
                pass
        else:
            QObject.disconnect(self.mapTool, SIGNAL("canvasClicked"), self.updateCoordsMouse)
            try:
                QObject.disconnect(self.globe, SIGNAL("newCoordinatesSelected( QgsPoint )"), self.updateCoords)
            except:
                pass
    
    @pyqtSlot()
    def on_availableVariablesUpdateButton_clicked(self):
        self.updateAvailableVariables()
    
    @pyqtSlot()
    def on_loadDataButton_clicked(self):
        self.temporalRasterLoader = TemporalRasterLoaderDialog(self.iface)
        # show the dialog
        self.temporalRasterLoader.show()
        result = self.temporalRasterLoader.exec_()
#        # See if OK was pressed
        if result == 1:
#            # do something useful (delete the line containing pass and
#            # substitute with your code
            pass
                
    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.close()            
