# -*- coding: utf-8 -*-
"""Xtal-xplore-R - A graphical tool for exploring the residual function
                   involved in crystal structure determination:
                        MainWindow

    Copyright (C) 2014-2015  Jan M. Simons <marten@xtal.rwth-aachen.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import division
from __future__ import absolute_import

import copy

#try:
#    from PySide import QtGui, QtCore  # noqa
#    backend = 'pyside'
#except ImportError:
from qtpy import QtGui, QtWidgets, QtCore  # noqa
#backend = 'pyqt4'
import visvis as vv
# Create a visvis app instance, which wraps a qt4 application object.
# This needs to be done *before* instantiating the main window.
app = vv.use()


from . import XtalxplorerMainWindowUI
import numpy as np
from cctbx.array_family import flex


class EmittingStream(QtCore.QObject):
    """A simple class to make a nice log handler."""

    def __init__(self):
        super(EmittingStream, self).__init__()
        self.textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        """Write text to stream."""
        self.textWritten.emit(str(text))

class XtalxplorerMainWindow(QtWidgets.QMainWindow,
                            XtalxplorerMainWindowUI.Ui_XtalxplorerMainWindow):
    """The second parent must be 'Ui_<obj. name of main widget class>'.
    If confusing, simply open up __UI.py and get the class name used."""

    def __init__(self, parent=None, **kwargs):
        super(XtalxplorerMainWindow, self).__init__(parent=parent, **kwargs)
        # This is because Python does not automatically
        # call the parent's constructor.
        self.setupUi(self)
        # Pass this "self" for building widgets and
        # keeping a reference.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Xtal-xplore-R - V {0}") #.format(program.versions))
        self._structure1 = None
        self._structure2 = None
        self._lastparams = [-0.1, -0.1, -0.1, -0.1]
        self._Rvalues = None
        self._update_structure_timer = QtCore.QTimer()
        self._update_structure_timer.setInterval(150)
        self._update_structure_timer.timeout.connect(self.update_params)
        self._update_rplots_timer = QtCore.QTimer()
        self._update_rplots_timer.setInterval(1000)
        self._update_rplots_timer.timeout.connect(self.update_rplots)
        # redirect stdout and stderr to log window
        #sys.stdout = EmittingStream(textWritten=self.handle_stdout)
        #sys.stderr = EmittingStream(textWritten=self.handle_stdout)
        self.dss_x.setText("X")
        self.dss_y.setText("Y")
        self.dss_z.setText("Z")
        self.dss_uiso.setText("u_iso")
        self.dss_uiso.setMinimum(0.0001)
        self.dss_uiso.setMaximum(0.3000)
        self.dss_dmin.setText("d_min")
        self.dss_dmin.setMinimum(0.5)
        self.dss_dmin.setMaximum(2.5)

    def main(self):
        """Main entry point"""
        self.show()
        self.textEdit_log.setPlainText()

    def center(self):
        """Center the form window on the screen."""
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)

    def invalidate_cached_params(self):
        self._lastparams = [-0.1, -0.1, -0.1, -0.1]

    def _enable_buttons(self):
        """Make buttons clickable."""
        for buttons in [ self.hLayout_buttonsStructure,
                         self.hLayout_buttonsGrid]:
            for w_id in range(buttons.count()):
                widget = buttons.itemAt(w_id).widget()
                if widget is not None: # the spacer is represented by 'None'
                    widget.setEnabled(True)

    def _enable_sliders(self, enable=True):
        for slider in [self.dss_x, self.dss_y, self.dss_z, self.dss_uiso]:
            slider.setEnabled(enable)

    def _copy_structure(self):
        if self.radioButton_structure1.isChecked():
            self._structure2 = self._structure1.customized_copy()
            self.radioButton_structure2.setEnabled(True)
        else:
            self._structure1 = self._structure2.customized_copy()

    def selected_structure(self):
        if self.radioButton_structure1.isChecked():
            return self._structure1
        else:
            return self._structure2

    def set_selected_structure(self, structure):
        if self.radioButton_structure1.isChecked():
            self._structure1 = structure
        else:
            self._structure2 = structure
        self._load_structure()

    def browse_structure(self):
        """Present a file selection dialog to browse for a job file."""
        # Lets get a user-provided file to open
        # using PyQt's QFileDialog class.
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
                        self,
                        "Open crystal structure",
                        QtCore.QDir.homePath(),
                        "crystal structure file (*.cif)",
                        options=QtWidgets.QFileDialog.DontUseNativeDialog
                    )
        # Don't attempt to open if open dialog was cancelled away.
        if filename:
            # load the job file
            self.open_structure(str(filename))

    def open_structure(self, filename):
        """Open the specified job file."""
        if 1:
            print(filename)
        try:
            from iotbx.cif import reader, CifParserError
            cif = reader(file_path=filename)
            structures = cif.build_crystal_structures()
            self.set_selected_structure(next(iter(structures.items()))[1])
        except CifParserError as e:
            print("could not load file!")
            print(e.text)
        self._load_structure()

    def _load_structure(self):
        self.invalidate_cached_params()
        self._update_list_from_structure()
        self._update_structure_view()
        self.lstWidget_atoms.setCurrentRow(0)


    def randomise_structure(self):
        from cctbx.development import random_structure
        base_structure = self.selected_structure()
        atoms = []
        for scat in base_structure.scatterers():
            atoms.append(str(scat.element_symbol()))
        new_xtal_structure = random_structure.xray_structure(
            elements            = atoms,
            space_group_info    = base_structure.space_group_info(),
            unit_cell           = base_structure.unit_cell(),
            min_distance        = 1.0,
            use_u_aniso         = False,
            u_iso               = 0.1)
        self.set_selected_structure(new_xtal_structure)


    def _update_structure_view(self):
        self.Q_structure_view.visualization.load_structure(
            self.selected_structure(),
            show_labels=self.checkBox_showLabels.isChecked(),
            suffixes=self.checkBox_suffix.isChecked())

    def _update_list_from_structure(self):
        self.lstWidget_atoms.clear()
        self.comboBox_x.clear()
        self.comboBox_y.clear()
        for scatterer in self.selected_structure().scatterers():
            #print(scatterer)
            self.lstWidget_atoms.addItem(scatterer.label)
            self.comboBox_x.addItem(scatterer.label+"_x")
            self.comboBox_x.addItem(scatterer.label+"_y")
            self.comboBox_x.addItem(scatterer.label+"_z")
            self.comboBox_y.addItem(scatterer.label+"_x")
            self.comboBox_y.addItem(scatterer.label+"_y")
            self.comboBox_y.addItem(scatterer.label+"_z")
        self.comboBox_x.setCurrentIndex(0)
        self.comboBox_y.setCurrentIndex(1)

    def load_atom_params(self, index):
        if not self.dss_x.isEnabled(): self._enable_sliders()
        atom = self.selected_structure().scatterers()[index]
        self.dss_x.setValue(atom.site[0])
        self.dss_y.setValue(atom.site[1])
        self.dss_z.setValue(atom.site[2])
        self.dss_uiso.setValue(atom.u_iso)
        self._lastparams = list(atom.site)
        self._lastparams.append(atom.u_iso)

    def update_params(self):
        index = self.lstWidget_atoms.currentRow()
        if index < 0: return # index out of range
        params = [self.dss_x.value(),
                  self.dss_y.value(),
                  self.dss_z.value(),
                  self.dss_uiso.value()]
        if params == self._lastparams: return # only update if something changed
        scatterer = self.selected_structure().scatterers()[index]
        scatterer.site = tuple(params[:3])
        scatterer.u_iso = params[3]
        self._lastparams = params
        #print(self._lastparams)
        self._update_structure_view()

    def update_rplots(self):
        # deactivte timer, so it doesn't fire while we're still working
        timeractive = self._update_rplots_timer.isActive()
        self._update_rplots_timer.stop()
        self._Rvalues = self.do_slice(dx=self.comboBox_x.currentIndex(),
                                      dy=self.comboBox_y.currentIndex(),
                                      d_min=self.dss_dmin.value(),
                                      fine_grid=self.checkBox_fine.isChecked())
        #print("R:", self._Rvalues)
        labels = (self.comboBox_x.currentText(),
                  self.comboBox_y.currentText(),
                  "r1")
        self.Q_3D_view.visualization.load_data(self._Rvalues,
                                                axis_labels=labels,
                                                topview=False)
        self.Q_top_view.visualization.load_data(self._Rvalues,
                                                 axis_labels=labels,
                                                 topview=True)
        # turn timer back on if it was running before
        if timeractive and self.checkBox_autoupdateRPlots.isChecked():
            self._update_rplots_timer.start()


    def do_slice(self, d_min=1.5, dx=0, dy=1, fine_grid=False):
        """Calculate a 2d slice of the target function.
        dx and dy specify which dimensions to use for x and y axis.
        z is the R1 value.
        """
        if fine_grid:
            step_sequence = map(lambda x: round(x * 0.01, 2), range(0,101))
        else:
            step_sequence = map(lambda x: round(x * 0.1, 1), range(0,11))

        structure = copy.deepcopy(self._structure1)
        if self._structure2 is None:
            f_obs = structure.structure_factors(d_min=d_min).f_calc()
        else:
            f_obs = self._structure2.structure_factors(d_min=d_min).f_calc()

        # convert sites from flex.vec3_double into list of lists
        sites0 = list(list(x) for x in flex.to_list(structure.sites_frac()))

        # iterate grid
        all_r1 = np.zeros(len(step_sequence)**2)
        i = 0
        for y in step_sequence:
            self.progressBar.setValue(int(y*len(step_sequence)))
            QtWidgets.QApplication.processEvents()
            QtWidgets.QApplication.processEvents()
            for x in step_sequence:
                newsites = copy.deepcopy(sites0)
                newsites[dx//3][dx%3] = x
                newsites[dy//3][dy%3] = y
                structure.set_sites_frac(flex.vec3_double(newsites))
                f_calc = structure.structure_factors(d_min=d_min).f_calc()
                r1 = f_obs.r1_factor(other=f_calc, assume_index_matching=True)
                all_r1[i] = r1
                i += 1
        self.progressBar.setValue(100)
        return np.asarray(all_r1)

    def _update_status(self):
        """Show current job status in treeWidget"""
        self.treeWidget_xtalData.clear()
        self.treeWidget_xtalData.setHeaderLabels(["Item","Value"])
        for key in self._job.results.scalars:
            #print("{0}: {1}".format(key, self._job.options[key]))
            QtWidgets.QTreeWidgetItem(self.treeWidget_xtalData,
                                  [key, str(self._job.results[key])])
        for section in self._job.results.sections:
            qsection = QtWidgets.QTreeWidgetItem(self.treeWidget_xtalData,
                                  [ section, "" ])
            for key in self._job.results[section].scalars:
                #print("{0}-->{1}: {2}".format(section, key,
                #                              self._job.results[section][key]))
                QtWidgets.QTreeWidgetItem(qsection,
                                      [key,
                                       str(self._job.results[section][key])])
        self.treeWidget_Status.expandAll()

    def handle_autoupdate_structure(self, enable):
        if enable:
            self._update_structure_timer.start()
        else:
            self._update_structure_timer.stop()

    def handle_autoupdate_r_plots(self, enable):
        if enable:
            self._update_rplots_timer.start()
        else:
            self._update_rplots_timer.stop()

    def file_quit(self):
        """Exit programme"""
        self.close()

    def close_event(self, event):
        """Ask for confirmation before closing."""
        reply = QtWidgets.QMessageBox.question(self,
                                    'Exit?', "Are you sure to quit?",
                                    QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.fileQuit()
            #event.accept()
        else:
            event.ignore()

    def about(self):
        """Show some info about this programme."""
        QtWidgets.QMessageBox.about(self, "About",
"""This programme is the graphical tool for crystal structure exploration.

It is written in PyQT4 and uses Mayavi for visualisation.
"""
)

    def handle_stdout(self, text):
        """Append text to the log window.
        The colour will be picked automatically if certain keywords are found in
        the message."""
        self.textEdit_log.moveCursor(QtGui.QTextCursor.End)
        if "-->ERROR:" in text:
            self.textEdit_log.setTextColor(QtGui.QColor('red'))
        elif "-->DEBUG:" in text:
            self.textEdit_log.setTextColor(QtGui.QColor('grey'))
        elif "-->WARNING:" in text:
            self.textEdit_log.setTextColor(QtGui.QColor('brown'))
        elif "-->CRITICAL:" in text:
            self.textEdit_log.setTextColor(QtGui.QColor('violet'))
        else:
            self.textEdit_log.setTextColor(QtGui.QColor('black'))
        self.textEdit_log.insertPlainText(text)
