"""
/***************************************************************************
 MultiView
                                 A QGIS plugin
 This plugin allows analysis of multi temporal and multivariate datasets
                              -------------------
        begin                : 2011-02-19
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

#
# map tool that allows panning and emits the coords of a mouse click
#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


class PanEmitMapTool(QgsMapToolPan):
    def __init__(self, canvas):
        QgsMapToolPan.__init__(self, canvas) 
        self.cursor = QCursor(Qt.ArrowCursor)

    def canvasPressEvent(self, e):
        point = self.toMapCoordinates(e.pos())
        self.emit(SIGNAL("canvasClicked"), point, e.button())
