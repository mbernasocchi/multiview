"""
/***************************************************************************
 PlotWidget - shows the values as xy plots
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
    
from ui_plotwidget import Ui_PlotWidget

# create the dialog for zoom to point
class PlotWidget(QWidget):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_PlotWidget()
        self.ui.setupUi(self)
    
    def name(self):
        return "Plot"
    
    def redraw(self, valuesArray):
        self.reset()
        #add curves
        numVars = len(valuesArray)
        i = 0
        for (var, values) in valuesArray.iteritems():
            curve = QwtPlotCurve(var)
            curve.setStyle(QwtPlotCurve.Lines)
            color = QColor.fromHsv( int(360 / numVars * i), 255, 255 )
            curve.setPen(QPen(color))
            curve.setData(values.keys(), values.values())
            curve.attach(self.ui.qwtPlot)
            i +=1
        #finally, refresh the plot
        self.ui.qwtPlot.replot()
        
    def reset(self):
        self.ui.qwtPlot.detachItems()
        self.ui.qwtPlot.replot()
        
