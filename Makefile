#/***************************************************************************
# MultiView
# 
# Allows analysis of multi temporal and multivariate datasets
#                             -------------------
#        begin                : 2011-02-19
#        copyright            : (C) 2011 by http://bernawebdesign.ch
#        email                : marco@bernawebdesign.ch
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

UI_PATH=.
UI_SOURCES=$(shell find $(UI_PATH) -name '*.ui')
UI_FILES=$(patsubst $(UI_PATH)/%.ui, $(UI_PATH)/%.py, $(UI_SOURCES))

LANG_PATH=i18n
LANG_SOURCES=$(wildcard $(LANG_PATH)/*.ts)
LANG_FILES=$(patsubst $(LANG_PATH)/%.ts, $(LANG_PATH)/%.qm, $(LANG_SOURCES))

RES_PATH=.
RES_SOURCES=$(shell find $(UI_PATH) -name '*.qrc')
RES_FILES=$(patsubst $(RES_PATH)/%.qrc, $(RES_PATH)/%_rc.py, $(RES_SOURCES))

ALL_FILES= ${RES_FILES} ${UI_FILES} ${LANG_FILES}

all: $(ALL_FILES)

ui: $(UI_FILES) 

lang: $(LANG_FILES)

res: $(RES_FILES)

$(UI_FILES): $(UI_PATH)/%.py: $(UI_PATH)/%.ui
	pyuic4 -o $@ $<
	sed -i 's|from qwt_plot import QwtPlot|from PyQt4.Qwt5 import QwtPlot|g' $@
	sed -i 's|from QGLViewer.qglviewer import QGLViewer|from PyQGLViewer import *|g' $@

$(LANG_FILES): $(LANG_PATH)/%.qm: $(LANG_PATH)/%.ts
	lrelease $< 

$(RES_FILES): $(RES_PATH)/%_rc.py: $(RES_PATH)/%.qrc
	pyrcc4 -o $@ $<


clean:
	rm -f $(ALL_FILES)

package:
	cd .. && rm -f GdalTools.zip && zip -r GdalTools.zip GdalTools -x \*.svn* -x \*.pyc -x \*~ -x \*entries\* -x \*.git\*