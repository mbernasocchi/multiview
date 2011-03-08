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

# create the dialog for zoom to point
class RawValueWidget(QWidget):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_RawValueWidget()
        self.ui.setupUi(self)
    
    def name(self):
        return "Raw Values"
    
    def redraw(self, values):
        self.ui.display.setText(str(values))
        
    def reset(self):
        self.ui.display.setText("")
