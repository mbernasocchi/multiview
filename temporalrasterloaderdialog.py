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
from datetime import datetime
import re

from ui_temporalrasterloaderdialog import Ui_TemporalRasterLoaderDialog
# create the dialog for zoom to point
class TemporalRasterLoaderDialog(QDialog):
    def __init__(self, iface):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TemporalRasterLoaderDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("MultiView - Temporal Raster Loader")
        
        self.iface = iface
        self.mainWindow = self.iface.mainWindow()
        self.mapCanvas = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()
    
    def loadTemporalRasters(self):
        filesCount = len(self.files)
        if filesCount > 0:
            
            #TODO hack to generate the correct groups
            tmpGroup = self.legend.addGroup("dummy group", False)
            tmpLayer = QgsRasterLayer(self.files[0], "Dummy layer")
            tmpLayer = QgsMapLayerRegistry.instance().addMapLayer(tmpLayer)
            self.legend.moveLayer(tmpLayer, tmpGroup)
            #END Hack
            
            i = 0.0
            startTime = datetime.now()
            self.printToResult("NEW IMPORT RUN\nStart: " + str(startTime))
            
            #re for the temporal format
            temporalSearchPattern = re.compile(str(self.ui.temporalRegEx.text()))
            #re for the temporal format
            intervalSearchPattern = re.compile(str(self.ui.intervalRegEx.text()))
            #re to remove all non digit
            onlyDigits = re.compile(r'[^\d]+')
            
            for filePath in self.files:
                i += 1
                self.ui.progressBar.setValue(i / filesCount * 100)
                fileBaseName = QFileInfo(filePath).baseName()
                
                #look for search pattern in filename
                fileNameInfo = temporalSearchPattern.search(fileBaseName)
                temporalInfo = fileNameInfo.group()
                fileNameInfo = intervalSearchPattern.search(fileBaseName)
                intervalInfo = fileNameInfo.group()
                variableInfo = str(fileBaseName).replace(temporalInfo, '').replace(intervalInfo, '')
                
                groupName = variableInfo + intervalInfo
                layerName = onlyDigits.sub('', str(temporalInfo))

                #check if new group is needed
                if groupName not in self.legend.groups():
                    self.legend.addGroup(groupName, False)
                    self.printToResult("New group: " + groupName)
                    
                #createLayer
                layer = QgsRasterLayer(filePath, layerName)
                layer.setCustomProperty("isTemporalRaster", True)
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
                        self.printToResult("Moving : " + fileBaseName + " to " + groupName + "(i " + str(groupIndex) + ")/" + layerName + " -> " + layerWasAdded)
                    else:
                        self.printToResult("NOT Moving : " + fileBaseName + " to " + groupName + "(i " + str(groupIndex) + ")/" + layerName + " -> " + layerWasAdded)
                else:
                    self.printToResult("Layer invalid : " + layerName + " of " + groupName + " -> ERROR")
             
            #TODO hack to generate the correct groups
            QgsMapLayerRegistry.instance().removeMapLayer(tmpLayer.id())
            self.legend.removeGroup(tmpGroup)   
            #END Hack
            
            endTime = datetime.now()
            self.printToResult("End: " + str(endTime))
            self.printToResult("Duration: " + str(endTime - startTime))
        
    def printToResult(self, text):
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
    def on_closeButton_clicked(self):
        self.close()      
