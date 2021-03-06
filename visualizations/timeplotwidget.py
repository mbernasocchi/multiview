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

from abstractvisualisationwidget import AbstractVisualisationWidget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    from PyQt4.Qwt5  import *
except:
    raise ImportError("PyQt4.Qwt5 needed for this visualization \nPlease get it at http://pyqwt.sourceforge.net")
    
from ui_timeplotwidget import Ui_TimePlotWidget

# pcp like time plot class
class TimePlotWidget(AbstractVisualisationWidget):
    def __init__(self, mainWidget, main):
        AbstractVisualisationWidget.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_TimePlotWidget()
        self.ui.setupUi(self)
        self.main = main #main plugin file
        self.mainWidget = mainWidget #multiview widget
        self.plot = self.ui.qwtPlot
        self.warningDisplay = self.ui.warningDisplay
        
        self.isFirstRedraw = True
        
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
        
    def canvasWidget(self):
        return self.plot
    
    def redraw(self, valuesArray, recalculateBonds=True):
        self.reset()
        if valuesArray is None:
            return
        
        ticks = []
        
        #add curves
        for (layerGroupName, values) in valuesArray.iteritems():
            x = []
            y = []
            for value in values:
                x.append(value[0])
                y.append(value[1])
            
            color = self.mainWidget.availableVariables[QString(layerGroupName)]['color']
            curve = QwtPlotCurve(layerGroupName)
            pointSize = self.ui.pointSize.value()
            curve.setSymbol(QwtSymbol(QwtSymbol.Ellipse, QBrush(Qt.white), QPen(color), QSize(pointSize,pointSize)))
            
            pen = QPen(color)
            pen.setWidth(self.ui.lineWidth.value())
            pen.setDashOffset(self.ui.dashOffset.value())
            pen.setDashPattern(eval(str(self.ui.dashPattern.text())))
            curve.setPen(pen)   
            curve.setData(x, y)
            curve.attach(self.plot)
            ticks = list(set.union(set(ticks), set(x)))
        
        if len(ticks) > 0 and self.isFirstRedraw:
            #init zoom base
            self.zoomer.setZoomBase()
            
        if len(ticks) > 0 and (self.isFirstRedraw or recalculateBonds):
            ticks.sort()
            #update axes
            div = QwtScaleDiv(ticks[0], ticks[len(ticks)-1], [], [], ticks)
            #according to http://pyqwt.sourceforge.net/doc5/reference.html#PyQt4.Qwt5.QwtScaleDiv
            #this line should be (note ticks position, maybe a bug in api?:
            #div = QwtScaleDiv(ticks[0], ticks[len(ticks)-1], ticks, [], [])
            baseTime = QDateTime(self.mainWidget.timeMin)
            draw = TimeScaleDraw(baseTime)
            self.plot.setAxisScaleDraw(QwtPlot.xBottom, draw)
            self.plot.setAxisScaleDiv(QwtPlot.xBottom, div)
            
            self.plot.setAxisScale(QwtPlot.yLeft, self.mainWidget.valueMin, self.mainWidget.valueMax)
            
            # reinitialize the scale
            self.picker.updateBaseTime(baseTime)
            #update zoom base
            tl = QPointF(min(ticks), self.mainWidget.valueMax)
            br = QPointF(max(ticks), self.mainWidget.valueMin)
            self.zoomer.setZoomBase(QRectF(tl, br)) 
        #finally, refresh the plot
        self.isFirstRedraw = False
        self.plot.replot()
        
        
    def reset(self):
        self.plot.detachItems()
        self.plot.replot()
        
    def help(self):
         QMessageBox.about(self, 'TimePlot Help', "This plot shows the temporal evoution of multiple variable.\
         \nClick on the magnify glass to enable the click&drag zoomer.\
         \nRight click zooms out again" )
    
    def zoomEnabled(self, on):
        self.zoomer.setEnabled(on)
        
        if on:
            self.picker.setRubberBand(QwtPicker.NoRubberBand)
        else:
            self.zoomer.zoom(0)
            self.picker.setRubberBand(QwtPicker.CrossRubberBand)
            
    @pyqtSlot(float)
    def on_pointSize_valueChanged(self, value):
        self.mainWidget.redraw(False)
    
    @pyqtSlot(float)
    def on_lineWidth_valueChanged(self, value):
        self.mainWidget.redraw(False)
    
    @pyqtSlot(float)
    def on_dashOffset_valueChanged(self, value):
        self.mainWidget.redraw(False)
        
    @pyqtSlot(str)
    def on_dashPattern_textChanged(self, value):
        self.mainWidget.redraw(False)
        
class TimeScaleDraw(QwtScaleDraw):
    def __init__(self, baseTime):
        QwtScaleDraw.__init__(self)
        #QTime baseTime
        print "here"
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
    
    
    
    
    
