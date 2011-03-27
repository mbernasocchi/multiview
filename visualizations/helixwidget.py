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
    
class Viewer(QGLViewer):
    def __init__(self, parent):
        QGLViewer.__init__(self)
        
        #config
        self.mainWidget = parent.mainWidget
        self.data = None
        self.PRECISION = 30
        self.timeStepsPerCycle = 5
        self.height = 10
        self.ribbonScale = 0.8
        self.subRibbonScale = 1
        self.minSaturation = 0.25
    
    
    def init(self):
        """OpenGL init, happens only once"""
        
        light_position = [ 1.0, 1.0, 1.0, 0.0 ]
        glShadeModel (GL_SMOOTH)
        
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0,0,0,1])
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        
#        self.setSceneRadius(100.0)          # scene has a 100 OpenGL units radius 
#        self.setSceneCenter( Vec(400,0,0) ) # with a center shifted by 400 units along X direction
        #self.camera().showEntireScene()

    def helpString(self):
        return helpstr
        
    def setData(self, data):
        self.data = data
        self.updateGL()
        
    def draw(self):
        '''Drawing routine'''
        # Draw Helix
        if (self.data == None):
            return
        
        data = []
        variableRange = []
        timeCounts  = []
        colors = []
        for (layerGroupName, values) in self.data.iteritems():
            timeCounts.append(len(values))
            x, y = zip(*values)
            minVal = min(y)
            maxVal = max(y)
            variableRange.append({'min':minVal, 'max':maxVal, 'range':maxVal-minVal})
            data.append(y)
            color = self.mainWidget.colors[QString(layerGroupName)]
            color = QColor.fromHsvF(color.hueF(), 1.0, color.valueF())
            colors.append(color)
        
        variablesCount = len(self.data)
        timeStepCount = max(timeCounts)
        
        #prepare ribbons values
        quadsPerTimeStep = 1 + self.PRECISION / self.timeStepsPerCycle # At least one quad per time step
        quadsPerCycle = quadsPerTimeStep * self.timeStepsPerCycle
        cycleCount = float( timeStepCount / self.timeStepsPerCycle )
        #transparency = getMapView().getFadingManager().getTransparency(a)
        ribbonHeight = self.height / (1 + cycleCount)
        subRibbonHeight = ribbonHeight * self.ribbonScale / variablesCount
        heightStepPerQuad = (self.height - ribbonHeight) / (timeStepCount * quadsPerTimeStep)
        angleStepPerQuad = 360.0 / quadsPerCycle
        sin = float( math.sin(angleStepPerQuad * math.pi / 180) )
        cos = float( (-1 * math.cos(angleStepPerQuad * math.pi / 180)) )
        
        #set the helix horizontal
        glRotatef(90, 0, 1, 0);
        
        glMatrixMode(GL_MODELVIEW)
        for t in range(0, timeStepCount):
            for j in range(0, quadsPerTimeStep):
                glPushMatrix()
                for v in range(0, variablesCount):
                    try:
                        #avoid division by 0 and normalizing values to 0-1 range
                        value = data[v][t]
                        if variableRange[v]['min'] > 0:
                            sat = ( value - variableRange[v]['min'] ) / variableRange[v]['range']
                        else:
                            sat = ( value + math.fabs((variableRange[v]['min'])) ) / variableRange[v]['range']
                        #add minSaturation
                        sat =  ( sat + self.minSaturation ) / ( 1 + self.minSaturation )
                        color = QColor.fromHsvF(colors[v].hueF(), sat, colors[v].valueF(),1.0)
                    except:
                        value = None
                    #print "Var: ", v, "Time: ", t, " Quad: ", j, '--> ', value    
                    
                    if value is not None:
                      #setOpenGL color
                      glColor4f(color.redF(),color.greenF(),color.blueF(),color.alphaF())
                      actualSubRibbonHeight  = subRibbonHeight * self.subRibbonScale
                      #start drawing QUADS
                      glBegin(GL_QUADS)
                      glVertex3f(0, -1, 0)
                      glVertex3f(0, -1, actualSubRibbonHeight)
                      glVertex3f(sin, cos, actualSubRibbonHeight + heightStepPerQuad)
                      glVertex3f(sin, cos, heightStepPerQuad)
                      glEnd()
                
                    glTranslatef(0, 0, subRibbonHeight)
                    
                glPopMatrix()
                glRotatef(angleStepPerQuad, 0, 0, 1)
                glTranslatef(0, 0, heightStepPerQuad)
                
                
                
###OTHER VARIANT                
#        for v in range(0, variablesCount):
#            glBegin(GL_QUAD_STRIP)
#            z=0
#            for t in range(0, timeStepCount):
#                angle = angleStepPerQuad * (t/float(timeStepCount))
#                #angle = math.radians(angle)
#                try:
#                    #avoid division by 0 and normalizing values to 0-1 range
#                    if variableRange[v]['min'] > 0:
#                        sat = ( data[v][t] - variableRange[v]['min'] ) / variableRange[v]['range']
#                    else:
#                        sat = ( data[v][t] + math.fabs((variableRange[v]['min'])) ) / variableRange[v]['range']
#                        
#                    #add minSaturation
#                    sat =  ( sat + self.minSaturation ) / ( 1 + self.minSaturation )
#                    color = QColor.fromHsvF(colors[v].hueF(), sat, colors[v].valueF(),1.0)
#                except:
#                    #color for NODATA
#                    color = self.nodataColor 
#               
#                #setOpenGL color
#                glColor4f(color.redF(),color.greenF(),color.blueF(),color.alphaF())
#                
#                size = 0.1
#                
#                z += size
#                y = math.cos(angle)
#                x = math.sin(angle)
#                
#                #tl
#                glVertex3f(x,y,z)
#                #bl
#                glVertex3f(x,y,z-size)
#            glEnd()
#            glTranslatef(0.0, 0.0, size)



helpstr = """<h2>Helix V i e w e r</h2>
Use the mouse to move the camera around the helix. 
You can respectively revolve around, zoom and translate with the three mouse buttons. 
Left and middle buttons pressed together rotate around the camera view direction axis<br><br>
Press <b>F</b> to display the frame rate, <b>A</b> for the world axis, 
<b>Alt+Return</b> for full screen mode and <b>Control+S</b> to save a snapshot. 
See the <b>Keyboard</b> tab in this window for a complete shortcut list.<br><br>
Double clicks automates single click actions: A left button double click aligns 
the closer axis with the camera (if close enough). A middle button double click 
fits the zoom of the camera and the right button re-centers the scene.<br><br>
A left button double click while holding right button pressed defines the camera 
<i>Revolve Around Point</i>.
See the <b>Mouse</b> tab and the documentation web pages for details.<br><br>
Press <b>Escape</b> to exit the viewer."""
   
