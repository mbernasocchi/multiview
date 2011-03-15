"""
/***************************************************************************
 DurationDialog
                                 A QGIS plugin
 DurationDialog
                             -------------------
        begin                : 2011-03-13
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

from PyQt4 import QtCore, QtGui
from ui_stepdurationdialog import Ui_StepDurationDialog
# create the dialog for zoom to point
class StepDurationDialog(QtGui.QDialog):
    def __init__(self, stepDurationText):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_StepDurationDialog()
        self.ui.setupUi(self)
        self.ui.stepDurationText.setText(stepDurationText)
        self.setWindowTitle(stepDurationText)

        #allow only INT bigger than 1
        validator = QtGui.QIntValidator(self)
        validator.setBottom(1)  
        self.ui.input.setValidator(validator);
