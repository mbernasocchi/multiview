# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_timeplotwidget.ui'
#
# Created: Fri Apr  1 15:00:22 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TimePlotWidget(object):
    def setupUi(self, TimePlotWidget):
        TimePlotWidget.setObjectName("TimePlotWidget")
        TimePlotWidget.resize(474, 459)
        self.verticalLayout = QtGui.QVBoxLayout(TimePlotWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.warningDisplay = QtGui.QLabel(TimePlotWidget)
        self.warningDisplay.setText("")
        self.warningDisplay.setObjectName("warningDisplay")
        self.verticalLayout.addWidget(self.warningDisplay)
        self.qwtPlot = QwtPlot(TimePlotWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwtPlot.sizePolicy().hasHeightForWidth())
        self.qwtPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")
        self.verticalLayout.addWidget(self.qwtPlot)
        self.zoomButton = QtGui.QPushButton(TimePlotWidget)
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
        self.verticalLayout.addWidget(self.zoomButton)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(TimePlotWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtGui.QLabel(TimePlotWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(TimePlotWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(TimePlotWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.pointSize = QtGui.QDoubleSpinBox(TimePlotWidget)
        self.pointSize.setProperty("value", 7.0)
        self.pointSize.setObjectName("pointSize")
        self.gridLayout.addWidget(self.pointSize, 1, 1, 1, 1)
        self.lineWidth = QtGui.QDoubleSpinBox(TimePlotWidget)
        self.lineWidth.setProperty("value", 2.0)
        self.lineWidth.setObjectName("lineWidth")
        self.gridLayout.addWidget(self.lineWidth, 1, 2, 1, 1)
        self.dashOffset = QtGui.QDoubleSpinBox(TimePlotWidget)
        self.dashOffset.setProperty("value", 1.0)
        self.dashOffset.setObjectName("dashOffset")
        self.gridLayout.addWidget(self.dashOffset, 1, 3, 1, 1)
        self.dashPattern = QtGui.QLineEdit(TimePlotWidget)
        self.dashPattern.setObjectName("dashPattern")
        self.gridLayout.addWidget(self.dashPattern, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(TimePlotWidget)
        QtCore.QMetaObject.connectSlotsByName(TimePlotWidget)

    def retranslateUi(self, TimePlotWidget):
        TimePlotWidget.setWindowTitle(QtGui.QApplication.translate("TimePlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomButton.setToolTip(QtGui.QApplication.translate("TimePlotWidget", "Zoom in/out the plot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TimePlotWidget", "Point size", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TimePlotWidget", "Line width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("TimePlotWidget", "Offset for the start of the dash pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TimePlotWidget", "Dash offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("TimePlotWidget", "use an array in this format: [dash, space, dash, space,...]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TimePlotWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dash pattern <img src=\":/plugins/multiview/images/info.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.dashOffset.setToolTip(QtGui.QApplication.translate("TimePlotWidget", "Offset for the start of the dash pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.dashPattern.setToolTip(QtGui.QApplication.translate("TimePlotWidget", "use an array in this format: [dash, space, dash, space,...]", None, QtGui.QApplication.UnicodeUTF8))
        self.dashPattern.setText(QtGui.QApplication.translate("TimePlotWidget", "[1,1]", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
import resources_rc
