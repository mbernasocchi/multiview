# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_plotwidget.ui'
#
# Created: Tue Mar  8 23:41:10 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PlotWidget(object):
    def setupUi(self, PlotWidget):
        PlotWidget.setObjectName("PlotWidget")
        PlotWidget.resize(381, 267)
        self.qwtPlot = QwtPlot(PlotWidget)
        self.qwtPlot.setGeometry(QtCore.QRect(0, 40, 361, 200))
        self.qwtPlot.setObjectName("qwtPlot")

        self.retranslateUi(PlotWidget)
        QtCore.QMetaObject.connectSlotsByName(PlotWidget)

    def retranslateUi(self, PlotWidget):
        PlotWidget.setWindowTitle(QtGui.QApplication.translate("PlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
