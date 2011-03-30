# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_temporalrasterloaderdialog.ui'
#
# Created: Wed Mar 30 21:06:07 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TemporalRasterLoaderDialog(object):
    def setupUi(self, TemporalRasterLoaderDialog):
        TemporalRasterLoaderDialog.setObjectName("TemporalRasterLoaderDialog")
        TemporalRasterLoaderDialog.resize(688, 295)
        self.verticalLayout_2 = QtGui.QVBoxLayout(TemporalRasterLoaderDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.results = QtGui.QTextBrowser(TemporalRasterLoaderDialog)
        self.results.setObjectName("results")
        self.verticalLayout.addWidget(self.results)
        self.progressBar = QtGui.QProgressBar(TemporalRasterLoaderDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(TemporalRasterLoaderDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.temporalRegEx = QtGui.QLineEdit(TemporalRasterLoaderDialog)
        self.temporalRegEx.setObjectName("temporalRegEx")
        self.horizontalLayout_3.addWidget(self.temporalRegEx)
        self.label_2 = QtGui.QLabel(TemporalRasterLoaderDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.intervalRegEx = QtGui.QLineEdit(TemporalRasterLoaderDialog)
        self.intervalRegEx.setObjectName("intervalRegEx")
        self.horizontalLayout_3.addWidget(self.intervalRegEx)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.loadDataButton = QtGui.QPushButton(TemporalRasterLoaderDialog)
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
        self.label_3 = QtGui.QLabel(TemporalRasterLoaderDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.startDatetime = QtGui.QDateTimeEdit(TemporalRasterLoaderDialog)
        self.startDatetime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 12, 31), QtCore.QTime(0, 0, 0)))
        self.startDatetime.setCalendarPopup(True)
        self.startDatetime.setObjectName("startDatetime")
        self.horizontalLayout_4.addWidget(self.startDatetime)
        self.dataVisible = QtGui.QCheckBox(TemporalRasterLoaderDialog)
        self.dataVisible.setObjectName("dataVisible")
        self.horizontalLayout_4.addWidget(self.dataVisible)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.saveLogButton = QtGui.QPushButton(TemporalRasterLoaderDialog)
        self.saveLogButton.setEnabled(False)
        self.saveLogButton.setObjectName("saveLogButton")
        self.horizontalLayout_4.addWidget(self.saveLogButton)
        self.closeButton = QtGui.QPushButton(TemporalRasterLoaderDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_4.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(TemporalRasterLoaderDialog)
        QtCore.QMetaObject.connectSlotsByName(TemporalRasterLoaderDialog)

    def retranslateUi(self, TemporalRasterLoaderDialog):
        TemporalRasterLoaderDialog.setWindowTitle(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "TemporalRasterLoader", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "RegularExpression for the temporal describing part of the filenames", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temporal RE<img src=\":/plugins/multiview/images/info.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.temporalRegEx.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "N\\d\\d\\d\\d", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "RegularExpression for the interval describing part of the filenames", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Interval RE<img src=\":/plugins/multiview/images/info.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.intervalRegEx.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "S\\d\\d\\d\\d", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataButton.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Choose and Load", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Date to which the first step will be set to", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Start date<img src=\":/plugins/multiview/images/info.png\" />", None, QtGui.QApplication.UnicodeUTF8))
        self.startDatetime.setDisplayFormat(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.dataVisible.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Show all data after load (slow)", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLogButton.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Save Log", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("TemporalRasterLoaderDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
