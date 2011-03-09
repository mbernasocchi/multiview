# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_pcpwidget.ui'
#
# Created: Wed Mar  9 23:40:18 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PCPWidget(object):
    def setupUi(self, PCPWidget):
        PCPWidget.setObjectName("PCPWidget")
        PCPWidget.resize(386, 308)
        self.qwtPlot = QwtPlot(PCPWidget)
        self.qwtPlot.setGeometry(QtCore.QRect(0, 40, 341, 231))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwtPlot.sizePolicy().hasHeightForWidth())
        self.qwtPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")

        self.retranslateUi(PCPWidget)
        QtCore.QMetaObject.connectSlotsByName(PCPWidget)

    def retranslateUi(self, PCPWidget):
        PCPWidget.setWindowTitle(QtGui.QApplication.translate("PCPWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
