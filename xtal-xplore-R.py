# -*- coding: utf-8 -*-
"""xtal-xplore-R - A graphical tool for crystal structure exploration

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
from __future__ import division, print_function, absolute_import

__author__ = "Jan M. Simons <marten@xtal.rwth-aachen.de>"
__status__ = "alpha"
__version__ = "0.1.0"
__date__ = "13 October 2014"

if __name__ == "__main__":
    import sys
    from argparse import ArgumentParser
    version_string = "%(prog)s {0:s} ({1:s})".format(__version__,
                                                     __status__)
    parser = ArgumentParser(description=
                        'A graphical tool for crystal structure exploration')
    parser.add_argument('-V', '--version',
                        action='version',
                        version=version_string)
    parser.add_argument('STRUCTUREFILE',
                        help="read crystal data from STRUCTUREFILE",
                        nargs="?", default="")
    cmd_args = parser.parse_args()

    #try:
    #    from PySide import QtGui, QtCore  # noqa
    #    backend = 'pyside'
    #except ImportError:
    from qtpy import QtGui, QtCore  # noqa
    #backend = 'pyqt4'
    import visvis as vv
    # Create a visvis app instance, which wraps a qt4 application object.
    # This needs to be done *before* instantiating the main window.
    app = vv.use()
    app.Create()

    from gui.xtalxplorermainwindow import XtalxplorerMainWindow
    mainwindow = XtalxplorerMainWindow()
    mainwindow.center()
    mainwindow.statusBar().showMessage('Ready')
    mainwindow.show()
    if cmd_args.STRUCTUREFILE != "":
        mainwindow.open_structure(cmd_args.STRUCTUREFILE)

    # Start the main event loop.
    app.Run()

    #sys.exit(app.exec_())
