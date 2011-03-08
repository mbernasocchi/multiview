# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_temporalrasterloaderdialog.ui'
#
# Created: Tue Mar  8 22:28:20 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TemporalRasterLoaderDialog(object):
    def setupUi(self, TemporalRasterLoaderDialog):
        TemporalRasterLoaderDialog.setObjectName("TemporalRasterLoaderDialog")
        TemporalRasterLoaderDialog.resize(673, 295)
        self.verticalLayoutWidget = QtGui.QWidget(TemporalRasterLoaderDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 671, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.results = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.results.setObjectName("results")
        self.verticalLayout.addWidget(self.results)
        self.progressBar = QtGui.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.temporalRegEx = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.temporalRegEx.setObjectName("temporalRegEx")
        self.horizontalLayout_3.addWidget(self.temporalRegEx)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.intervalRegEx = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.intervalRegEx.setObjectName("intervalRegEx")
        self.horizontalLayout_3.addWidget(self.intervalRegEx)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.loadDataButton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadDataButton.sizePolicy().hasHeightForWidth())
        self.loadDataButton.setSizePolicy(sizePolicy)
        self.loadDataButton.setObjectName("loadDataButton")
        self.horizontalLayout_3.addWidget(self.loadDataButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_4.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(TemporalRasterLoaderDialog)
        QtCore.QMetaObject.connectSlotsByName(TemporalRasterLoaderDialog)

    def retranslateUi(self, TemporalRasterLoaderDialog):
        TemporalRasterLoaderDialog.setWindowTitle(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "TemporalRasterLoader", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Temporal RE:", None, QtGui.QApplication.UnicodeUTF8))
        self.temporalRegEx.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "N\\d\\d\\d\\d", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Interval RE:", None, QtGui.QApplication.UnicodeUTF8))
        self.intervalRegEx.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "S\\d\\d\\d\\d", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataButton.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Choose and Load", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

