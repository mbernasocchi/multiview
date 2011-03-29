# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizations/ui_helixwidget.ui'
#
# Created: Tue Mar 29 02:02:04 2011
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
        self.unitPerCycle = QtGui.QComboBox(HelixWidget)
        self.unitPerCycle.setObjectName("unitPerCycle")
        self.unitPerCycle.addItem("")
        self.unitPerCycle.addItem("")
        self.horizontalLayout.addWidget(self.unitPerCycle)
        self.label = QtGui.QLabel(HelixWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sizePerCycle = QtGui.QSpinBox(HelixWidget)
        self.sizePerCycle.setAccelerated(True)
        self.sizePerCycle.setMaximum(99999)
        self.sizePerCycle.setObjectName("sizePerCycle")
        self.horizontalLayout.addWidget(self.sizePerCycle)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.minSaturation = QtGui.QDoubleSpinBox(HelixWidget)
        self.minSaturation.setAccelerated(True)
        self.minSaturation.setMaximum(1.0)
        self.minSaturation.setSingleStep(0.01)
        self.minSaturation.setProperty("value", 0.15)
        self.minSaturation.setObjectName("minSaturation")
        self.gridLayout.addWidget(self.minSaturation, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(HelixWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ribbonWidth = QtGui.QDoubleSpinBox(HelixWidget)
        self.ribbonWidth.setAccelerated(True)
        self.ribbonWidth.setMinimum(0.01)
        self.ribbonWidth.setMaximum(1.0)
        self.ribbonWidth.setSingleStep(0.01)
        self.ribbonWidth.setProperty("value", 0.8)
        self.ribbonWidth.setObjectName("ribbonWidth")
        self.gridLayout.addWidget(self.ribbonWidth, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(HelixWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(HelixWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.precision = QtGui.QSpinBox(HelixWidget)
        self.precision.setAccelerated(True)
        self.precision.setMaximum(50)
        self.precision.setObjectName("precision")
        self.gridLayout.addWidget(self.precision, 1, 3, 1, 1)
        self.textOffset = QtGui.QDoubleSpinBox(HelixWidget)
        self.textOffset.setAccelerated(True)
        self.textOffset.setMaximum(10.0)
        self.textOffset.setSingleStep(0.01)
        self.textOffset.setProperty("value", 0.3)
        self.textOffset.setObjectName("textOffset")
        self.gridLayout.addWidget(self.textOffset, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(HelixWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(HelixWidget)
        QtCore.QMetaObject.connectSlotsByName(HelixWidget)
        HelixWidget.setTabOrder(self.unitPerCycle, self.sizePerCycle)
        HelixWidget.setTabOrder(self.sizePerCycle, self.minSaturation)
        HelixWidget.setTabOrder(self.minSaturation, self.ribbonWidth)
        HelixWidget.setTabOrder(self.ribbonWidth, self.textOffset)
        HelixWidget.setTabOrder(self.textOffset, self.precision)

    def retranslateUi(self, HelixWidget):
        HelixWidget.setWindowTitle(QtGui.QApplication.translate("HelixWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        HelixWidget.setToolTip(QtGui.QApplication.translate("HelixWidget", "Pres H for help", None, QtGui.QApplication.UnicodeUTF8))
        self.unitPerCycle.setItemText(0, QtGui.QApplication.translate("HelixWidget", "Day(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.unitPerCycle.setItemText(1, QtGui.QApplication.translate("HelixWidget", "Year(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HelixWidget", "per cycle:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HelixWidget", "Min value color saturation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("HelixWidget", "Ribbon width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("HelixWidget", "Helix roundness:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("HelixWidget", "Text offset:", None, QtGui.QApplication.UnicodeUTF8))

