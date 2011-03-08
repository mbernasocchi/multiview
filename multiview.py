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

class MultiView:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.mapCanvas = iface.mapCanvas()
        self.mainWindow = iface.mainWindow()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/multiview/icon.png"), \
            "MultiView", self.mainWindow)
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&MultiView", self.action)
        
        #clear plugin projects settings when a new project is loaded
        QObject.connect(self.iface, SIGNAL("projectRead()"), self.removeProjectSettings )
        QObject.connect(self.iface, SIGNAL("newProjectCreated()"), self.removeProjectSettings )
        self.removeProjectSettings()
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&MultiView",self.action)
        self.iface.removeToolBarIcon(self.action)
        
        #TODO, is it necessary to disconnect signals
        #QObject.disconnect(self.iface, SIGNAL("projectRead()"), self.removeProjectSettings )
        #QObject.disconnect(self.iface, SIGNAL("newProjectCreated()"), self.removeProjectSettings )
        
        try:
            self.multiviewwidget.temporalRasterLoader.close()
            self.multiviewwidget.close()
        except:
            pass

    # run method that performs all the real work
    def run(self):
        # create the widget
        self.multiviewwidget = MultiViewWidget(self.iface, self)
        # show the widget
        self.multiviewwidget.show()
    
    def removeProjectSettings(self):
        try:
            del self.activatedVariables
        except:
            pass

