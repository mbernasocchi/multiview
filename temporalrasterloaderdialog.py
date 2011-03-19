"""
/***************************************************************************
 TemporalRasterLoaderDialog
                                 A QGIS plugin
                             -------------------
        begin                : 2011-01-02
        copyright            : (C) 2011 by marco
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
import re

from stepdurationdialog import StepDurationDialog

from ui_temporalrasterloaderdialog import Ui_TemporalRasterLoaderDialog

# create the dialog for zoom to point
class TemporalRasterLoaderDialog(QDialog):
    def __init__(self, iface, main):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TemporalRasterLoaderDialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle("MultiView - Temporal Raster Loader")
        
        self.iface = iface
        self.mainWindow = self.iface.mainWindow()
        self.mapCanvas = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()
        self.main = main
        self.timeFormat = self.main.timeFormat
        
        self.ui.startDatetime.setDisplayFormat(self.timeFormat)
    
    def loadTemporalRasters(self):
        filesCount = len(self.files)
        if filesCount > 0:
            self.main.isLoadingTemporalData = True
            
#            #TODO hack to generate the correct groups
#            tmpGroup = self.legend.addGroup("dummy group", False)
#            tmpLayer = QgsRasterLayer(self.files[0], "Dummy layer")
#            tmpLayer = QgsMapLayerRegistry.instance().addMapLayer(tmpLayer)
#            self.legend.moveLayer(tmpLayer, tmpGroup)
#            #END Hack
            
            i = 0.0
            importStartTime = QDateTime.currentDateTime()
            self.printToResult("NEW IMPORT RUN\nStart: " + importStartTime.toString(self.timeFormat))
            
            #re for the temporal format
            temporalSearchPattern = re.compile(str(self.ui.temporalRegEx.text()))
            #re for the temporal format
            intervalSearchPattern = re.compile(str(self.ui.intervalRegEx.text()))
            #re to remove all non digit
            onlyDigits = re.compile(r'[^\d]+')
            
            layersStartDatetime = self.ui.startDatetime.dateTime()
            
            for filePath in self.files:
                i += 1
                self.ui.progressBar.setValue(i / filesCount * 100)
                fileBaseName = QFileInfo(filePath).baseName()
                
                #look for search pattern in filename
                stepNumberText = temporalSearchPattern.search(fileBaseName)
                stepNumberText = stepNumberText.group()
                stepNumber   = int(onlyDigits.sub('', str(stepNumberText)))
                stepDurationText = intervalSearchPattern.search(fileBaseName)
                stepDurationText = stepDurationText.group()
                if stepDurationText in self.main.stepDurations.keys():
                    stepDuration = self.main.stepDurations[stepDurationText]
                else:
                    dlg = StepDurationDialog(stepDurationText)
                    # show the dialog
                    dlg.show()
                    # See if OK was pressed
                    if dlg.exec_():
                      stepDuration = int(dlg.ui.input.text())
                      stepDuration = stepDuration
                      self.main.stepDurations[stepDurationText] = stepDuration
                    else:
                        self.printToResult("ABORTED by user when entering " + stepDurationText + " duration")
                        break
                        
                variableInfo = str(fileBaseName).replace(stepNumberText, '').replace(stepDurationText, '')
                
                groupName = variableInfo + stepDurationText
                layerName = str(stepNumber)
                layerTime = layersStartDatetime.addSecs( (stepDuration *  (stepNumber - 1)) )
                
                #check if new group is needed
                if groupName not in self.legend.groups():
                    self.legend.addGroup(groupName, False, True )
                    self.printToResult("New group: " + groupName)
                    
                #createLayer
                layer = QgsRasterLayer(filePath, fileBaseName)
                #set time properties
                layer.setCustomProperty("isTemporalRaster", True)
                layer.setCustomProperty("temporalRasterIteration", layerName)
                layer.setCustomProperty("temporalRasterTime", layerTime.toString(self.timeFormat))
                
                #set symbology to pseudocolors
                layer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
                layer.setColorShadingAlgorithm(QgsRasterLayer.PseudoColorShader)
                
                #add layer to project
                if layer.isValid():
                    layer = QgsMapLayerRegistry.instance().addMapLayer(layer)
                    layerWasAdded = "OK" if bool(layer) else "ERROR"
                    self.printToResult("Adding : " + fileBaseName + " -> " + layerWasAdded)
                    
                    #get the current group index
                    groups = []
                    for group in self.legend.groupLayerRelationship():
                        groups.append(group[0])
                    
                    #the group IS present since we created it before
                    groupIndex = groups.index(groupName)
                    
                    #self.printToResult( groupName + " in: " + str(self.legend.groupLayerRelationship()) + " has index:" + str(groupIndex))
                    
                    if self.legend.groupExists(groupIndex):
                        self.legend.moveLayer(layer, groupIndex)
                        #self.printToResult("Moving : " + fileBaseName + " to " + groupName + "(i " + str(groupIndex) + ")/" + layerName + " -> " + layerWasAdded)
                    else:
                        self.printToResult("Moving : " + fileBaseName + " to " + groupName + "(i " + str(groupIndex) + ")/" + layerName + " -> " + layerWasAdded)
                else:
                    self.printToResult("Layer invalid : " + layerName + " of " + groupName + " -> ERROR")
             
#            #TODO hack to generate the correct groups
#            #BUG https://trac.osgeo.org/qgis/ticket/3263
#            QgsMapLayerRegistry.instance().removeMapLayer(tmpLayer.id())
#            self.legend.removeGroup(tmpGroup)   
#            #END Hack
            
            importEndTime = QDateTime.currentDateTime()
            self.printToResult("End: " + importEndTime.toString(self.timeFormat))
            self.printToResult("Duration: " + str(importStartTime.secsTo(importEndTime)) + " sec")
            self.main.isLoadingTemporalData = False
            self.main.writeStepDurations()
            try:
                self.main.multiviewwidget.refreshAll()
            except:
                pass
        
    def printToResult(self, text):
        if self.ui.results.toPlainText().isEmpty():
            self.ui.results.setText(text)
        else:
            self.ui.results.setText(self.ui.results.toPlainText() + "\n" + text)
        
        self.ui.results.verticalScrollBar().setValue(self.ui.results.verticalScrollBar().maximum());
    
    @pyqtSlot()
    def on_loadDataButton_clicked(self):
        self.files = QFileDialog.getOpenFileNames(
                         self,
                         "Select temporal rasters to load",
                         #QDir.homePath (),
                         "/home/marco/master/data/wallisWGS/testData",
                         "GDAL files (*.dem *.tif *.tiff *.jpg *.jpeg *.asc);;All files (*.*)")
        self.loadTemporalRasters()
    
    @pyqtSlot()
    def on_saveLogButton_clicked(self):
        file = QFileDialog.getSaveFileName(self, "Save As...")
        if not file.isEmpty():
            file = open(file, 'w')
            file.write(self.ui.results.toPlainText())
            file.close()
    
    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.close()      
