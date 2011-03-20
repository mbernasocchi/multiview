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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Multitemporal and Multivariate data visualisation"
def description():
    return "This plugin allows analysis of multi temporal and multivariate datasets"
def version():
    return "Version 0.2"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.6"
    #TODO change to 1.7
def classFactory(iface):
    # load MultiView class from file MultiView
    from multiview import MultiView
    return MultiView(iface)
