# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_timeplotwidget.ui'
#
# Created: Thu Mar 17 16:44:54 2011
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
        self.zoomButton = QtGui.QPushButton(TimePlotWidget)
        self.zoomButton.setGeometry(QtCore.QRect(340, 10, 38, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomButton.sizePolicy().hasHeightForWidth())
        self.zoomButton.setSizePolicy(sizePolicy)
        self.zoomButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/multiview/images/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomButton.setIcon(icon)
        self.zoomButton.setIconSize(QtCore.QSize(16, 16))
        self.zoomButton.setCheckable(True)
        self.zoomButton.setObjectName("zoomButton")

        self.retranslateUi(TimePlotWidget)
        QtCore.QMetaObject.connectSlotsByName(TimePlotWidget)

    def retranslateUi(self, TimePlotWidget):
        TimePlotWidget.setWindowTitle(QtGui.QApplication.translate("TimePlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomButton.setToolTip(QtGui.QApplication.translate("TimePlotWidget", "Zoom in/out the plot", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
import resources_rc
