# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_helixwidget.ui'
#
# Created: Tue Mar  8 23:39:13 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HelixWidget(object):
    def setupUi(self, HelixWidget):
        HelixWidget.setObjectName("HelixWidget")
        HelixWidget.resize(425, 267)
        self.calendarWidget = QtGui.QCalendarWidget(HelixWidget)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 40, 304, 179))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(HelixWidget)
        QtCore.QMetaObject.connectSlotsByName(HelixWidget)

    def retranslateUi(self, HelixWidget):
        HelixWidget.setWindowTitle(QtGui.QApplication.translate("HelixWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

