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
from PyQt4.QtXml import QXmlSimpleReader, QXmlInputSource
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
            self.ui.saveLogButton.setEnabled(False)
            self.ui.dataVisible.setEnabled(False)
            dir = QFileInfo(self.files[0]).absoluteDir().absolutePath()
            usingHeaderFile, layersStartDatetime = self.parseHeaderFile(dir)
            
            i = 0.0
            
            importStartTime = QDateTime.currentDateTime()
            self.printToResult("NEW IMPORT RUN\nStart: " + importStartTime.toString(self.timeFormat))
            
            #re for the temporal format
            temporalSearchPattern = re.compile(str(self.ui.temporalRegEx.text()))
            #re for the temporal format
            intervalSearchPattern = re.compile(str(self.ui.intervalRegEx.text()))
            #re to remove all non digit
            onlyDigits = re.compile(r'[^\d]+')
            
            if not usingHeaderFile:
                if not importStartTime.isValid():
                    layersStartDatetime = self.ui.startDatetime.dateTime()

            addedGroups = []
            
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
                    g = self.legend.addGroup(groupName, False )
                    self.legend.setGroupVisible(g, False)
                    self.printToResult("New group: " + groupName)
                    addedGroups.append(g)
                    
                #createLayer
                layer = QgsRasterLayer(filePath, fileBaseName)
                layerTime = layerTime.toString(self.timeFormat)
                #set time properties
                layer.setCustomProperty("isTemporalRaster", True)
                layer.setCustomProperty("temporalRasterIteration", layerName)
                layer.setCustomProperty("temporalRasterTime", layerTime)
                layer.setTransparency(127)
                
                #set symbology to pseudocolors
                layer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
                layer.setColorShadingAlgorithm(QgsRasterLayer.PseudoColorShader)
                
                #add layer to project
                if layer.isValid():
                    layer = QgsMapLayerRegistry.instance().addMapLayer(layer)
                    self.legend.setLayerVisible(layer, False)
                    layerWasAdded = "OK" if bool(layer) else "ERROR"
                    self.printToResult("Adding : " + fileBaseName + " with time: "+ layerTime +" -> " + layerWasAdded)
                    
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
             
            importEndTime = QDateTime.currentDateTime()
            self.printToResult("End: " + importEndTime.toString(self.timeFormat))
            self.printToResult("Duration: " + str(importStartTime.secsTo(importEndTime)) + " sec")
            self.main.writeStepDurations()
            
            #show layers if olprion was checked
            if self.ui.dataVisible.isChecked():
                for g in addedGroups:
                    self.legend.setGroupVisible(g, True)
            #update GUI
            self.main.isLoadingTemporalData = False
            self.ui.saveLogButton.setEnabled(True)
            self.ui.dataVisible.setEnabled(True)
            try:
                self.main.multiviewwidget.refreshAll()
            except:
                pass
    
    def parseHeaderFile(self, dir):
        useHeader = QMessageBox.question(self, "Header file found", "The Header file importHeader.xml has been found in the import directory, do you want to use it instead of the manually entered informations?",
         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if useHeader == QMessageBox.Yes:
            #TODO implement a real method
            self.main.stepDurations[QString('S0002')] = 864000
            self.main.stepDurations[QString('S0003')] = 86400
            self.main.stepDurations[QString('S0004')] = 14400
            return True, self.ui.startDatetime.dateTime()
        return False, False
        
        #file = QFile(dir+"/importHeader.xml")
        #xmlReader = QXmlSimpleReader()
        #source = QXmlInputSource(file)
        #handler = Handler()
        #xmlReader.setContentHandler(handler)
        #xmlReader.setErrorHandler(handler)
        #ok = xmlReader.parse(source)

        #if not ok:
            #return (False, False)
        #self.main.stepDurations[stepDurationText] = stepDuration
        #return (True, layersStartDatetime)

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
                         QDir.homePath (),
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
