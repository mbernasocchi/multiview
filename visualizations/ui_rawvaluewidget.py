# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_rawvaluewidget.ui'
#
# Created: Fri Apr  1 15:00:22 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RawValueWidget(object):
    def setupUi(self, RawValueWidget):
        RawValueWidget.setObjectName("RawValueWidget")
        RawValueWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(RawValueWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.warningDisplay = QtGui.QLabel(RawValueWidget)
        self.warningDisplay.setText("")
        self.warningDisplay.setObjectName("warningDisplay")
        self.verticalLayout.addWidget(self.warningDisplay)
        self.display = QtGui.QTextBrowser(RawValueWidget)
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)

        self.retranslateUi(RawValueWidget)
        QtCore.QMetaObject.connectSlotsByName(RawValueWidget)

    def retranslateUi(self, RawValueWidget):
        RawValueWidget.setWindowTitle(QtGui.QApplication.translate("RawValueWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

