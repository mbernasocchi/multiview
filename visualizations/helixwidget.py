"""
/***************************************************************************
 HelixWidget - shows the values in an helix based on Tominski 2005
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
import sys
import math
import fractions

try:
    from PyQGLViewer import *
    from OpenGL.GL import *
except:
    raise ImportError("PyQGLViewer needed for this visualization \n\
		please get it at:\n\
		http://hub.qgis.org/projects/multiview/documents")

from ui_helixwidget import Ui_HelixWidget

# create the dialog for zoom to point
class HelixWidget(QWidget):
    def __init__(self, mainWidget, main):
        QWidget.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_HelixWidget()
        self.ui.setupUi(self)
        self.main = main #main plugin file
        self.mainWidget = mainWidget #multiview widget
        self.warningDisplay = self.ui.warningDisplay
        
        self.viewer = Viewer(self)
        self.viewer.setObjectName("viewer")
        self.viewer.setSizePolicy( QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.ui.verticalLayout.insertWidget(1, self.viewer)
        
    def name(self):
        return "Helix"
    
    def redraw(self, valuesArray, recalculateBonds=True):
        self.viewer.setData(valuesArray)
        
    def reset(self):
        self.viewer.setData(None)
    
    def help(self):
        self.viewer.help()
        
    @pyqtSlot(int)
    def on_sizePerCycle_valueChanged(self, value):
        self.mainWidget.redraw(False)
    
    @pyqtSlot(int)
    def on_unitPerCycle_currentIndexChanged(self, value):
        self.mainWidget.redraw(False)
        
    @pyqtSlot(float)
    def on_minSaturation_valueChanged(self, value):
        self.mainWidget.redraw(False)
    
    @pyqtSlot(float)
    def on_textOffset_valueChanged(self, value):
        self.mainWidget.redraw(False)
    
    @pyqtSlot(int)
    def on_precision_valueChanged(self, value):
        self.mainWidget.redraw(False)
    
    @pyqtSlot(float)
    def on_ribbonWidth_valueChanged(self, value):
        self.mainWidget.redraw(False)
        
    @pyqtSlot(str)
    def on_interpolationMethod_currentIndexChanged(self, value):
        self.mainWidget.redraw(False)
        
    
    
class Viewer(QGLViewer):
    def __init__(self, parent):
        QGLViewer.__init__(self)
        
        #INIT
        self.main = parent.main
        self.mainWidget = parent.mainWidget
        self.ui = parent.ui
        self.rawdata = None
    
    
    def init(self):
        """OpenGL init, happens only once"""
        #prevent saving the state on exit
        self.setStateFileName(QString())
        #lighting
        glDisable(GL_LIGHTING)

    def helpString(self):
        '''Returns the help string for the help dialog'''
        return helpstr
        
    def setData(self, rawdata):
        '''Set new raw data and call a repaint'''
        self.rawdata = rawdata
        if self.rawdata is not None:
            #find the greatest Common Divisor of the time step units of the selected variables
            durations = []
            for (layerGroupName, values) in self.rawdata.iteritems():
                layerGroupName = QString(layerGroupName)
                d = self.mainWidget.availableVariables[layerGroupName]['duration']
                if d not in durations:
                  durations.append(d)
            self.timeUnit = self.greatestCommonDivisor(durations)
            
            if len(durations) > 1:
                self.mainWidget.showWarning("Multiple temporal resolutions Data. See help for details")
                self.ui.interpolationMethod.setEnabled(True)
            else:
                self.ui.interpolationMethod.setEnabled(False)
            
            self.data = []
            self.variables = []
            self.colors = []
            self.timeStepCount = self.mainWidget.maxTimeDelta / self.timeUnit
            
            #create an array with the same ammount of elements for each variables
            #if a variable has a lower temporal resolution than another
            #the array values of the values outside the first-last range 
            #is filled with None.
            #the elements in the first-last range are interpolated linearly
            for (layerGroupName, values) in self.rawdata.iteritems():
                layerGroupName = QString(layerGroupName)
                
                data = [None] * (self.timeStepCount+1)
                minVal = sys.maxint
                maxVal = -sys.maxint
                
                isFirstStep = True
                for t,v in values:
                    #divide the timestep value by the greatest common divisor
                    timeStep = t/self.timeUnit
                    #insert existing point into the array
                    data[timeStep] = v
                    #rawdata = list(data)
                    #update layerGroupName min and max
                    if v < minVal:
                        minVal = v
                    if v > maxVal:
                        maxVal = v
                    
                    if isFirstStep == True:
                        isFirstStep = False
                    else:
                        interpolatedV = None
                        for j in range(lastTimeStep, timeStep):
                            #number of interpolation steps needed
                            steps = timeStep
                            #+1 so that the counter starts from 1
                            step = j
                            if lastTimeStep is not 0:
                                #normalize value to 1 - lastTimeStep
                                steps = steps - lastTimeStep
                                step = step - lastTimeStep
                                
                            if self.ui.interpolationMethod.currentText() == 'Linear':
                                delta = v - lastV
                                deltaStep = delta / steps
                                interpolatedV = lastV + deltaStep * step
                                #print lastV, v, delta, deltaStep, interpolatedV
                                
                            elif self.ui.interpolationMethod.currentText() == 'Previous Value':
                                interpolatedV = lastV
                                
                            elif self.ui.interpolationMethod.currentText() == 'Nearest Neighbor':
                                if step <= steps/2:
                                    interpolatedV = lastV
                                else:
                                    interpolatedV = v
                            elif self.ui.interpolationMethod.currentText() == 'None':
                                interpolatedV = None
                            
                            if data[j] is None:
                                data[j] = interpolatedV
                    lastTimeStep = timeStep
                    lastV = v
                #print rawdata
                #print data    
                self.variables.append({'min':minVal, 'max':maxVal, 'range':maxVal-minVal,
                                       'name':self.mainWidget.availableVariables[layerGroupName]['readableName']})
                self.data.append(data)
                color = self.mainWidget.availableVariables[layerGroupName]['color']
                
                color = QColor.fromHsvF(color.hueF(), 1.0, color.valueF())
                self.colors.append(color)
            
            self.variablesCount = len(self.rawdata)
            
            unitMultiplier = 1 #seconds
            if self.ui.unitPerCycle.currentText() == 'Day(s)':
                                unitMultiplier = 86400#60*60*24
            elif self.ui.unitPerCycle.currentText() == 'Years(s)':
                                unitMultiplier = 31557600#60*60*24*365.25
            
            self.TIMESTEPSPERCYCLE = float(self.ui.sizePerCycle.value() * unitMultiplier) / float(self.timeUnit)
            self.HEIGHT = self.TIMESTEPSPERCYCLE*2
            #set the scene to fit the helix and make the helix rotate arount it's middle
            self.setSceneCenter(Vec(self.HEIGHT/2,0,0))
            self.setSceneRadius(self.HEIGHT/2.5)
            self.showEntireScene()
        self.updateGL()
        
    def greatestCommonDivisor(self, values):
        '''Calculates the greatest common divisor of a list'''
        if len(values) == 1:
            return values[0]
        else:
            gcd = fractions.gcd(values[0], values[1])
            
            for i in range(2, len(values)):
                gcd = fractions.gcd( gcd, values[i] )
                if gcd == 1:
                    break
            return gcd
    
    def draw(self):
        '''Drawing routine wrapper'''
         # Draw Helix
        self.drawWithNames()
        
    def drawWithNames(self):
        '''Drawing routine'''
        if self.rawdata is None:
            return
        glMatrixMode(GL_MODELVIEW)
        
        #SETTINGS from GUI:
        self.PRECISION = self.ui.precision.value()
        self.MINSATURATION = self.ui.minSaturation.value()
        self.RIBBONSCALE = self.ui.ribbonWidth.value()
        self.TEXTOFFSET  = self.ui.textOffset.value()
        
        #prepare ribbons values
        quadsPerTimeStep = 1 + self.PRECISION # At least one quad per time step
        quadsPerCycle = quadsPerTimeStep * self.TIMESTEPSPERCYCLE
        cycleCount = float( self.timeStepCount / self.TIMESTEPSPERCYCLE )
        #transparency = getMapView().getFadingManager().getTransparency(a)
        ribbonHeight = self.HEIGHT / (1 + cycleCount)
        subRibbonHeight = ribbonHeight * self.RIBBONSCALE / self.variablesCount
        heightStepPerQuad = (self.HEIGHT - ribbonHeight) / (self.timeStepCount * quadsPerTimeStep)
        angleStepPerQuad = 360.0 / quadsPerCycle
        sin = float( math.sin(angleStepPerQuad * math.pi / 180) )
        cos = float( (-1 * math.cos(angleStepPerQuad * math.pi / 180)) )
        
        #set the helix horizontal
        glRotatef(90, 0, 1, 0)
        
        quadID = 0
        self.quadIdInfo = []
        for t in range(0, self.timeStepCount):
            #print time labels
            #TODO limit number of labels
            if (t % self.TIMESTEPSPERCYCLE == 0 ) or \
             (t % self.TIMESTEPSPERCYCLE == self.TIMESTEPSPERCYCLE/2):
                self.qglColor(self.foregroundColor())
                time = QDateTime(self.mainWidget.timeMin)
                for v in range(0, self.variablesCount):
                    try:
                        time = time.addSecs(t * self.timeUnit)
                        break
                    except:
                      pass
                time = time.toString('dd MM yy hh:mm:ss')
                self.renderText(0, -1-self.TEXTOFFSET, 0, time)
            
            for j in range(0, quadsPerTimeStep):
                glPushMatrix()
                for v in range(0, self.variablesCount):
                    #avoid division by 0 and normalizing values to 0-1 range
                    try: 
                      value = self.data[v][t]
                      if self.variables[v]['range'] == 0:
                        sat = 0
                      else:
                        if self.variables[v]['min'] > 0:
                            sat = ( value - self.variables[v]['min'] ) / self.variables[v]['range']
                        else:
                            sat = ( value + abs((self.variables[v]['min'])) ) / self.variables[v]['range']
                      #add minSaturation
                      adjustedSat =  ( sat + self.MINSATURATION ) / ( 1 + self.MINSATURATION )
                      color = QColor.fromHsvF(self.colors[v].hueF(), adjustedSat, self.colors[v].valueF(),1.0)
                    except:
                      value = None
                    
                    if value is not None:
                      #setOpenGL color
                      self.qglColor(color)
                      self.quadIdInfo.append(\
                        {'var':v, 'time':t, 'quad': j, 'value': value,\
                         'varInfos':self.variables[v], 'ratio':sat} )
                      #start drawing QUADS
                      glPushName(quadID)
                      glBegin(GL_QUADS)
                      glVertex3f(0, -1, 0)
                      glVertex3f(0, -1, subRibbonHeight)
                      glVertex3f(sin, cos, subRibbonHeight + heightStepPerQuad)
                      glVertex3f(sin, cos, heightStepPerQuad)
                      glEnd()
                      glPopName()
                      quadID += 1
                      
                    glTranslatef(0, 0, subRibbonHeight)
                    
                glPopMatrix()
                glRotatef(angleStepPerQuad, 0, 0, 1)
                glTranslatef(0, 0, heightStepPerQuad)
        
    def postSelection(self,point):
        '''Executed after a selection has been made in the plot'''
        # Find the selectedPoint coordinates, using camera()->pointUnderPixel().
        self.selectedPoint, found = self.camera().pointUnderPixel(point)
        
        if self.selectedName() == -1:
             self.displayMessage("No object selected under pixel " + str(point.x()) + "," + str(point.y()))
        else:
            info = self.quadIdInfo[self.selectedName()]
            infoMsg = str(info['varInfos']['name']) + ' @ ' + str(info['time']) +\
            ':' + str(info['quad']) + ' = ' + str(info['value']) +\
            ' (range: ' + str(info['varInfos']['min']) + ' - ' + str(info['varInfos']['max']) +\
            ' -> ' + str(int(info['ratio']*100)) + '%)'
            self.displayMessage(infoMsg, 5000)
                

helpstr = """<h2>Helix V i e w e r</h2>
Use the mouse to move the camera around the helix. 
You can respectively revolve around, zoom and translate with the three mouse buttons. 
Left and middle buttons pressed together rotate around the camera view direction axis<br/><br/>
Press SHIFT and left Mouse to get information about the selected time<br/><br/>
Press <b>F</b> to display the frame rate, <b>A</b> for the world axis, 
<b>Alt+Return</b> for full screen mode and <b>Control+S</b> to save a snapshot. 
See the <b>Keyboard</b> tab in this window for a complete shortcut list.<br/><br/>
Double clicks automates single click actions: A left button double click aligns 
the closer axis with the camera (if close enough). A middle button double click 
fits the zoom of the camera and the right button re-centers the scene.<br/><br/>
A left button double click while holding right button pressed defines the camera 
<i>Revolve Around Point</i>.
See the <b>Mouse</b> tab and the documentation web pages for details.
<h3>Warnings</h3>
<ul><li>Multiple temporal resolutions Data:<br/>The variables selected have different temporal resolutions.
The data with lower resolution (longer interval between each sample) are interpolated using the chosen interpolation method"""
   
