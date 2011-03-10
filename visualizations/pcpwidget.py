"""
/***************************************************************************
 PCPWidget - shows the values as Parallel Coordinates Plot
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

hasqwt = True
try:
    from PyQt4.Qwt5 import *
except:
    hasqwt = False
    
from ui_pcpwidget import Ui_PCPWidget

# create the dialog for zoom to point
class PCPWidget(QWidget):
    def __init__(self, main):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_PCPWidget()
        self.ui.setupUi(self)
        self.main = main
    
    def name(self):
        return "PCP"
    
    def redraw(self, valuesArray):
        self.reset()
        #add curves
        for (layerGroupName, values) in valuesArray.iteritems():
            color = self.main.colors[QString(layerGroupName)]
            curve = QwtPlotCurve(layerGroupName)
            curve.setSymbol(QwtSymbol(QwtSymbol.Ellipse, QBrush(Qt.white), QPen(color), QSize(5,5)))
            curve.setPen(QPen(color))
            curve.setData(values.keys(), values.values())
            curve.attach(self.ui.qwtPlot)
        self.ui.qwtPlot.setAxisScale(0,0,self.main.maxValue)
        #finally, refresh the plot
        self.ui.qwtPlot.replot()
        
    def reset(self):
        self.ui.qwtPlot.detachItems()
        self.ui.qwtPlot.replot()
        
