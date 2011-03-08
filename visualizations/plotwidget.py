"""
/***************************************************************************
 PlotWidget - shows the values as xy plots
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

hasqwt = True
try:
    from PyQt4.Qwt5 import *
except:
    hasqwt = False
    


# create the dialog for zoom to point
class PlotWidget(QWidget):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
    
    def name(self):
        return "Plot"
    
    def redraw(self, values):
        print str(values)
        
    def reset(self):
        print "reset"
        
