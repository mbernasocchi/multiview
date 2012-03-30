# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stepdurationdialog.ui'
#
# Created: Fri Mar 30 19:02:42 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StepDurationDialog(object):
    def setupUi(self, StepDurationDialog):
        StepDurationDialog.setObjectName(_fromUtf8("StepDurationDialog"))
        StepDurationDialog.setWindowModality(QtCore.Qt.WindowModal)
        StepDurationDialog.resize(382, 162)
        StepDurationDialog.setWindowTitle(QtGui.QApplication.translate("StepDurationDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayoutWidget = QtGui.QWidget(StepDurationDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 371, 141))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("StepDurationDialog", "Enter the duration (in seconds) of each steps of: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.stepDurationText = QtGui.QLabel(self.verticalLayoutWidget)
        self.stepDurationText.setText(_fromUtf8(""))
        self.stepDurationText.setObjectName(_fromUtf8("stepDurationText"))
        self.verticalLayout.addWidget(self.stepDurationText)
        self.input = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input.setObjectName(_fromUtf8("input"))
        self.verticalLayout.addWidget(self.input)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StepDurationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), StepDurationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), StepDurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StepDurationDialog)

    def retranslateUi(self, StepDurationDialog):
        pass

