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
    def __init__(self, mainWidget, main):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TimePlotWidget()
        self.ui.setupUi(self)
        self.main = main #main plugin file
        self.mainWidget = mainWidget #multiview widget
        self.timeFormat = self.main.timeFormat
        self.plot = self.ui.qwtPlot
        self.isFirstRedraw = True
        
        print "pr: "+ self.plot.grabProperties()
        
        self.picker = TimeScalePicker(
            QwtPlot.xBottom,
            QwtPlot.yLeft,
            QwtPicker.PointSelection | QwtPicker.DragSelection,
            QwtPlotPicker.CrossRubberBand,
            QwtPicker.AlwaysOn,
            self.plot.canvas())
        self.picker.setRubberBandPen(QPen(Qt.blue))
        self.picker.setTrackerPen(QPen(Qt.blue))
        
        self.zoomer = QwtPlotZoomer(
            QwtPlot.xBottom,
            QwtPlot.yLeft,
            QwtPicker.DragSelection,
            QwtPicker.AlwaysOff,
            self.plot.canvas())
        self.zoomer.setRubberBandPen(QPen(Qt.darkBlue))
        self.zoomEnabled(False)
        
        QObject.connect(self.ui.zoomButton, SIGNAL("toggled(bool)"), self.zoomEnabled)
        
        #setup plot
        self.plot.setAxisTitle(QwtPlot.yLeft, "Value")
    
    def name(self):
        return "TimePlot"
    
    def redraw(self, valuesArray, recalculateBonds=True):
        self.reset()
        ticks = []
        
        #add curves
        for (layerGroupName, values) in valuesArray.iteritems():
            x = []
            y = []
            for value in values:
                x.append(value[0])
                y.append(value[1])
            
            color = self.mainWidget.colors[QString(layerGroupName)]
            curve = QwtPlotCurve(layerGroupName)
            curve.setSymbol(QwtSymbol(QwtSymbol.Ellipse, QBrush(Qt.white), QPen(color), QSize(5,5)))
            curve.setPen(QPen(color))   
            curve.setData(x, y)
            curve.attach(self.plot)
            ticks = list(set.union(set(ticks), set(x)))
        
        if len(ticks) > 0 and self.isFirstRedraw:
            #init zoom base
            self.zoomer.setZoomBase()
            
        if len(ticks) > 0 and (self.isFirstRedraw or recalculateBonds):
            ticks.sort()
            #update axes
            div = QwtScaleDiv()
            div.setInterval(ticks[0], ticks[len(ticks)-1])
            div.setTicks(QwtScaleDiv.MinorTick, [])
            div.setTicks(QwtScaleDiv.MediumTick, [])
            div.setTicks(QwtScaleDiv.MajorTick, ticks)
            baseTime = QDateTime(self.mainWidget.timeMin)
            draw = TimeScaleDraw(baseTime)
            draw.setScaleDiv(div)
            #self.plot.setAxisScaleDiv(QwtPlot.xBottom, div)
            self.plot.setAxisScaleDraw(QwtPlot.xBottom, draw)
            self.plot.setAxisScale(QwtPlot.yLeft, self.mainWidget.valueMin, self.mainWidget.valueMax)
            
            # reinitialize the scale
            self.picker.updateBaseTime(baseTime)
            #update zoom base
            tl = QPointF(min(ticks), self.mainWidget.valueMax)
            br = QPointF(max(ticks), self.mainWidget.valueMin)
            self.zoomer.setZoomBase(QRectF(tl, br)) 
        #finally, refresh the plot
        print self.zoomer.zoomBase()
        self.isFirstRedraw = False
        self.plot.replot()
        
        
    def reset(self):
        self.plot.detachItems()
        self.plot.replot()
    
    def zoomEnabled(self, on):
        self.zoomer.setEnabled(on)
        
        if on:
            self.picker.setRubberBand(QwtPicker.NoRubberBand)
        else:
            self.zoomer.zoom(0)
            self.picker.setRubberBand(QwtPicker.CrossRubberBand)

        
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

class TimeScalePicker(QwtPlotPicker):
    def __init__(self, xAxis, yAxis, selectionFlags, rubberBand, trackerMode, QwtPlotCanvas ):
        QwtPlotPicker.__init__(self, xAxis, yAxis, selectionFlags, rubberBand, trackerMode, QwtPlotCanvas)
        self.baseTime = QDateTime()
        
    def updateBaseTime(self, baseTime):
        self.baseTime = baseTime
        
    def trackerText (self, clickPos):
        pos = self.invTransform(clickPos)
        upTime = self.baseTime.addSecs(pos.x())
        upTime = upTime.toString('dd MM yy hh:mm:ss')
        text = QwtText(upTime + " || " + str(pos.y()))
        bgColor = QColor(Qt.white)
        bgColor.setAlpha(127)
        text.setBackgroundBrush(QBrush(bgColor))
        return text
    
    
    
    
    
