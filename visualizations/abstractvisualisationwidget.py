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

from PyQt4.QtGui import *
# This is an example visualisation class for multi view.
# Use it as your working base
# All the methods present here have to exist to make the class working
class AbstractVisualisationWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
    def name(self):
        '''Returns the name of the visualization'''
        raise NotImplementedError
        
    def canvasWidget(self):
        raise NotImplementedError
    
    def redraw(self, values, recalculateBonds=True):
        '''Redraws the visualization'''
        raise NotImplementedError
        
    def reset(self):
        '''Reset the visualization'''
        raise NotImplementedError
    
    def help(self):
        '''Help about the visualization'''
        raise NotImplementedError
        
        
