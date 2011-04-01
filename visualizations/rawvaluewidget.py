"""
/***************************************************************************
 RawValueWidget - shows the raw values passed to the redraw method
                                 A QGIS plugin
                             -------------------
        begin                : 2011-01-02
        copyright            : (C) 2011 by marco
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_rawvaluewidget import Ui_RawValueWidget

# This is an example visualisation class for multi view.
# Use it as your working base
# All the methods present here have to exist to make the class working
class RawValueWidget(QWidget):
    def __init__(self, mainWidget, main):
        QWidget.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_RawValueWidget()
        self.ui.setupUi(self)
        #main plugin file
        self.main = main
        #multiview widget
        self.mainWidget = mainWidget
        #this is the label that shows the warnings
        self.warningDisplay = self.ui.warningDisplay
    
    def name(self):
        '''Returns the name of the visualization'''
        return "Raw Values"
    
    def redraw(self, values, recalculateBonds=True):
        '''Redraws the visualization'''
        self.ui.display.setText(str(values))
        
    def reset(self):
        '''Reset the visualization'''
        self.ui.display.setText("")
    
    def help(self):
        '''Help about the visualization'''
        self.ui.display.setText("This widget shows the raw values coming from the data in the form:\
        \n{'variableID': [(timeInSec, value), (timeInSec, value), ...], ...}")
