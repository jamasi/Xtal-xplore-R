# -*- coding: utf-8 -*-
"""DoubleSpinSlider - a custom widget combining a slider with a spinbox

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
from __future__ import division, print_function, absolute_import

from decimal import Decimal
from qtpy import QtGui, QtWidgets, QtCore
from qtpy.QtCore import Slot


class DoubleSpinSlider(QtWidgets.QWidget):
    """This is a QWidget containing a QSlider and a QDoubleSpinBox"""
    def __init__(self, parent=None, width=50, height=100, dpi=100, **kwarg):
        super(DoubleSpinSlider, self).__init__(parent, **kwarg)
        #QtGui.QWidget.__init__(self, parent)
        self._vLayout = QtWidgets.QVBoxLayout()

        self._label = QtWidgets.QLabel(parent)
        self._label.setAlignment(QtCore.Qt.AlignCenter)
        self._vLayout.addWidget(self._label)

        self._dSBox = QtWidgets.QDoubleSpinBox(parent)
        self._dSBox.setWrapping(True)
        self._dSBox.setDecimals(4)
        self._dSBox.setMaximum(1.00000000)
        self._dSBox.setSingleStep(0.1000000000)
        self._vLayout.addWidget(self._dSBox)

        self._hLayout = QtWidgets.QHBoxLayout()
        self._vSlider = QtWidgets.QSlider(parent)
        self._vSlider.setMinimum(0)
        self._vSlider.setMaximum(10000)
        self._vSlider.setPageStep(1000)
        self._vSlider.setOrientation(QtCore.Qt.Vertical)
        self._vSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self._vSlider.setTickInterval(0)
        self._hLayout.addWidget(self._vSlider)
        self._vLayout.addLayout(self._hLayout)
        self.setLayout(self._vLayout)
        self.setParent(parent)

        # map functions
        self.setText = self._label.setText
        self.text = self._label.text
        self.setValue = self._dSBox.setValue
        self.value = self._dSBox.value
        self._vSlider.valueChanged.connect(self.ChangeSpinBox)
        self._dSBox.valueChanged.connect(self.ChangeSlider)

    def _multiplier(self):
        return 10.000000 ** self._dSBox.decimals()

    @Slot(int)
    def ChangeSpinBox(self, slidervalue):
        #print("sv: {}".format(slidervalue))
        newvalue = round(slidervalue / (self._multiplier()),4)
        #print("nv: {}".format(newvalue))
        if newvalue != self._dSBox.value():
            self._dSBox.setValue(newvalue)

    @Slot('double')
    def ChangeSlider(self, spinboxvalue):
        newvalue = spinboxvalue * self._multiplier()
        #print("sb: {sb}  mult: {mult}  prod: {prod}".format(
        #                    sb=spinboxvalue,
        #                    mult=int(10.00000000 ** self._dSBox.decimals()),
        #                    prod=newvalue))
        self._vSlider.setValue(newvalue)

    @Slot('double')
    def setMaximum(self, maximum):
        self._dSBox.setMaximum(maximum)
        self._vSlider.setMaximum(maximum * self._multiplier())

    @Slot('double')
    def setMinimum(self, minimum):
        self._dSBox.setMinimum(minimum)
        self._vSlider.setMinimum(minimum * self._multiplier())
