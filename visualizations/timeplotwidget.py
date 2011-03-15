"""
/***************************************************************************
 TimePlotWidget - shows the values as Parallel Coordinates Plot
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
    
from ui_timeplotwidget import Ui_TimePlotWidget

# create the dialog for zoom to point
class TimePlotWidget(QWidget):
    def __init__(self, main):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TimePlotWidget()
        self.ui.setupUi(self)
        self.main = main
        self.timeFormat = self.main.timeFormat
        self.plot = self.ui.qwtPlot
        
        #setup plot
        #self.plot.setAxisTitle(QwtPlot.xBottom, "Time")
        self.plot.setAxisTitle(QwtPlot.yLeft, "Value")
    
    def name(self):
        return "TimePlot"
    
    def redraw(self, valuesArray):
        self.reset()
        ticks = []
        #add curves
        for (layerGroupName, values) in valuesArray.iteritems():
            x = []
            y = []
            for value in values:
                x.append(value[0])
                y.append(value[1])
            
            color = self.main.colors[QString(layerGroupName)]
            curve = QwtPlotCurve(layerGroupName)
            curve.setSymbol(QwtSymbol(QwtSymbol.Ellipse, QBrush(Qt.white), QPen(color), QSize(5,5)))
            curve.setPen(QPen(color))   
            curve.setData(x, y)
            curve.attach(self.plot)
            ticks = list(set.union(set(ticks), set(x)))
        
        if len(ticks) > 0:
            ticks.sort()
            #update axes
            div = QwtScaleDiv()
            div.setInterval(ticks[0], ticks[len(ticks)-1])
            div.setTicks(QwtScaleDiv.MinorTick, [])
            div.setTicks(QwtScaleDiv.MediumTick, [])
            div.setTicks(QwtScaleDiv.MajorTick, ticks)
            draw = TimeScaleDraw(QDateTime(self.main.timeMin))
            draw.setScaleDiv(div)
            self.plot.setAxisScaleDraw(QwtPlot.xBottom, draw)
            self.plot.setAxisScale(QwtPlot.yLeft, self.main.valueMin, self.main.valueMax)
        
        #finally, refresh the plot
        self.plot.replot()
        
    def reset(self):
        self.plot.detachItems()
        self.plot.replot()
        
        
class TimeScaleDraw(QwtScaleDraw):
    def __init__(self, baseTime):
        QwtScaleDraw.__init__(self)
        #QTime baseTime
        self.baseTime = baseTime
        self.setLabelAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.setLabelRotation(-25.0)

    def label(self, secs):
        upTime = self.baseTime.addSecs(secs)
        upTime = upTime.toString('dd MM yy hh:mm:ss')
        return QwtText(upTime)
    
