# -*- coding: utf-8 -*-
"""PowPySol-GUI - A graphical user interface for the PowPySol-tool:
                  Mayavi integration

    Copyright (C) 2014  Jan M. Simons <marten@xtal.rwth-aachen.de>

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

# First, and before importing any Enthought packages, set the ETS_TOOLKIT
# environment variable to qt4, to tell Traits that we will use Qt.
import os
os.environ['ETS_TOOLKIT'] = 'qt4'

# To be able to use PySide or PyQt4 and not run in conflicts with traits,
# we need to import QtGui and QtCore from pyface.qt
from pyface.qt import QtGui, QtCore
# Alternatively, you can bypass this line, but you need to make sure that
# the following lines are executed before the import of PyQT:
#   import sip
#   sip.setapi('QString', 2)

from traits.api import HasTraits, Instance, on_trait_change, Int, Dict
from traitsui.api import View, Item
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor
import numpy as np

################################################################################
#The actual visualization
class TestVisualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.

        # We can do normal mlab calls on the embedded scene.
        self.scene.mlab.test_points3d()

    # the layout of the dialog screated
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True # We need this to resize with the parent widget
               )

class StructureVisualization(HasTraits):
    scene = Instance(MlabSceneModel, ())
    xtal_structure = None
    _box_corners = [(0.0,  0.0, 0.0),
                    (1.0,  0.0, 0.0),
                    (0.0,  1.0, 0.0),
                    (0.0,  0.0, 1.0),
                    (1.0,  1.0, 0.0),
                    (0.0,  1.0, 1.0),
                    (1.0,  0.0, 1.0),
                    (1.0,  1.0, 1.0)]
    _box_edges = [ (0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6),
                   (7, 4), (7, 5), (7, 6), (2, 4), (3, 5), (1, 6) ]
    _showLabels = False
    _suffixLabels = False

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.

        # We can do normal mlab calls on the embedded scene.
        # Visualize the data ###################################################
        #self.scene.mlab.figure(1, bgcolor=(0, 0, 0))
        if self.xtal_structure is None:
            self.prepare_structure()

        self.scene.mlab.clf(figure=self.scene.mayavi_scene)

        # draw the atoms of the structure
        pts = self.scene.mlab.points3d(self._x, self._y, self._z,
                                       1.5*self._scalars.max() - self._scalars,
                                       scale_factor=0.015,
                                       resolution=30,
                                       figure=self.scene.mayavi_scene)
        # draw the unit cell of the structure
        bx = self.scene.mlab.points3d(self._xb, self._yb, self._zb,
                                      1.5*self._scalarsb.max() - self._scalarsb,
                                      scale_factor=0.015,
                                      resolution=30,
                                      figure=self.scene.mayavi_scene)
        bx.mlab_source.dataset.lines = np.array(self._box_edges)
        # Use a tube fiter to plot tubes on the link
        tube = self.scene.mlab.pipeline.tube(bx, tube_radius=0.05)
        self.scene.mlab.pipeline.surface(tube, color=(0.9, 0.9, 0.9),
                                         figure=self.scene.mayavi_scene)
        if self._showLabels:
            for (label, x, y, z, s) in zip(tuple(self._labels),
                                        tuple(self._x),
                                        tuple(self._y),
                                        tuple(self._z),
                                        tuple(self._scalars)):
                self.scene.mlab.text3d(x+0.3, y+0.3, z+0.3, label,
                                      line_width=0.13,
                                      scale=0.4,
                                      figure=self.scene.mayavi_scene)
        # vv doesn't work vv
        #self.scene.show_axes = True
        #self.scene.parallel_projection = True

    def load_structure(self, xtal_structure, show_labels=False, suffixes=False):
        self._showLabels = show_labels
        self._suffixLabels = suffixes
        self.prepare_structure(xtal_structure)
        self.update_plot()

    def prepare_structure(self, xtal_structure=None):
        # this function extracts the atom data to plot from a
        # xray structure
        if xtal_structure is None:
            from cctbx.development import random_structure
            self.xtal_structure = random_structure.xray_structure(
                    elements            = ['C', 'Si', 'O', 'Ti', 'Cl'],
                    space_group_symbol  = "P 2/c",
                    unit_cell           = [10.0, 10.0, 6.0, 90.0, 110.0, 90.0],
                    min_distance        = 1.0,
                    use_u_aniso         = False,
                    u_iso               = 0.1)
        else:
            self.xtal_structure = xtal_structure
        uc = self.xtal_structure.unit_cell()
        # expand to P1 to generate all symmetrically equivalent atoms
        self.xtal_structure = self.xtal_structure.expand_to_p1(
            append_number_to_labels=self._suffixLabels,
            sites_mod_positive=True)
        # turn the structure into 3D positions
        x       = list()
        y       = list()
        z       = list()
        scalars = list()
        labels  = list()
        scatterers = list(self.xtal_structure.scatterers())
        for sc in scatterers:
            scalars.append(sc.electron_count())
            labels.append(sc.label)
            site_cart = uc.orthogonalize(sc.site)
            x.append(float(site_cart[0]))
            y.append(float(site_cart[1]))
            z.append(float(site_cart[2]))
        # convert the corners of the unit cell into 3D positons
        xb       = list()
        yb       = list()
        zb       = list()
        scalarsb = list()
        for xyz in self._box_corners:
            scalarsb.append(0)
            site_cart = uc.orthogonalize(xyz)
            xb.append(float(site_cart[0]))
            yb.append(float(site_cart[1]))
            zb.append(float(site_cart[2]))
        # mayavi expects numpy arrays
        self._x         = np.array(x)
        self._y         = np.array(y)
        self._z         = np.array(z)
        self._scalars   = np.array(scalars)
        self._labels    = labels
        self._xb        = np.array(xb)
        self._yb        = np.array(yb)
        self._zb        = np.array(zb)
        self._scalarsb  = np.array(scalarsb)

    # the layout of the dialog screated
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True # We need this to resize with the parent widget
               )


class RPlotVisualization(HasTraits):
    scene = Instance(MlabSceneModel, ())
    x = None
    y = None
    z = None
    TEN_BY_TEN = np.mgrid[0.00:1.00:0.1, 0.00:1.00:0.1]
    ELEVEN_BY_ELEVEN = np.mgrid[0.00:1.10:0.1, 0.00:1.10:0.1]
    HUNDRED_BY_HUNDRED = np.mgrid[0.00:1.00:0.01, 0.00:1.00:0.01]
    HUNDREDONE_BY_HUNDREDONE = np.mgrid[0.00:1.01:0.01, 0.00:1.01:0.01]

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.

        # We can do normal mlab calls on the embedded scene.
        # Visualize the data
        #self.scene.mlab.figure(1, bgcolor=(0, 0, 0))
        if self.x is None:
            self.prepare_data()

        self.scene.mlab.clf(figure=self.scene.mayavi_scene)
        #fig = self.scene.mlab.figure()
        # mark position of global minimum
        xm, ym, zm, index_min = self.get_min()
        #print(index_min)
        #print(xm,ym,zm)
        glyph = self.scene.mlab.points3d(xm, ym, zm, color=(0.36, 0.12, 0.01),
                                         scale_mode="none", scale_factor=0.04,
                                         figure=self.scene.mayavi_scene)

        # plot surface
        s = self.scene.mlab.surf(self.x, self.y, self.z,
                                 figure=self.scene.mayavi_scene)
        s.enable_contours = True
        s.contour.number_of_contours = 10
        s.contour.filled_contours = True

        # add axes (x and y seem to be swapped in plots)
        ax = self.scene.mlab.axes(extent=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
                                  nb_labels=11,
                                  figure=self.scene.mayavi_scene)
        ax.axes.label_format = '%-#6.1f'
        self.scene.mlab.ylabel(str(self._names[0]).replace("_",".",1))
        self.scene.mlab.xlabel(str(self._names[1]).replace("_",".",1))
        self.scene.mlab.zlabel(self._names[2])


        scene = s.parent.parent.scene
        #scene.background = (1.0, 1.0, 1.0)
        slut = s.parent.scalar_lut_manager
        slut.lut_mode = 'gist_rainbow'
        slut.scalar_bar.position2 = np.array([ 0.17,  0.8 ])
        slut.scalar_bar.position = np.array([ 0.85,  0.115 ])
        slut.data_name = u'R1'
        slut.use_default_range = False
        slut.data_range = np.array([ 0.0,  1.0])
        slut.number_of_labels = 11
        slut.label_text_property.bold = False
        slut.scalar_bar.label_format = '%-#6.1f'
        slut.show_scalar_bar = True

        if self._topview:
            ax.axes.y_axis_visibility = False
            slut.show_legend = False
            scene.z_plus_view()
            scene.parallel_projection = True
            scene.camera.position = [0.69278935562056577,
                                     0.44454621842443059,
                                     3.8460652149512318]
            scene.camera.focal_point = [0.69278935562056577,
                                        0.44454621842443059,
                                        0.5]
            scene.camera.view_angle = 30.0
            scene.camera.view_up = [0.0, 1.0, 0.0]
            scene.camera.clipping_range = [2.3176045628017192,
                                           4.6487561931755002]
            clm_text = "CLM:\n\n{0}={1}\n\n{2}={3}\n\n{4}={5:.2f}".format(
                                                            self._names[0],ym,
                                                            self._names[1],xm,
                                                            self._names[2],zm)
            text = self.scene.mlab.text3d(1.1,1.0, 0.3,
                                clm_text,
                                line_width=0.13, scale=0.1,
                                figure=self.scene.mayavi_scene)
        else:
            slut.show_legend = True
            scene.parallel_projection = False
            scene.camera.position = [-1.6410025575697766,
                                     -1.7944249231504954,
                                     1.6262220378106524]
            scene.camera.focal_point = [0.51745554413721884,
                                        0.44298005338227575,
                                        0.36249261549848044]
            scene.camera.view_angle = 30.0
            scene.camera.view_up = [0.20508491340556723,
                                    0.32382999987701611,
                                    0.92362021928554749]
            scene.camera.clipping_range = [1.6195411896711804,
                                           5.493155101016737]
            scene.camera.compute_view_plane_normal()

    def get_min(self):
        index_min = self.z.argmin()
        return ( self.x.flat[index_min],
                     self.y.flat[index_min],
                     self.z.flat[index_min],
                     index_min )


    def prepare_data(self, R=None, axis_labels=None, topview=True):
        self._topview = topview
        if R is None:            #dummy data
            R = np.linspace(0.00, 1.00, num=100*100, endpoint=True)
        if axis_labels is None:
            self._names = ("x", "y", "R1")
        else:
            self._names = axis_labels
        if len(R.shape) == 1:
            size = len(R)
        else:
            size = R.shape[0] * R.shape[1]
        if size == 100:          # 10 * 10
            self.x, self.y = self.TEN_BY_TEN
            shape = (10, 10)
        elif size == 121:        # 11 * 11
            self.x, self.y = self.ELEVEN_BY_ELEVEN
            shape = (11, 11)
        elif size == 10000:      #100 * 100
            self.x, self.y = self.HUNDRED_BY_HUNDRED
            shape = (100, 100)
        elif size == 10201:      #101 * 101
            self.x, self.y = self.HUNDREDONE_BY_HUNDREDONE
            shape = (101, 101)
        else:
            raise(ArgumentError("R has invalid dimensions."))
        self.z = R
        self.z.shape = shape

    def load_data(self, Rvalues, axis_labels=None, topview=False):
        self.prepare_data(Rvalues, axis_labels=axis_labels, topview=topview)
        self.update_plot()

    # the layout of the dialog screated
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                resizable=True # We need this to resize with the parent widget
               )

################################################################################
# The QWidget containing the visualization, this is pure PyQt4 code.
class MayaviQWidget(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    layout = QtGui.QVBoxLayout(self)
    layout.setMargin(0)
    layout.setSpacing(0)
    #self.visualization = TestVisualization()
    self.visualization = TestVisualization()

    # If you want to debug, beware that you need to remove the Qt
    # input hook.
    #QtCore.pyqtRemoveInputHook()
    #import pdb ; pdb.set_trace()
    #QtCore.pyqtRestoreInputHook()

    # The edit_traits call will generate the widget to embed.
    self.ui = self.visualization.edit_traits(parent=self, kind='subpanel').control
    layout.addWidget(self.ui)
    self.ui.setParent(self)

class MayaviQStructureWidget(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    layout = QtGui.QVBoxLayout(self)
    layout.setMargin(0)
    layout.setSpacing(0)
    #self.visualization = TestVisualization()
    self.visualization = StructureVisualization()

    # If you want to debug, beware that you need to remove the Qt
    # input hook.
    #QtCore.pyqtRemoveInputHook()
    #import pdb ; pdb.set_trace()
    #QtCore.pyqtRestoreInputHook()

    # The edit_traits call will generate the widget to embed.
    self.ui = self.visualization.edit_traits(parent=self, kind='subpanel').control
    layout.addWidget(self.ui)
    self.ui.setParent(self)

class MayaviQRPlotWidget(QtGui.QWidget):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    layout = QtGui.QVBoxLayout(self)
    layout.setMargin(0)
    layout.setSpacing(0)
    #self.visualization = TestVisualization()
    self.visualization = RPlotVisualization()

    # If you want to debug, beware that you need to remove the Qt
    # input hook.
    #QtCore.pyqtRemoveInputHook()
    #import pdb ; pdb.set_trace()
    #QtCore.pyqtRestoreInputHook()

    # The edit_traits call will generate the widget to embed.
    self.ui = self.visualization.edit_traits(parent=self, kind='subpanel').control
    layout.addWidget(self.ui)
    self.ui.setParent(self)
