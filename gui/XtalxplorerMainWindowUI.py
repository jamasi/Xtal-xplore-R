# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XtalxplorerMainWindowUI.ui'
#
# Created: Mon Feb  2 20:27:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_XtalxplorerMainWindow(object):
    def setupUi(self, XtalxplorerMainWindow):
        XtalxplorerMainWindow.setObjectName(_fromUtf8("XtalxplorerMainWindow"))
        XtalxplorerMainWindow.resize(1024, 740)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(XtalxplorerMainWindow.sizePolicy().hasHeightForWidth())
        XtalxplorerMainWindow.setSizePolicy(sizePolicy)
        XtalxplorerMainWindow.setMinimumSize(QtCore.QSize(1024, 740))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/PowPySol.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        XtalxplorerMainWindow.setWindowIcon(icon)
        self.container = QtGui.QWidget(XtalxplorerMainWindow)
        self.container.setMinimumSize(QtCore.QSize(1024, 700))
        self.container.setObjectName(_fromUtf8("container"))
        self.gridLayout = QtGui.QGridLayout(self.container)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hLayout_main = QtGui.QHBoxLayout()
        self.hLayout_main.setObjectName(_fromUtf8("hLayout_main"))
        self.vLayout_tools = QtGui.QVBoxLayout()
        self.vLayout_tools.setObjectName(_fromUtf8("vLayout_tools"))
        self.toolButton_open = QtGui.QToolButton(self.container)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Document-open.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_open.setIcon(icon1)
        self.toolButton_open.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_open.setObjectName(_fromUtf8("toolButton_open"))
        self.vLayout_tools.addWidget(self.toolButton_open)
        self.toolButton_copyStructure = QtGui.QToolButton(self.container)
        self.toolButton_copyStructure.setObjectName(_fromUtf8("toolButton_copyStructure"))
        self.vLayout_tools.addWidget(self.toolButton_copyStructure)
        self.progressBar = QtGui.QProgressBar(self.container)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.vLayout_tools.addWidget(self.progressBar)
        self.hLayout_main.addLayout(self.vLayout_tools)
        self.vLayout_main = QtGui.QVBoxLayout()
        self.vLayout_main.setObjectName(_fromUtf8("vLayout_main"))
        self.hLayout_top = QtGui.QHBoxLayout()
        self.hLayout_top.setObjectName(_fromUtf8("hLayout_top"))
        self.tabWidget = QtGui.QTabWidget(self.container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabParams = QtGui.QWidget()
        self.tabParams.setObjectName(_fromUtf8("tabParams"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tabParams)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 471, 331))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_params = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_params.setMargin(0)
        self.gridLayout_params.setObjectName(_fromUtf8("gridLayout_params"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lstWidget_atoms = QtGui.QListWidget(self.gridLayoutWidget_2)
        self.lstWidget_atoms.setMinimumSize(QtCore.QSize(20, 0))
        self.lstWidget_atoms.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lstWidget_atoms.setAlternatingRowColors(True)
        self.lstWidget_atoms.setObjectName(_fromUtf8("lstWidget_atoms"))
        self.horizontalLayout.addWidget(self.lstWidget_atoms)
        self.dss_x = DoubleSpinSlider(self.gridLayoutWidget_2)
        self.dss_x.setEnabled(False)
        self.dss_x.setObjectName(_fromUtf8("dss_x"))
        self.horizontalLayout.addWidget(self.dss_x)
        self.dss_y = DoubleSpinSlider(self.gridLayoutWidget_2)
        self.dss_y.setEnabled(False)
        self.dss_y.setObjectName(_fromUtf8("dss_y"))
        self.horizontalLayout.addWidget(self.dss_y)
        self.dss_z = DoubleSpinSlider(self.gridLayoutWidget_2)
        self.dss_z.setEnabled(False)
        self.dss_z.setObjectName(_fromUtf8("dss_z"))
        self.horizontalLayout.addWidget(self.dss_z)
        self.dss_uiso = DoubleSpinSlider(self.gridLayoutWidget_2)
        self.dss_uiso.setEnabled(False)
        self.dss_uiso.setObjectName(_fromUtf8("dss_uiso"))
        self.horizontalLayout.addWidget(self.dss_uiso)
        self.vLayout_paramButtons = QtGui.QVBoxLayout()
        self.vLayout_paramButtons.setObjectName(_fromUtf8("vLayout_paramButtons"))
        self.groupBox_structureSelect = QtGui.QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_structureSelect.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox_structureSelect.setObjectName(_fromUtf8("groupBox_structureSelect"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox_structureSelect)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 119, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vLayout_structureSelect = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_structureSelect.setMargin(0)
        self.vLayout_structureSelect.setObjectName(_fromUtf8("vLayout_structureSelect"))
        self.radioButton_structure1 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_structure1.setChecked(True)
        self.radioButton_structure1.setObjectName(_fromUtf8("radioButton_structure1"))
        self.vLayout_structureSelect.addWidget(self.radioButton_structure1)
        self.radioButton_structure2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_structure2.setEnabled(False)
        self.radioButton_structure2.setObjectName(_fromUtf8("radioButton_structure2"))
        self.vLayout_structureSelect.addWidget(self.radioButton_structure2)
        self.vLayout_paramButtons.addWidget(self.groupBox_structureSelect)
        self.hLayout_Cbuttons = QtGui.QHBoxLayout()
        self.hLayout_Cbuttons.setObjectName(_fromUtf8("hLayout_Cbuttons"))
        self.toolButton_updateParams = QtGui.QToolButton(self.gridLayoutWidget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Media-playback-start.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_updateParams.setIcon(icon2)
        self.toolButton_updateParams.setObjectName(_fromUtf8("toolButton_updateParams"))
        self.hLayout_Cbuttons.addWidget(self.toolButton_updateParams)
        self.toolButton_randomStructure = QtGui.QToolButton(self.gridLayoutWidget_2)
        self.toolButton_randomStructure.setIcon(icon)
        self.toolButton_randomStructure.setObjectName(_fromUtf8("toolButton_randomStructure"))
        self.hLayout_Cbuttons.addWidget(self.toolButton_randomStructure)
        self.vLayout_paramButtons.addLayout(self.hLayout_Cbuttons)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vLayout_paramButtons.addItem(spacerItem)
        self.checkBox_autoupdateStructure = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_autoupdateStructure.setObjectName(_fromUtf8("checkBox_autoupdateStructure"))
        self.vLayout_paramButtons.addWidget(self.checkBox_autoupdateStructure)
        self.checkBox_showLabels = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_showLabels.setObjectName(_fromUtf8("checkBox_showLabels"))
        self.vLayout_paramButtons.addWidget(self.checkBox_showLabels)
        self.checkBox_suffix = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_suffix.setObjectName(_fromUtf8("checkBox_suffix"))
        self.vLayout_paramButtons.addWidget(self.checkBox_suffix)
        self.horizontalLayout.addLayout(self.vLayout_paramButtons)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 3)
        self.gridLayout_params.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabParams, _fromUtf8(""))
        self.tab_xtalData = QtGui.QWidget()
        self.tab_xtalData.setObjectName(_fromUtf8("tab_xtalData"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tab_xtalData)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 471, 331))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_xtalData = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_xtalData.setMargin(0)
        self.gridLayout_xtalData.setObjectName(_fromUtf8("gridLayout_xtalData"))
        self.treeView_xtalData = QtGui.QTreeView(self.gridLayoutWidget_3)
        self.treeView_xtalData.setObjectName(_fromUtf8("treeView_xtalData"))
        self.gridLayout_xtalData.addWidget(self.treeView_xtalData, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_xtalData, _fromUtf8(""))
        self.tab_log = QtGui.QWidget()
        self.tab_log.setObjectName(_fromUtf8("tab_log"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_log)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 471, 331))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_log = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_log.setMargin(0)
        self.gridLayout_log.setObjectName(_fromUtf8("gridLayout_log"))
        self.textEdit_log = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_log.setObjectName(_fromUtf8("textEdit_log"))
        self.gridLayout_log.addWidget(self.textEdit_log, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_log, _fromUtf8(""))
        self.hLayout_top.addWidget(self.tabWidget)
        self.QMayavi_structure = MayaviQStructureWidget(self.container)
        self.QMayavi_structure.setObjectName(_fromUtf8("QMayavi_structure"))
        self.hLayout_top.addWidget(self.QMayavi_structure)
        self.hLayout_top.setStretch(0, 1)
        self.hLayout_top.setStretch(1, 1)
        self.vLayout_main.addLayout(self.hLayout_top)
        self.line = QtGui.QFrame(self.container)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.vLayout_main.addWidget(self.line)
        self.hLayout_bottom = QtGui.QHBoxLayout()
        self.hLayout_bottom.setObjectName(_fromUtf8("hLayout_bottom"))
        self.vLayout_mainvis = QtGui.QVBoxLayout()
        self.vLayout_mainvis.setObjectName(_fromUtf8("vLayout_mainvis"))
        self.hLayout_xyselector = QtGui.QHBoxLayout()
        self.hLayout_xyselector.setObjectName(_fromUtf8("hLayout_xyselector"))
        self.label_xaxis = QtGui.QLabel(self.container)
        self.label_xaxis.setObjectName(_fromUtf8("label_xaxis"))
        self.hLayout_xyselector.addWidget(self.label_xaxis)
        self.comboBox_x = QtGui.QComboBox(self.container)
        self.comboBox_x.setObjectName(_fromUtf8("comboBox_x"))
        self.hLayout_xyselector.addWidget(self.comboBox_x)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout_xyselector.addItem(spacerItem1)
        self.checkBox_fine = QtGui.QCheckBox(self.container)
        self.checkBox_fine.setObjectName(_fromUtf8("checkBox_fine"))
        self.hLayout_xyselector.addWidget(self.checkBox_fine)
        self.checkBox_autoupdateRPlots = QtGui.QCheckBox(self.container)
        self.checkBox_autoupdateRPlots.setObjectName(_fromUtf8("checkBox_autoupdateRPlots"))
        self.hLayout_xyselector.addWidget(self.checkBox_autoupdateRPlots)
        self.toolButton_updateRPlots = QtGui.QToolButton(self.container)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Media-playback-start.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_updateRPlots.setIcon(icon3)
        self.toolButton_updateRPlots.setObjectName(_fromUtf8("toolButton_updateRPlots"))
        self.hLayout_xyselector.addWidget(self.toolButton_updateRPlots)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hLayout_xyselector.addItem(spacerItem2)
        self.label_yaxis = QtGui.QLabel(self.container)
        self.label_yaxis.setObjectName(_fromUtf8("label_yaxis"))
        self.hLayout_xyselector.addWidget(self.label_yaxis)
        self.comboBox_y = QtGui.QComboBox(self.container)
        self.comboBox_y.setObjectName(_fromUtf8("comboBox_y"))
        self.hLayout_xyselector.addWidget(self.comboBox_y)
        self.vLayout_mainvis.addLayout(self.hLayout_xyselector)
        self.hLayout_topView = QtGui.QHBoxLayout()
        self.hLayout_topView.setObjectName(_fromUtf8("hLayout_topView"))
        self.dss_dmin = DoubleSpinSlider(self.container)
        self.dss_dmin.setObjectName(_fromUtf8("dss_dmin"))
        self.hLayout_topView.addWidget(self.dss_dmin)
        self.QMayavi_top = MayaviQRPlotWidget(self.container)
        self.QMayavi_top.setMinimumSize(QtCore.QSize(0, 20))
        self.QMayavi_top.setObjectName(_fromUtf8("QMayavi_top"))
        self.hLayout_topView.addWidget(self.QMayavi_top)
        self.hLayout_topView.setStretch(1, 1)
        self.vLayout_mainvis.addLayout(self.hLayout_topView)
        self.vLayout_mainvis.setStretch(1, 1)
        self.hLayout_bottom.addLayout(self.vLayout_mainvis)
        self.line_2 = QtGui.QFrame(self.container)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hLayout_bottom.addWidget(self.line_2)
        self.QMayavi_3D = MayaviQRPlotWidget(self.container)
        self.QMayavi_3D.setObjectName(_fromUtf8("QMayavi_3D"))
        self.hLayout_bottom.addWidget(self.QMayavi_3D)
        self.hLayout_bottom.setStretch(0, 1)
        self.hLayout_bottom.setStretch(2, 1)
        self.vLayout_main.addLayout(self.hLayout_bottom)
        self.vLayout_main.setStretch(0, 1)
        self.vLayout_main.setStretch(2, 1)
        self.hLayout_main.addLayout(self.vLayout_main)
        self.gridLayout.addLayout(self.hLayout_main, 0, 0, 1, 1)
        XtalxplorerMainWindow.setCentralWidget(self.container)
        self.menubar = QtGui.QMenuBar(XtalxplorerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        self.menu_Job = QtGui.QMenu(self.menubar)
        self.menu_Job.setObjectName(_fromUtf8("menu_Job"))
        XtalxplorerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(XtalxplorerMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        XtalxplorerMainWindow.setStatusBar(self.statusbar)
        self.action_about = QtGui.QAction(XtalxplorerMainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_open = QtGui.QAction(XtalxplorerMainWindow)
        self.action_open.setIcon(icon1)
        self.action_open.setPriority(QtGui.QAction.HighPriority)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_quit = QtGui.QAction(XtalxplorerMainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/System-log-out-2.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon4)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.action_run = QtGui.QAction(XtalxplorerMainWindow)
        self.action_run.setIcon(icon3)
        self.action_run.setObjectName(_fromUtf8("action_run"))
        self.action_pause = QtGui.QAction(XtalxplorerMainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Media-playback-pause.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pause.setIcon(icon5)
        self.action_pause.setObjectName(_fromUtf8("action_pause"))
        self.action_stop = QtGui.QAction(XtalxplorerMainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Media-playback-stop.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_stop.setIcon(icon6)
        self.action_stop.setObjectName(_fromUtf8("action_stop"))
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_help.addAction(self.action_about)
        self.menu_Job.addAction(self.action_run)
        self.menu_Job.addAction(self.action_pause)
        self.menu_Job.addAction(self.action_stop)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_Job.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(XtalxplorerMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_quit, QtCore.SIGNAL(_fromUtf8("activated()")), XtalxplorerMainWindow.close)
        QtCore.QObject.connect(self.action_about, QtCore.SIGNAL(_fromUtf8("activated()")), XtalxplorerMainWindow.about)
        QtCore.QObject.connect(self.action_open, QtCore.SIGNAL(_fromUtf8("activated()")), XtalxplorerMainWindow.browse_structure)
        QtCore.QObject.connect(self.toolButton_open, QtCore.SIGNAL(_fromUtf8("clicked()")), XtalxplorerMainWindow.browse_structure)
        QtCore.QObject.connect(self.lstWidget_atoms, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), XtalxplorerMainWindow.load_atom_params)
        QtCore.QObject.connect(self.toolButton_updateParams, QtCore.SIGNAL(_fromUtf8("clicked()")), XtalxplorerMainWindow.update_params)
        QtCore.QObject.connect(self.checkBox_autoupdateStructure, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), XtalxplorerMainWindow.handle_autoupdate_structure)
        QtCore.QObject.connect(self.checkBox_showLabels, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), XtalxplorerMainWindow.invalidate_cached_params)
        QtCore.QObject.connect(self.checkBox_suffix, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), XtalxplorerMainWindow.invalidate_cached_params)
        QtCore.QObject.connect(self.checkBox_autoupdateRPlots, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), XtalxplorerMainWindow.handle_autoupdate_r_plots)
        QtCore.QObject.connect(self.radioButton_structure1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), XtalxplorerMainWindow._load_structure)
        QtCore.QObject.connect(self.toolButton_randomStructure, QtCore.SIGNAL(_fromUtf8("clicked()")), XtalxplorerMainWindow.randomise_structure)
        QtCore.QObject.connect(self.toolButton_copyStructure, QtCore.SIGNAL(_fromUtf8("clicked()")), XtalxplorerMainWindow._copy_structure)
        QtCore.QObject.connect(self.toolButton_updateRPlots, QtCore.SIGNAL(_fromUtf8("clicked()")), XtalxplorerMainWindow.update_rplots)
        QtCore.QObject.connect(self.checkBox_fine, QtCore.SIGNAL(_fromUtf8("clicked()")), XtalxplorerMainWindow.update_rplots)
        QtCore.QMetaObject.connectSlotsByName(XtalxplorerMainWindow)

    def retranslateUi(self, XtalxplorerMainWindow):
        XtalxplorerMainWindow.setWindowTitle(_translate("XtalxplorerMainWindow", "MainWindow", None))
        self.toolButton_open.setText(_translate("XtalxplorerMainWindow", "open file", None))
        self.toolButton_copyStructure.setText(_translate("XtalxplorerMainWindow", "Copy", None))
        self.groupBox_structureSelect.setTitle(_translate("XtalxplorerMainWindow", "Structure select:", None))
        self.radioButton_structure1.setText(_translate("XtalxplorerMainWindow", "trial structure", None))
        self.radioButton_structure2.setText(_translate("XtalxplorerMainWindow", "target structure", None))
        self.toolButton_updateParams.setText(_translate("XtalxplorerMainWindow", "...", None))
        self.toolButton_randomStructure.setToolTip(_translate("XtalxplorerMainWindow", "randomise structure", None))
        self.toolButton_randomStructure.setText(_translate("XtalxplorerMainWindow", "...", None))
        self.checkBox_autoupdateStructure.setText(_translate("XtalxplorerMainWindow", "Autoupdate -->", None))
        self.checkBox_showLabels.setText(_translate("XtalxplorerMainWindow", "Atom labels", None))
        self.checkBox_suffix.setToolTip(_translate("XtalxplorerMainWindow", "Add suffixes to symmetry generated atom labels", None))
        self.checkBox_suffix.setText(_translate("XtalxplorerMainWindow", "suffix symm.eq.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabParams), _translate("XtalxplorerMainWindow", "Coordinates", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_xtalData), _translate("XtalxplorerMainWindow", "Crystal data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), _translate("XtalxplorerMainWindow", "Log", None))
        self.label_xaxis.setText(_translate("XtalxplorerMainWindow", "x-axis:", None))
        self.checkBox_fine.setText(_translate("XtalxplorerMainWindow", "fine", None))
        self.checkBox_autoupdateRPlots.setText(_translate("XtalxplorerMainWindow", "Autoupdate", None))
        self.toolButton_updateRPlots.setText(_translate("XtalxplorerMainWindow", "...", None))
        self.label_yaxis.setText(_translate("XtalxplorerMainWindow", "y-axis:", None))
        self.menu_file.setTitle(_translate("XtalxplorerMainWindow", "&File", None))
        self.menu_help.setTitle(_translate("XtalxplorerMainWindow", "&Help", None))
        self.menu_Job.setTitle(_translate("XtalxplorerMainWindow", "&Job", None))
        self.action_about.setText(_translate("XtalxplorerMainWindow", "&About", None))
        self.action_about.setStatusTip(_translate("XtalxplorerMainWindow", "About this programme", None))
        self.action_about.setShortcut(_translate("XtalxplorerMainWindow", "Ctrl+A", None))
        self.action_open.setText(_translate("XtalxplorerMainWindow", "&Open", None))
        self.action_open.setShortcut(_translate("XtalxplorerMainWindow", "Ctrl+O", None))
        self.action_quit.setText(_translate("XtalxplorerMainWindow", "&Quit", None))
        self.action_quit.setStatusTip(_translate("XtalxplorerMainWindow", "Exit this programme", None))
        self.action_quit.setShortcut(_translate("XtalxplorerMainWindow", "Ctrl+Q", None))
        self.action_run.setText(_translate("XtalxplorerMainWindow", "&Run", None))
        self.action_run.setShortcut(_translate("XtalxplorerMainWindow", "Ctrl+R", None))
        self.action_pause.setText(_translate("XtalxplorerMainWindow", "&Pause", None))
        self.action_pause.setShortcut(_translate("XtalxplorerMainWindow", "Ctrl+P", None))
        self.action_stop.setText(_translate("XtalxplorerMainWindow", "&Stop", None))
        self.action_stop.setShortcut(_translate("XtalxplorerMainWindow", "Ctrl+S", None))

from gui.doublespinslider import DoubleSpinSlider
from gui.mayaviqwidget import MayaviQStructureWidget, MayaviQRPlotWidget
import gui_rc
