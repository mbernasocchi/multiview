# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multiview.ui'
#
# Created: Wed Mar  9 01:23:51 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MultiView(object):
    def setupUi(self, MultiView):
        MultiView.setObjectName("MultiView")
        MultiView.setWindowModality(QtCore.Qt.NonModal)
        MultiView.resize(794, 391)
        self.layoutWidget = QtGui.QWidget(MultiView)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtGui.QVBoxLayout()
        self.left.setObjectName("left")
        self.title = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setObjectName("title")
        self.left.addWidget(self.title)
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 388, 124))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.availableVariables = QtGui.QVBoxLayout()
        self.availableVariables.setObjectName("availableVariables")
        self.verticalLayout_5.addLayout(self.availableVariables)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.left.addWidget(self.scrollArea)
        self.availableVariablesUpdateButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableVariablesUpdateButton.sizePolicy().hasHeightForWidth())
        self.availableVariablesUpdateButton.setSizePolicy(sizePolicy)
        self.availableVariablesUpdateButton.setObjectName("availableVariablesUpdateButton")
        self.left.addWidget(self.availableVariablesUpdateButton)
        self.loadDataButton = QtGui.QPushButton(self.layoutWidget)
        self.loadDataButton.setObjectName("loadDataButton")
        self.left.addWidget(self.loadDataButton)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 131, 75))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.trackMouseMove = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.trackMouseMove.setObjectName("trackMouseMove")
        self.verticalLayout.addWidget(self.trackMouseMove)
        self.trackRightClick = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.trackRightClick.setObjectName("trackRightClick")
        self.verticalLayout.addWidget(self.trackRightClick)
        self.left.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.left)
        self.visualizations = QtGui.QTabWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualizations.sizePolicy().hasHeightForWidth())
        self.visualizations.setSizePolicy(sizePolicy)
        self.visualizations.setObjectName("visualizations")
        self.horizontalLayout.addWidget(self.visualizations)
        self.horizontalLayoutWidget = QtGui.QWidget(MultiView)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 340, 791, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.warningDisplay = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warningDisplay.sizePolicy().hasHeightForWidth())
        self.warningDisplay.setSizePolicy(sizePolicy)
        self.warningDisplay.setText("")
        self.warningDisplay.setObjectName("warningDisplay")
        self.horizontalLayout_3.addWidget(self.warningDisplay)
        self.closeButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)

        self.retranslateUi(MultiView)
        self.visualizations.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MultiView)

    def retranslateUi(self, MultiView):
        MultiView.setWindowTitle(QtGui.QApplication.translate("MultiView", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("MultiView", "Enable Variables:", None, QtGui.QApplication.UnicodeUTF8))
        self.availableVariablesUpdateButton.setText(QtGui.QApplication.translate("MultiView", "Update List", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataButton.setText(QtGui.QApplication.translate("MultiView", "Load Data ...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MultiView", "Tracking:", None, QtGui.QApplication.UnicodeUTF8))
        self.trackMouseMove.setText(QtGui.QApplication.translate("MultiView", "Mouse Move", None, QtGui.QApplication.UnicodeUTF8))
        self.trackRightClick.setText(QtGui.QApplication.translate("MultiView", "Right click", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MultiView", "Close", None, QtGui.QApplication.UnicodeUTF8))

