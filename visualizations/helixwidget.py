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
from PyQt4.Qwt3D import *
from PyQt4.Qwt3D.OpenGL import *

import sys
from math import log
#try:
#    from PyQt4.Qwt3D import *
#except:
#    print "PyQt4.Qwt3D needed for this visualization"
#    print "please get it at http://qwtplot3d.sourceforge.net/"
    
from ui_helixwidget import Ui_HelixWidget

# create the dialog for zoom to point
class HelixWidget(QWidget):
    def __init__(self, mainWidget, main):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_HelixWidget()
        self.ui.setupUi(self)
        self.main = main #main plugin file
        self.mainWidget = mainWidget #multiview widget
        self.plot = SurfacePlot(self)
        self.plot.setGeometry(QRect(10, 40, 341, 231))
        
        
        
        
            
        self.plot.setTitle('A Simple SurfacePlot Demonstration');
        self.plot.setBackgroundColor(RGBA(1.0, 1.0, 0.6))

        rosenbrock = Rosenbrock(self.plot)

        rosenbrock.setMesh(41, 31)
        rosenbrock.setDomain(-1.73, 1.5, -1.5, 1.5)
        rosenbrock.setMinZ(-10)
        
        rosenbrock.create()

        self.plot.setRotation(30, 0, 15)
        self.plot.setScale(1, 1, 1)
        self.plot.setShift(0.15, 0, 0)
        self.plot.setZoom(0.9)

        axes = self.plot.coordinates().axes # alias
        for axis in axes:
            axis.setMajors(7)
            axis.setMinors(4)
            
        axes[X1].setLabelString('x-axis')
        axes[Y1].setLabelString('y-axis')
        axes[Z1].setLabelString('z-axis')

        self.plot.setCoordinateStyle(BOX);

        self.plot.updateData();
        self.plot.updateGL();

        
    def name(self):
        return "Helix"
    
    def redraw(self, values, recalculateBonds=True):
        print str(values)
        
#            RenderingContext rc = getRenderingContext();
#            // Draw Helix
#            rc.gl.glEnable(GL.GL_BLEND);
#            rc.gl.glEnable(GL.GL_DEPTH_TEST);
#            rc.gl.glTranslated(a.getBounds().getCenterX(), a.getBounds().getCenterY(), 0);
#
#            rc.gl.glScalef(perimeter, perimeter, 1);
#            rc.gl.glRotatef(rotationAngle, 0, 0, 1);
#
#            int data[][] = a.getData(this);
#            if (data == null) return;
#            int timeStepCount = data.length;
#            int diagnosesCount = data[0].length;
#
#            float[] maxPerDiagnosis = new float[diagnosesCount];
#            for (int d = 0; d < diagnosesCount; d++) {
#                for (int i = 0; i < timeStepCount; i++) {
#                    if (data[i][d] > maxPerDiagnosis[d]) maxPerDiagnosis[d] = data[i][d];
#                }
#            }
#
#            int quadsPerTimeStep = 1 + PRECISION / timeStepsPerCycle; // At least one quad per time step
#            int quadsPerCycle = quadsPerTimeStep * timeStepsPerCycle;
#
#            float cycleCount = (float) timeStepCount / timeStepsPerCycle;
#            float transparency = getMapView().getFadingManager().getTransparency(a);
#            float ribbonHeight = height / (1 + cycleCount);
#            float subRibbonHeight = ribbonHeight * ribbonScale / diagnosesCount;
#
#            // h = hs * ts * qt + rh
#            // h - rh = hs * ts * qt
#            // (h - rh)
#            // ------ = hs
#            // (ts * qt)
#            float heightStepPerQuad = (height - ribbonHeight) / (timeStepCount * quadsPerTimeStep);
#            float angleStepPerQuad = 360f / quadsPerCycle;
#            float sin = (float) Math.sin(angleStepPerQuad * Math.PI / 180);
#            float cos = (float) (-1 * Math.cos(angleStepPerQuad * Math.PI / 180));
#
#            rc.gl.glMatrixMode(GL.GL_MODELVIEW);
#            for (int i = 0; i < timeStepCount; i++) {
#                for (int j = 0; j < quadsPerTimeStep; j++) {
#                    rc.gl.glPushMatrix();
#                    for (int d = 0; d < diagnosesCount; d++) {
#                        float t = data[i][d] / maxPerDiagnosis[d];
#                        colorScales[d % colorScales.length].getColor(t).getColorComponents(rc.c);
#                        rc.c[3] = transparency;
#                        rc.gl.glColor4fv(rc.c, 0);
#
#                        rc.gl.glBegin(GL.GL_QUADS);
#                        rc.gl.glVertex3f(0, -1, 0);
#                        rc.gl.glVertex3f(0, -1, subRibbonHeight * subRibbonScale);
#                        rc.gl.glVertex3f(sin, cos, subRibbonHeight * subRibbonScale + heightStepPerQuad);
#                        rc.gl.glVertex3f(sin, cos, heightStepPerQuad);
#                        rc.gl.glEnd();
#
#                        rc.gl.glTranslatef(0, 0, subRibbonHeight);
#                    }
#                    rc.gl.glPopMatrix();
#                    rc.gl.glRotatef(angleStepPerQuad, 0, 0, 1);
#                    rc.gl.glTranslatef(0, 0, heightStepPerQuad);
#                }
#            }
#    }
        
    def reset(self):
        print "reset"
        
class Rosenbrock(Function):

    def __init__(self, *args):
        Function.__init__(self, *args)

    # __init__()

    def __call__(self, x, y):
        return log((1-x)*(1-x) + 100*(y-x*x)*(y-x*x)) / 8

    # __call__()

# class Rosenbrock

        
