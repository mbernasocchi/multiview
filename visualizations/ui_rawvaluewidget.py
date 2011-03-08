# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_rawvaluewidget.ui'
#
# Created: Tue Mar  8 22:29:08 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RawValueWidget(object):
    def setupUi(self, RawValueWidget):
        RawValueWidget.setObjectName("RawValueWidget")
        RawValueWidget.resize(400, 300)
        self.display = QtGui.QTextBrowser(RawValueWidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 391, 291))
        self.display.setObjectName("display")

        self.retranslateUi(RawValueWidget)
        QtCore.QMetaObject.connectSlotsByName(RawValueWidget)

    def retranslateUi(self, RawValueWidget):
        RawValueWidget.setWindowTitle(QtGui.QApplication.translate("RawValueWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

