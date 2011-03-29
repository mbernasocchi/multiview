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
import math

try:
    from PyQGLViewer import *
    from OpenGL.GL import *
except:
    raise ImportError("PyQGLViewer needed for this visualization \nplease get it at http://pyqglviewer.gforge.inria.fr")

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
        
        self.viewer = Viewer(self)
        self.viewer.setObjectName("viewer")
        self.viewer.setSizePolicy( QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.ui.verticalLayout.insertWidget(0, self.viewer)
        
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
    
class Viewer(QGLViewer):
    def __init__(self, parent):
        QGLViewer.__init__(self)
        
        #INIT
        self.mainWidget = parent.mainWidget
        self.ui = parent.ui
        self.rawdata = None
    
    
    def init(self):
        """OpenGL init, happens only once"""
        
        self.TIMESTEPSPERCYCLE = 7
        self.HEIGHT = self.TIMESTEPSPERCYCLE*2
        
        
        #prevent saving the state on exit
        self.setStateFileName(QString())
        #lighting
        glDisable(GL_LIGHTING)
        
        self.setSceneCenter(Vec(self.HEIGHT/2,0,0))
        self.setSceneRadius(self.HEIGHT/2.5)
        self.showEntireScene()

    def helpString(self):
        return helpstr
        
    def setData(self, rawdata):
        self.rawdata = rawdata
        self.updateGL()
        
    def draw(self):
        self.drawWithNames()
        
    def drawWithNames(self):
        '''Drawing routine'''
        # Draw Helix
        if (self.rawdata == None):
            return
        
        #SETTINGS from GUI:
        self.PRECISION = self.ui.precision.value()
        self.MINSATURATION = self.ui.minSaturation.value()
        self.RIBBONSCALE = self.ui.ribbonWidth.value()
        self.TEXTOFFSET  = self.ui.textOffset.value()
        
        data = []
        times = []
        variables = []
        timeCounts  = []
        colors = []
        for (layerGroupName, values) in self.rawdata.iteritems():
            timeCounts.append(len(values))
            print values
            x, y = zip(*values)
            minVal = min(y)
            maxVal = max(y)
            variables.append({'min':minVal, 'max':maxVal, 'range':maxVal-minVal, 'name':layerGroupName})
            data.append(y)
            times.append(x)
            color = self.mainWidget.colors[QString(layerGroupName)]
            color = QColor.fromHsvF(color.hueF(), 1.0, color.valueF())
            colors.append(color)
        
        variablesCount = len(self.rawdata)
        timeStepCount = max(timeCounts)
        
        #prepare ribbons values
        quadsPerTimeStep = 1 + self.PRECISION # At least one quad per time step
        quadsPerCycle = quadsPerTimeStep * self.TIMESTEPSPERCYCLE
        cycleCount = float( timeStepCount / self.TIMESTEPSPERCYCLE )
        #transparency = getMapView().getFadingManager().getTransparency(a)
        ribbonHeight = self.HEIGHT / (1 + cycleCount)
        subRibbonHeight = ribbonHeight * self.RIBBONSCALE / variablesCount
        heightStepPerQuad = (self.HEIGHT - ribbonHeight) / (timeStepCount * quadsPerTimeStep)
        angleStepPerQuad = 360.0 / quadsPerCycle
        sin = float( math.sin(angleStepPerQuad * math.pi / 180) )
        cos = float( (-1 * math.cos(angleStepPerQuad * math.pi / 180)) )
        
        #set the helix horizontal
        glRotatef(90, 0, 1, 0)
        
        quadID = 0
        self.quadIdInfo = []
        glMatrixMode(GL_MODELVIEW)
        
        for t in range(0, timeStepCount):
            #print time labels
            if (t % self.TIMESTEPSPERCYCLE == 0 ) or \
             (t % self.TIMESTEPSPERCYCLE == self.TIMESTEPSPERCYCLE/2):
                self.qglColor(self.foregroundColor())
                time = QDateTime(self.mainWidget.timeMin)
                for v in range(0, variablesCount):
                    try:
                        time = time.addSecs(times[v][t])
                        break
                    except:
                      pass
                time = time.toString('dd MM yy hh:mm:ss')
                self.renderText(0, -1-self.TEXTOFFSET, 0, time)
            
            for j in range(0, quadsPerTimeStep):
                glPushMatrix()
                for v in range(0, variablesCount):
                    #avoid division by 0 and normalizing values to 0-1 range
                    try: 
                      value = data[v][t]
                      if variables[v]['range'] == 0:
                        sat = 0
                      else:
                        if variables[v]['min'] > 0:
                            sat = ( value - variables[v]['min'] ) / variables[v]['range']
                        else:
                            sat = ( value + math.fabs((variables[v]['min'])) ) / variables[v]['range']
                      #add minSaturation
                      adjustedSat =  ( sat + self.MINSATURATION ) / ( 1 + self.MINSATURATION )
                      color = QColor.fromHsvF(colors[v].hueF(), adjustedSat, colors[v].valueF(),1.0)
                    except:
                      value = None
                    
                    if value is not None:
                      #setOpenGL color
                      self.qglColor(color)
                      self.quadIdInfo.append(\
                        {'var':v, 'time':t, 'quad': j, 'value': value,\
                         'varInfos':variables[v], 'ratio':sat} )
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
Left and middle buttons pressed together rotate around the camera view direction axis<br><br>
Press SHIFT and left Mouse to get information about the selected time<br/><br/>
Press <b>F</b> to display the frame rate, <b>A</b> for the world axis, 
<b>Alt+Return</b> for full screen mode and <b>Control+S</b> to save a snapshot. 
See the <b>Keyboard</b> tab in this window for a complete shortcut list.<br><br>
Double clicks automates single click actions: A left button double click aligns 
the closer axis with the camera (if close enough). A middle button double click 
fits the zoom of the camera and the right button re-centers the scene.<br><br>
A left button double click while holding right button pressed defines the camera 
<i>Revolve Around Point</i>.
See the <b>Mouse</b> tab and the documentation web pages for details."""
   
