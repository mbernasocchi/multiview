# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_helixwidget.ui'
#
# Created: Sat Mar 26 18:43:08 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HelixWidget(object):
    def setupUi(self, HelixWidget):
        HelixWidget.setObjectName("HelixWidget")
        HelixWidget.resize(528, 325)
        self.verticalLayout = QtGui.QVBoxLayout(HelixWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sizePerCycle = QtGui.QSpinBox(HelixWidget)
        self.sizePerCycle.setAccelerated(True)
        self.sizePerCycle.setMaximum(99999)
        self.sizePerCycle.setObjectName("sizePerCycle")
        self.horizontalLayout.addWidget(self.sizePerCycle)
        self.unitPerCycle = QtGui.QComboBox(HelixWidget)
        self.unitPerCycle.setObjectName("unitPerCycle")
        self.unitPerCycle.addItem("")
        self.unitPerCycle.addItem("")
        self.horizontalLayout.addWidget(self.unitPerCycle)
        self.label = QtGui.QLabel(HelixWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(HelixWidget)
        QtCore.QMetaObject.connectSlotsByName(HelixWidget)

    def retranslateUi(self, HelixWidget):
        HelixWidget.setWindowTitle(QtGui.QApplication.translate("HelixWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        HelixWidget.setToolTip(QtGui.QApplication.translate("HelixWidget", "Pres H for help", None, QtGui.QApplication.UnicodeUTF8))
        self.unitPerCycle.setItemText(0, QtGui.QApplication.translate("HelixWidget", "Day(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.unitPerCycle.setItemText(1, QtGui.QApplication.translate("HelixWidget", "Year(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HelixWidget", "per cycle", None, QtGui.QApplication.UnicodeUTF8))

