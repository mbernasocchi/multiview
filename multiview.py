"""
/***************************************************************************
 MultiView
                                 A QGIS plugin
 This plugin allows analysis of multi temporal and multivariate datasets
                              -------------------
        begin                : 2010-12-19
        copyright            : (C) 2011 by bernawebdesign.ch
        email                : marco@bernawebdesign.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the widget
from multiviewwidget import MultiViewWidget
from temporalrasterloaderdialog import TemporalRasterLoaderDialog

class MultiView:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.mapCanvas = iface.mapCanvas()
        self.mainWindow = iface.mainWindow()

    def initGui(self):
        # Create action that will start plugin
        self.runAction = QAction(QIcon(":/plugins/multiview/icon.png"), \
            "MultiView", self.mainWindow)
        QObject.connect(self.runAction, SIGNAL("triggered()"), self.run)
        
        self.loadDataAction = QAction(QIcon(":/plugins/multiview/icon.png"), \
            "MultiView Data Loader", self.mainWindow)
        QObject.connect(self.loadDataAction, SIGNAL("triggered()"), self.loadData)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.runAction)
        self.iface.addPluginToMenu("&Analyses", self.runAction)
        self.iface.addToolBarIcon(self.loadDataAction)
        self.iface.addPluginToMenu("&Analyses", self.loadDataAction)
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Analyses", self.runAction)
        self.iface.removeToolBarIcon(self.runAction)
        self.iface.removePluginMenu("&Analyses", self.loadDataAction)
        self.iface.removeToolBarIcon(self.loadDataAction)
        
        try:
            self.multiviewwidget.temporalRasterLoader.close()
        except:
            pass
        try:
            self.temporalRasterLoader.close()
        except:
            pass
        try:
            self.multiviewwidget.close()
        except:
            pass
        
    # run method that performs all the real work
    def run(self):
        # create the widget
        self.multiviewwidget = MultiViewWidget(self.iface, self)
        # show the widget
        self.multiviewwidget.show()
    
    def loadData(self):
        self.temporalRasterLoader = TemporalRasterLoaderDialog(self.iface)
        # show the dialog
        self.temporalRasterLoader.show()
