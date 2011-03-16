# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_timeplotwidget.ui'
#
# Created: Wed Mar 16 10:56:25 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TimePlotWidget(object):
    def setupUi(self, TimePlotWidget):
        TimePlotWidget.setObjectName("TimePlotWidget")
        TimePlotWidget.resize(386, 308)
        self.qwtPlot = QwtPlot(TimePlotWidget)
        self.qwtPlot.setGeometry(QtCore.QRect(0, 40, 341, 231))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwtPlot.sizePolicy().hasHeightForWidth())
        self.qwtPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")

        self.retranslateUi(TimePlotWidget)
        QtCore.QMetaObject.connectSlotsByName(TimePlotWidget)

    def retranslateUi(self, TimePlotWidget):
        TimePlotWidget.setWindowTitle(QtGui.QApplication.translate("TimePlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
