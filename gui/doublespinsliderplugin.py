# -*- coding: utf-8 -*-
"""DoubleSpinSliderPlugin - a custom widget combining a slider with a spinbox

    Copyright (C) 2014    Jan M. Simons <marten@xtal.rwth-aachen.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.    If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4 import QtGui, QtDesigner
from powpysol.gui.doublespinslider import DoubleSpinSlider

class DoubleSpinSliderPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    _logo_16x16_xpm = ""

    def __init__(self, parent = None):
        QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return DoubleSpinSlider(parent)

    def name(self):
        return "DoubleSpinSlider"

    def group(self):
        return "Input Widgets"

    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def domXml(self):
        return (
               '<widget class="DoubleSpinSlider" name=\"doubleSpinSlider\">\n'
               " <property name=\"toolTip\" >\n"
               "  <string>combined slider and spinbox</string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string>This widget creates a linked slider and spinbox.</string>\n"
               " </property>\n"
               " <property name=\"label\" >\n"
               "  <string>X</string>\n"
               " </property>\n"
               "</widget>\n"
               )
    
    def includeFile(self):
        return "powpysol.gui.doublespinslider"