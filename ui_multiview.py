# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multiview.ui'
#
# Created: Mon Apr 11 11:36:05 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MultiView(object):
    def setupUi(self, MultiView):
        MultiView.setObjectName("MultiView")
        MultiView.setWindowModality(QtCore.Qt.NonModal)
        MultiView.resize(857, 488)
        self.verticalLayout_2 = QtGui.QVBoxLayout(MultiView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main = QtGui.QHBoxLayout()
        self.main.setObjectName("main")
        self.controls = QtGui.QVBoxLayout()
        self.controls.setObjectName("controls")
        self.title = QtGui.QLabel(MultiView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.controls.addWidget(self.title)
        self.availableVariablesContainer = QtGui.QScrollArea(MultiView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableVariablesContainer.sizePolicy().hasHeightForWidth())
        self.availableVariablesContainer.setSizePolicy(sizePolicy)
        self.availableVariablesContainer.setWidgetResizable(True)
        self.availableVariablesContainer.setObjectName("availableVariablesContainer")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.availableVariablesContainer)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 251, 191))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.availableVariables = QtGui.QVBoxLayout()
        self.availableVariables.setObjectName("availableVariables")
        self.verticalLayout_5.addLayout(self.availableVariables)
        self.availableVariablesContainer.setWidget(self.scrollAreaWidgetContents_2)
        self.controls.addWidget(self.availableVariablesContainer)
        self.settings = QtGui.QHBoxLayout()
        self.settings.setObjectName("settings")
        self.tracking = QtGui.QGroupBox(MultiView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracking.sizePolicy().hasHeightForWidth())
        self.tracking.setSizePolicy(sizePolicy)
        self.tracking.setObjectName("tracking")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tracking)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.trackMouseMove = QtGui.QRadioButton(self.tracking)
        self.trackMouseMove.setObjectName("trackMouseMove")
        self.verticalLayout_3.addWidget(self.trackMouseMove)
        self.trackRightClick = QtGui.QRadioButton(self.tracking)
        self.trackRightClick.setObjectName("trackRightClick")
        self.verticalLayout_3.addWidget(self.trackRightClick)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.settings.addWidget(self.tracking)
        self.buttons = QtGui.QVBoxLayout()
        self.buttons.setObjectName("buttons")
        self.manualRefreshButton = QtGui.QPushButton(MultiView)
        self.manualRefreshButton.setObjectName("manualRefreshButton")
        self.buttons.addWidget(self.manualRefreshButton)
        self.loadDataButton = QtGui.QPushButton(MultiView)
        self.loadDataButton.setObjectName("loadDataButton")
        self.buttons.addWidget(self.loadDataButton)
        self.helpButton = QtGui.QPushButton(MultiView)
        self.helpButton.setObjectName("helpButton")
        self.buttons.addWidget(self.helpButton)
        self.vizHelpButton = QtGui.QPushButton(MultiView)
        self.vizHelpButton.setObjectName("vizHelpButton")
        self.buttons.addWidget(self.vizHelpButton)
        self.printButton = QtGui.QPushButton(MultiView)
        self.printButton.setObjectName("printButton")
        self.buttons.addWidget(self.printButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.buttons.addItem(spacerItem1)
        self.settings.addLayout(self.buttons)
        self.controls.addLayout(self.settings)
        self.main.addLayout(self.controls)
        self.visualizations = QtGui.QTabWidget(MultiView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualizations.sizePolicy().hasHeightForWidth())
        self.visualizations.setSizePolicy(sizePolicy)
        self.visualizations.setObjectName("visualizations")
        self.main.addWidget(self.visualizations)
        self.verticalLayout_2.addLayout(self.main)
        self.bottom = QtGui.QHBoxLayout()
        self.bottom.setObjectName("bottom")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottom.addItem(spacerItem2)
        self.aboutButton = QtGui.QPushButton(MultiView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        self.aboutButton.setObjectName("aboutButton")
        self.bottom.addWidget(self.aboutButton)
        self.closeButton = QtGui.QPushButton(MultiView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setObjectName("closeButton")
        self.bottom.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.bottom)

        self.retranslateUi(MultiView)
        self.visualizations.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MultiView)

    def retranslateUi(self, MultiView):
        MultiView.setWindowTitle(QtGui.QApplication.translate("MultiView", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("MultiView", "Enable Variables:", None, QtGui.QApplication.UnicodeUTF8))
        self.tracking.setTitle(QtGui.QApplication.translate("MultiView", "Tracking:", None, QtGui.QApplication.UnicodeUTF8))
        self.trackMouseMove.setText(QtGui.QApplication.translate("MultiView", "Mouse Move", None, QtGui.QApplication.UnicodeUTF8))
        self.trackRightClick.setText(QtGui.QApplication.translate("MultiView", "Right click", None, QtGui.QApplication.UnicodeUTF8))
        self.manualRefreshButton.setText(QtGui.QApplication.translate("MultiView", "Refresh List", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataButton.setText(QtGui.QApplication.translate("MultiView", "Load Data ...", None, QtGui.QApplication.UnicodeUTF8))
        self.helpButton.setText(QtGui.QApplication.translate("MultiView", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.vizHelpButton.setText(QtGui.QApplication.translate("MultiView", "Viz Help", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setText(QtGui.QApplication.translate("MultiView", "Print Viz", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutButton.setText(QtGui.QApplication.translate("MultiView", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("MultiView", "Close", None, QtGui.QApplication.UnicodeUTF8))

