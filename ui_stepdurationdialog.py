# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stepdurationdialog.ui'
#
# Created: Tue Mar 15 20:20:07 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_StepDurationDialog(object):
    def setupUi(self, StepDurationDialog):
        StepDurationDialog.setObjectName("StepDurationDialog")
        StepDurationDialog.setWindowModality(QtCore.Qt.WindowModal)
        StepDurationDialog.resize(382, 162)
        self.verticalLayoutWidget = QtGui.QWidget(StepDurationDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 371, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.stepDurationText = QtGui.QLabel(self.verticalLayoutWidget)
        self.stepDurationText.setText("")
        self.stepDurationText.setObjectName("stepDurationText")
        self.verticalLayout.addWidget(self.stepDurationText)
        self.input = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StepDurationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), StepDurationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), StepDurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StepDurationDialog)

    def retranslateUi(self, StepDurationDialog):
        StepDurationDialog.setWindowTitle(QtGui.QApplication.translate("StepDurationDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("StepDurationDialog", "Enter the duration (in seconds) of each steps of: ", None, QtGui.QApplication.UnicodeUTF8))

