# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainApp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_UGMM(object):
    def setupUi(self, UGMM):
        if not UGMM.objectName():
            UGMM.setObjectName(u"UGMM")
        UGMM.setEnabled(True)
        UGMM.resize(1243, 863)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UGMM.sizePolicy().hasHeightForWidth())
        UGMM.setSizePolicy(sizePolicy)
        UGMM.setMaximumSize(QSize(16777215, 12777215))
        UGMM.setLayoutDirection(Qt.LeftToRight)
        UGMM.setStyleSheet(u"*{\n"
"	font-family: Roboto;\n"
"	font-size: 10pt;\n"
"}\n"
".QFrame{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
".QPushButton{\n"
"	color: #FAFAFA;\n"
"	background-color: #2CC985;\n"
"	border: 0px;\n"
"	border-radius: 6px;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #bdc3c7;\n"
"    color: #7f8c8d;\n"
"}\n"
".QPushButton:hover{\n"
"	background-color: #0C955A;\n"
"}\n"
".QPushButton:pressed{\n"
"	background-color: #2CC985;\n"
"}\n"
".QToolButton{\n"
"	color: #FAFAFA;\n"
"	background-color: #2CC985;\n"
"	border: 0px;\n"
"	border-radius: 6px;\n"
"}\n"
".QToolButton:hover{\n"
"	background-color: #0C955A;\n"
"}\n"
".QToolButton:pressed{\n"
"	background-color: #2CC985;\n"
"}\n"
".QLineEdit{\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 4px;\n"
"}\n"
".QComboBox{\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 4px\n"
"}\n"
".QComboBox::drop-down:button{\n"
"	border: none;\n"
"}\n"
".QComboBox::down-arrow{\n"
"	image: url(\"asset/arrow.pn"
                        "g\");\n"
"	width: 8px;\n"
"	height: 8px;\n"
"}\n"
".QProgressBar {\n"
"    border: 1px solid rgba(0,0,0,0.5);\n"
"    border-radius: 8px;\n"
"    background-color: #FFFFFF;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"}\n"
".QProgressBar::chunk {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Configuraci\u00f3n del \u00e1rea de deslizamiento */\n"
".QScrollArea{\n"
"	border: 0px;\n"
"	background-color: none;\n"
"}\n"
"\n"
"/* Configuraci\u00f3n de las barras de deslizamiento */\n"
".QScrollBar:vertical{\n"
"    background-color: none;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
".QScrollBar::handle:vertical{\n"
"    background-color: #8C8C8C;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
".QScrollBar::sub-line:vertical{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;"
                        "\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::sub-line:vertical:hover{\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::sub-line:vertical:on{\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::add-line:vertical{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::add-line:vertical:hover{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::add-line:vertical:on{\n"
""
                        "    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::up-arrow:vertical{\n"
"    background: none;\n"
"}\n"
".QScrollBar::down-arrow:vertical{\n"
"    background: none;\n"
"}\n"
".QScrollBar::add-page:vertical{\n"
"    background: none;\n"
"}\n"
".QScrollBar::sub-page:vertical{\n"
"    background: none;\n"
"}\n"
"\n"
".QScrollBar:horizontal{\n"
"    background-color: none;\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
".QScrollBar::handle:horizontal{\n"
"    background-color: #8C8C8C;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
".QScrollBar::sub-line:horizontal{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollB"
                        "ar::sub-line:horizontal:hover{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::sub-line:horizontal:on{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::add-line:horizontal{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::add-line:horizontal:hover{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::add-line:horizontal:on{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 1"
                        "0px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
".QScrollBar::up-arrow:horizontal{\n"
"    background: none;\n"
"}\n"
".QScrollBar::down-arrow:horizontal{\n"
"    background: none;\n"
"}\n"
".QScrollBar::add-page:horizontal{\n"
"    background: none;\n"
"}\n"
".QScrollBar::sub-page:horizontal{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Configuraci\u00f3n del explorador del proyecto*/\n"
"#title_explorer{\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"/* Configuraci\u00f3n de los men\u00fas de dise\u00f1o */\n"
"#files{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
"#run{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
"#parameters{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
"#holes_designer{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
"#c"
                        "harge_designer{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
"#init_designer{\n"
"	background-color: #DBDBDB;\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"/* Configuraci\u00f3n de las pesta\u00f1as de visualizaci\u00f3n */\n"
"#viewer_2D{\n"
"	background-color: white;\n"
"}\n"
"#viewer_3D{\n"
"	background-color: white;\n"
"}\n"
"#viewer_eval{\n"
"	background-color: white;\n"
"}")
        self.bmMenubar = QAction(UGMM)
        self.bmMenubar.setObjectName(u"bmMenubar")
        self.dpMenubar = QAction(UGMM)
        self.dpMenubar.setObjectName(u"dpMenubar")
        self.actionImport_File = QAction(UGMM)
        self.actionImport_File.setObjectName(u"actionImport_File")
        self.actionImport_File.setEnabled(False)
        self.actionAun_nada = QAction(UGMM)
        self.actionAun_nada.setObjectName(u"actionAun_nada")
        self.actionAun_nada.setEnabled(False)
        self.actionSimulation_Results = QAction(UGMM)
        self.actionSimulation_Results.setObjectName(u"actionSimulation_Results")
        self.actionSimulation_Results.setEnabled(False)
        self.actionModelo_de_fragmentacion = QAction(UGMM)
        self.actionModelo_de_fragmentacion.setObjectName(u"actionModelo_de_fragmentacion")
        self.actionModelo_de_fragmentacion.setEnabled(False)
        self.config = QAction(UGMM)
        self.config.setObjectName(u"config")
        self.config.setEnabled(True)
        self.res = QAction(UGMM)
        self.res.setObjectName(u"res")
        self.result_folder = QAction(UGMM)
        self.result_folder.setObjectName(u"result_folder")
        self.actionVisualizador_de_simulacion = QAction(UGMM)
        self.actionVisualizador_de_simulacion.setObjectName(u"actionVisualizador_de_simulacion")
        self.actionVisualizador_de_simulacion.setEnabled(False)
        self.viewer = QAction(UGMM)
        self.viewer.setObjectName(u"viewer")
        self.salida = QAction(UGMM)
        self.salida.setObjectName(u"salida")
        self.actionGuardar_simulacion_en = QAction(UGMM)
        self.actionGuardar_simulacion_en.setObjectName(u"actionGuardar_simulacion_en")
        self.result_folders = QAction(UGMM)
        self.result_folders.setObjectName(u"result_folders")
        self.actionManual_de_Usuario = QAction(UGMM)
        self.actionManual_de_Usuario.setObjectName(u"actionManual_de_Usuario")
        self.actionManual_de_Usuario.setEnabled(False)
        self.centralwidget = QWidget(UGMM)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 12777215))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1223, 800))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.FrameInput = QFrame(self.scrollAreaWidgetContents)
        self.FrameInput.setObjectName(u"FrameInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FrameInput.sizePolicy().hasHeightForWidth())
        self.FrameInput.setSizePolicy(sizePolicy1)
        self.FrameInput.setMinimumSize(QSize(340, 600))
        self.FrameInput.setMaximumSize(QSize(340, 16777215))
        self.FrameInput.setStyleSheet(u"")
        self.FrameInput.setFrameShape(QFrame.StyledPanel)
        self.FrameInput.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.FrameInput)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 10, 0, 1, 5)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 1, 0, 1, 4)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 2, 0, 1, 5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_11, 6, 0, 1, 5)

        self.verticalSpacer_12 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 13, 0, 1, 5)

        self.parameters = QGridLayout()
        self.parameters.setObjectName(u"parameters")
        self.label_9 = QLabel(self.FrameInput)
        self.label_9.setObjectName(u"label_9")

        self.parameters.addWidget(self.label_9, 6, 1, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.FrameInput)
        self.label_8.setObjectName(u"label_8")

        self.parameters.addWidget(self.label_8, 1, 0, 1, 4, Qt.AlignHCenter)

        self.inputmaxperiod = QLineEdit(self.FrameInput)
        self.inputmaxperiod.setObjectName(u"inputmaxperiod")
        self.inputmaxperiod.setMaximumSize(QSize(360, 16777215))

        self.parameters.addWidget(self.inputmaxperiod, 6, 2, 1, 1)

        self.label_7 = QLabel(self.FrameInput)
        self.label_7.setObjectName(u"label_7")

        self.parameters.addWidget(self.label_7, 7, 1, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.parameters.addItem(self.verticalSpacer_3, 4, 1, 1, 2)

        self.label_5 = QLabel(self.FrameInput)
        self.label_5.setObjectName(u"label_5")

        self.parameters.addWidget(self.label_5, 2, 1, 1, 1, Qt.AlignLeft)

        self.inputN = QLineEdit(self.FrameInput)
        self.inputN.setObjectName(u"inputN")
        self.inputN.setMaximumSize(QSize(360, 16777215))

        self.parameters.addWidget(self.inputN, 2, 2, 1, 1)

        self.label_6 = QLabel(self.FrameInput)
        self.label_6.setObjectName(u"label_6")

        self.parameters.addWidget(self.label_6, 3, 1, 1, 1, Qt.AlignLeft)

        self.inputton_per_period = QLineEdit(self.FrameInput)
        self.inputton_per_period.setObjectName(u"inputton_per_period")
        self.inputton_per_period.setMaximumSize(QSize(360, 16777215))

        self.parameters.addWidget(self.inputton_per_period, 7, 2, 1, 1)

        self.inputMVC = QLineEdit(self.FrameInput)
        self.inputMVC.setObjectName(u"inputMVC")
        self.inputMVC.setMaximumSize(QSize(360, 16777215))

        self.parameters.addWidget(self.inputMVC, 3, 2, 1, 1)

        self.label_10 = QLabel(self.FrameInput)
        self.label_10.setObjectName(u"label_10")

        self.parameters.addWidget(self.label_10, 5, 1, 1, 2, Qt.AlignHCenter)


        self.gridLayout_5.addLayout(self.parameters, 8, 0, 1, 5)

        self.verticalSpacer_4 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 9, 0, 1, 5)

        self.files = QGridLayout()
        self.files.setObjectName(u"files")
        self.bmImportButton = QToolButton(self.FrameInput)
        self.bmImportButton.setObjectName(u"bmImportButton")

        self.files.addWidget(self.bmImportButton, 2, 2, 1, 1)

        self.label_3 = QLabel(self.FrameInput)
        self.label_3.setObjectName(u"label_3")

        self.files.addWidget(self.label_3, 6, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.dpImportButton = QToolButton(self.FrameInput)
        self.dpImportButton.setObjectName(u"dpImportButton")

        self.files.addWidget(self.dpImportButton, 5, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.FrameInput)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_3.setReadOnly(True)

        self.files.addWidget(self.lineEdit_3, 6, 1, 1, 1)

        self.change_dcell = QCheckBox(self.FrameInput)
        self.change_dcell.setObjectName(u"change_dcell")

        self.files.addWidget(self.change_dcell, 3, 1, 1, 1, Qt.AlignHCenter)

        self.table_dcell = QTableWidget(self.FrameInput)
        if (self.table_dcell.columnCount() < 2):
            self.table_dcell.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_dcell.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_dcell.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_dcell.rowCount() < 3):
            self.table_dcell.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_dcell.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_dcell.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_dcell.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_dcell.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_dcell.setItem(1, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_dcell.setItem(2, 1, __qtablewidgetitem7)
        self.table_dcell.setObjectName(u"table_dcell")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_dcell.sizePolicy().hasHeightForWidth())
        self.table_dcell.setSizePolicy(sizePolicy2)
        self.table_dcell.setMaximumSize(QSize(130, 116))
        self.table_dcell.horizontalHeader().setDefaultSectionSize(55)

        self.files.addWidget(self.table_dcell, 4, 1, 1, 1, Qt.AlignHCenter)

        self.label_13 = QLabel(self.FrameInput)
        self.label_13.setObjectName(u"label_13")

        self.files.addWidget(self.label_13, 3, 0, 2, 1)

        self.bmName = QLineEdit(self.FrameInput)
        self.bmName.setObjectName(u"bmName")
        self.bmName.setEnabled(True)
        self.bmName.setMaximumSize(QSize(500, 16777215))
        self.bmName.setReadOnly(True)

        self.files.addWidget(self.bmName, 2, 1, 1, 1)

        self.dpName = QLineEdit(self.FrameInput)
        self.dpName.setObjectName(u"dpName")
        self.dpName.setEnabled(True)
        self.dpName.setMaximumSize(QSize(500, 16777215))
        self.dpName.setReadOnly(True)

        self.files.addWidget(self.dpName, 5, 1, 1, 1)

        self.toolButton_3 = QToolButton(self.FrameInput)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setEnabled(False)

        self.files.addWidget(self.toolButton_3, 6, 2, 1, 1)

        self.label_2 = QLabel(self.FrameInput)
        self.label_2.setObjectName(u"label_2")

        self.files.addWidget(self.label_2, 5, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label = QLabel(self.FrameInput)
        self.label.setObjectName(u"label")

        self.files.addWidget(self.label, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.FrameInput)
        self.label_4.setObjectName(u"label_4")

        self.files.addWidget(self.label_4, 1, 0, 1, 3, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.files.addItem(self.verticalSpacer_8, 0, 0, 1, 3)


        self.gridLayout_5.addLayout(self.files, 0, 0, 1, 5)

        self.label_12 = QLabel(self.FrameInput)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 5, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 14, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 7, 0, 1, 5)

        self.run = QGridLayout()
        self.run.setObjectName(u"run")
        self.stop = QPushButton(self.FrameInput)
        self.stop.setObjectName(u"stop")
        self.stop.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy2)
        self.stop.setMinimumSize(QSize(90, 0))
        self.stop.setMaximumSize(QSize(120, 40))

        self.run.addWidget(self.stop, 0, 2, 1, 1, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.FrameInput)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(240, 0))
        self.progressBar.setMaximumSize(QSize(650, 16777215))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.progressBar.setInvertedAppearance(False)

        self.run.addWidget(self.progressBar, 1, 0, 1, 3)

        self.simButton = QPushButton(self.FrameInput)
        self.simButton.setObjectName(u"simButton")
        sizePolicy2.setHeightForWidth(self.simButton.sizePolicy().hasHeightForWidth())
        self.simButton.setSizePolicy(sizePolicy2)
        self.simButton.setMinimumSize(QSize(110, 0))

        self.run.addWidget(self.simButton, 0, 0, 1, 2, Qt.AlignHCenter)

        self.sim_status = QLabel(self.FrameInput)
        self.sim_status.setObjectName(u"sim_status")
        self.sim_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.run.addWidget(self.sim_status, 3, 0, 1, 3, Qt.AlignLeft)


        self.gridLayout_5.addLayout(self.run, 15, 0, 1, 5)

        self.salida_button = QToolButton(self.FrameInput)
        self.salida_button.setObjectName(u"salida_button")

        self.gridLayout_5.addWidget(self.salida_button, 4, 4, 1, 1)

        self.showsimruta = QLineEdit(self.FrameInput)
        self.showsimruta.setObjectName(u"showsimruta")
        self.showsimruta.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.showsimruta.sizePolicy().hasHeightForWidth())
        self.showsimruta.setSizePolicy(sizePolicy2)
        self.showsimruta.setMaximumSize(QSize(1000, 16777215))

        self.gridLayout_5.addWidget(self.showsimruta, 4, 0, 1, 4)

        self.verticalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 16, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 11, 3, 1, 1)

        self.stress_model = QCheckBox(self.FrameInput)
        self.stress_model.setObjectName(u"stress_model")
        self.stress_model.setEnabled(False)
        self.stress_model.setTabletTracking(False)
        self.stress_model.setAcceptDrops(False)

        self.gridLayout_5.addWidget(self.stress_model, 11, 1, 1, 2, Qt.AlignLeft)

        self.frag_model = QCheckBox(self.FrameInput)
        self.frag_model.setObjectName(u"frag_model")
        self.frag_model.setEnabled(False)
        self.frag_model.setTabletTracking(False)

        self.gridLayout_5.addWidget(self.frag_model, 12, 1, 1, 2, Qt.AlignLeft)


        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_9, 1, 0, 1, 1)


        self.gridLayout_12.addWidget(self.FrameInput, 0, 0, 1, 1)

        self.FrameOutput = QFrame(self.scrollAreaWidgetContents)
        self.FrameOutput.setObjectName(u"FrameOutput")
        sizePolicy.setHeightForWidth(self.FrameOutput.sizePolicy().hasHeightForWidth())
        self.FrameOutput.setSizePolicy(sizePolicy)
        self.FrameOutput.setMinimumSize(QSize(850, 600))
        self.FrameOutput.setMaximumSize(QSize(16777215, 16777215))
        self.FrameOutput.setStyleSheet(u"")
        self.FrameOutput.setFrameShape(QFrame.StyledPanel)
        self.FrameOutput.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.FrameOutput)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 5, -1, -1)
        self.titulografica = QLabel(self.FrameOutput)
        self.titulografica.setObjectName(u"titulografica")

        self.gridLayout_6.addWidget(self.titulografica, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tabs = QTabWidget(self.FrameOutput)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setEnabled(True)
        self.dimension2 = QWidget()
        self.dimension2.setObjectName(u"dimension2")
        self.dimension2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dimension2.sizePolicy().hasHeightForWidth())
        self.dimension2.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(self.dimension2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gif = QPushButton(self.dimension2)
        self.gif.setObjectName(u"gif")
        self.gif.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.gif.sizePolicy().hasHeightForWidth())
        self.gif.setSizePolicy(sizePolicy2)
        self.gif.setMinimumSize(QSize(200, 0))

        self.gridLayout_7.addWidget(self.gif, 2, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.graphlayout2d = QHBoxLayout()
        self.graphlayout2d.setSpacing(6)
        self.graphlayout2d.setObjectName(u"graphlayout2d")

        self.gridLayout_7.addLayout(self.graphlayout2d, 1, 0, 1, 3)

        self.inputgraph2d = QWidget(self.dimension2)
        self.inputgraph2d.setObjectName(u"inputgraph2d")
        sizePolicy.setHeightForWidth(self.inputgraph2d.sizePolicy().hasHeightForWidth())
        self.inputgraph2d.setSizePolicy(sizePolicy)
        self.inputgraph2d.setMaximumSize(QSize(16777215, 160))
        self.gridLayout = QGridLayout(self.inputgraph2d)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 2, 1, 1, 4)

        self.cat = QComboBox(self.inputgraph2d)
        self.cat.setObjectName(u"cat")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cat.sizePolicy().hasHeightForWidth())
        self.cat.setSizePolicy(sizePolicy3)
        self.cat.setMinimumSize(QSize(120, 0))
        self.cat.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.cat, 1, 4, 1, 1, Qt.AlignLeft)

        self.extrbox = QComboBox(self.inputgraph2d)
        self.extrbox.setObjectName(u"extrbox")
        self.extrbox.setMinimumSize(QSize(120, 0))
        self.extrbox.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.extrbox, 1, 2, 1, 1, Qt.AlignLeft)

        self.grapher = QPushButton(self.inputgraph2d)
        self.grapher.setObjectName(u"grapher")
        self.grapher.setEnabled(False)
        self.grapher.setMaximumSize(QSize(200, 22))

        self.gridLayout.addWidget(self.grapher, 7, 3, 1, 1)

        self.update_axe = QLineEdit(self.inputgraph2d)
        self.update_axe.setObjectName(u"update_axe")
        self.update_axe.setEnabled(False)
        self.update_axe.setMaximumSize(QSize(50, 16777215))
        self.update_axe.setLayoutDirection(Qt.LeftToRight)
        self.update_axe.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.update_axe, 6, 3, 1, 1, Qt.AlignHCenter)

        self.mincut = QLabel(self.inputgraph2d)
        self.mincut.setObjectName(u"mincut")

        self.gridLayout.addWidget(self.mincut, 6, 2, 1, 1)

        self.coord = QLabel(self.inputgraph2d)
        self.coord.setObjectName(u"coord")
        self.coord.setMinimumSize(QSize(59, 13))

        self.gridLayout.addWidget(self.coord, 3, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.corte = QSlider(self.inputgraph2d)
        self.corte.setObjectName(u"corte")
        self.corte.setEnabled(False)
        self.corte.setSingleStep(2)
        self.corte.setValue(0)
        self.corte.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.corte, 4, 2, 2, 3)

        self.maxcut = QLabel(self.inputgraph2d)
        self.maxcut.setObjectName(u"maxcut")

        self.gridLayout.addWidget(self.maxcut, 6, 4, 1, 1, Qt.AlignRight)

        self.label_11 = QLabel(self.inputgraph2d)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1, Qt.AlignRight)

        self.label_14 = QLabel(self.inputgraph2d)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 3, 1, 1, Qt.AlignRight)

        self.graphy = QCheckBox(self.inputgraph2d)
        self.graphy.setObjectName(u"graphy")
        self.graphy.setEnabled(False)

        self.gridLayout.addWidget(self.graphy, 5, 1, 1, 1)

        self.graphx = QCheckBox(self.inputgraph2d)
        self.graphx.setObjectName(u"graphx")
        self.graphx.setEnabled(False)

        self.gridLayout.addWidget(self.graphx, 4, 1, 1, 1)

        self.graphz = QCheckBox(self.inputgraph2d)
        self.graphz.setObjectName(u"graphz")
        self.graphz.setEnabled(False)

        self.gridLayout.addWidget(self.graphz, 6, 1, 1, 1)

        self.save_graph_axe = QPushButton(self.inputgraph2d)
        self.save_graph_axe.setObjectName(u"save_graph_axe")
        self.save_graph_axe.setEnabled(False)
        self.save_graph_axe.setMinimumSize(QSize(100, 0))
        self.save_graph_axe.setMaximumSize(QSize(100, 22))

        self.gridLayout.addWidget(self.save_graph_axe, 7, 1, 1, 1)


        self.gridLayout_7.addWidget(self.inputgraph2d, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabs.addTab(self.dimension2, "")
        self.dimension3 = QWidget()
        self.dimension3.setObjectName(u"dimension3")
        self.dimension3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dimension3.sizePolicy().hasHeightForWidth())
        self.dimension3.setSizePolicy(sizePolicy)
        self.gridLayout_14 = QGridLayout(self.dimension3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.graphlayout3d = QHBoxLayout()
        self.graphlayout3d.setObjectName(u"graphlayout3d")

        self.gridLayout_8.addLayout(self.graphlayout3d, 3, 0, 1, 2)

        self.label_15 = QLabel(self.dimension3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignRight)

        self.cat3d = QComboBox(self.dimension3)
        self.cat3d.setObjectName(u"cat3d")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cat3d.sizePolicy().hasHeightForWidth())
        self.cat3d.setSizePolicy(sizePolicy4)
        self.cat3d.setMinimumSize(QSize(100, 0))
        self.cat3d.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_8.addWidget(self.cat3d, 0, 1, 1, 1, Qt.AlignLeft)

        self.view3d = QPushButton(self.dimension3)
        self.view3d.setObjectName(u"view3d")
        self.view3d.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.view3d.sizePolicy().hasHeightForWidth())
        self.view3d.setSizePolicy(sizePolicy2)
        self.view3d.setMinimumSize(QSize(200, 0))

        self.gridLayout_8.addWidget(self.view3d, 2, 0, 1, 2, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 1, 0, 1, 2)


        self.gridLayout_14.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.tabs.addTab(self.dimension3, "")

        self.gridLayout_6.addWidget(self.tabs, 1, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.FrameOutput, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        UGMM.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UGMM)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1243, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuModelos = QMenu(self.menubar)
        self.menuModelos.setObjectName(u"menuModelos")
        self.menuResultados = QMenu(self.menubar)
        self.menuResultados.setObjectName(u"menuResultados")
        UGMM.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UGMM)
        self.statusbar.setObjectName(u"statusbar")
        UGMM.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.inputgraph2d)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.bmImportButton, self.bmName)
        QWidget.setTabOrder(self.bmName, self.dpImportButton)
        QWidget.setTabOrder(self.dpImportButton, self.dpName)
        QWidget.setTabOrder(self.dpName, self.toolButton_3)
        QWidget.setTabOrder(self.toolButton_3, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.inputN)
        QWidget.setTabOrder(self.inputN, self.inputMVC)
        QWidget.setTabOrder(self.inputMVC, self.inputmaxperiod)
        QWidget.setTabOrder(self.inputmaxperiod, self.inputton_per_period)
        QWidget.setTabOrder(self.inputton_per_period, self.simButton)
        QWidget.setTabOrder(self.simButton, self.stop)
        QWidget.setTabOrder(self.stop, self.corte)
        QWidget.setTabOrder(self.corte, self.update_axe)
        QWidget.setTabOrder(self.update_axe, self.grapher)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuResultados.menuAction())
        self.menubar.addAction(self.menuModelos.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.bmMenubar)
        self.menuFile.addAction(self.dpMenubar)
        self.menuFile.addAction(self.actionImport_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.salida)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.result_folders)
        self.menuView.addAction(self.viewer)
        self.menuHelp.addAction(self.actionManual_de_Usuario)
        self.menuHelp.addAction(self.actionAun_nada)
        self.menuModelos.addAction(self.config)
        self.menuResultados.addAction(self.res)

        self.retranslateUi(UGMM)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(UGMM)
    # setupUi

    def retranslateUi(self, UGMM):
        UGMM.setWindowTitle(QCoreApplication.translate("UGMM", u"MainWindow", None))
        self.bmMenubar.setText(QCoreApplication.translate("UGMM", u"Importar Modelo de Bloque", None))
        self.dpMenubar.setText(QCoreApplication.translate("UGMM", u"Importar Puntos de Extracci\u00f3n", None))
        self.actionImport_File.setText(QCoreApplication.translate("UGMM", u"Importar Plan de extracci\u00f3n", None))
        self.actionAun_nada.setText(QCoreApplication.translate("UGMM", u"Sobre Gravity Flow Simulator (beta)", None))
        self.actionSimulation_Results.setText(QCoreApplication.translate("UGMM", u"Animaci\u00f3n de Extracciones", None))
        self.actionModelo_de_fragmentacion.setText(QCoreApplication.translate("UGMM", u"Tama\u00f1o de Puntos", None))
        self.config.setText(QCoreApplication.translate("UGMM", u"Ajustes de Visualizaci\u00f3n", None))
        self.res.setText(QCoreApplication.translate("UGMM", u"Ver Resultado de Simulaci\u00f3n", None))
        self.result_folder.setText(QCoreApplication.translate("UGMM", u"Ver Carpeta de Simulaci\u00f3n", None))
        self.actionVisualizador_de_simulacion.setText(QCoreApplication.translate("UGMM", u"Visualizador de Simulaci\u00f3n", None))
        self.viewer.setText(QCoreApplication.translate("UGMM", u"Visualizador de Simulaci\u00f3n", None))
        self.salida.setText(QCoreApplication.translate("UGMM", u"Seleccionar Ruta de Salida", None))
        self.actionGuardar_simulacion_en.setText(QCoreApplication.translate("UGMM", u"Guardar simulacion en ...", None))
        self.result_folders.setText(QCoreApplication.translate("UGMM", u"Ver Carpeta de Simulaciones", None))
        self.actionManual_de_Usuario.setText(QCoreApplication.translate("UGMM", u"Manual de Usuario", None))
        self.label_9.setText(QCoreApplication.translate("UGMM", u"Periodos totales", None))
        self.label_8.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Par\u00e1metros</span></p></body></html>", None))
        self.inputmaxperiod.setText(QCoreApplication.translate("UGMM", u"3", None))
        self.inputmaxperiod.setPlaceholderText(QCoreApplication.translate("UGMM", u"Ingresa solo n\u00fameros...", None))
        self.label_7.setText(QCoreApplication.translate("UGMM", u"Tonelaje por periodo", None))
        self.label_5.setText(QCoreApplication.translate("UGMM", u"Ingresar N", None))
        self.inputN.setText(QCoreApplication.translate("UGMM", u"2", None))
        self.inputN.setPlaceholderText(QCoreApplication.translate("UGMM", u"Ingresa solo n\u00fameros...", None))
        self.label_6.setText(QCoreApplication.translate("UGMM", u"Ingresar MVC", None))
        self.inputton_per_period.setText(QCoreApplication.translate("UGMM", u"400", None))
        self.inputton_per_period.setPlaceholderText(QCoreApplication.translate("UGMM", u"Ingresa solo n\u00fameros...", None))
        self.inputMVC.setText(QCoreApplication.translate("UGMM", u"2", None))
        self.inputMVC.setPlaceholderText(QCoreApplication.translate("UGMM", u"Ingresa solo n\u00fameros...", None))
        self.label_10.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Periodo</span></p></body></html>", None))
        self.bmImportButton.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.label_3.setText(QCoreApplication.translate("UGMM", u"Plan de Extracci\u00f3n", None))
        self.dpImportButton.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.change_dcell.setText(QCoreApplication.translate("UGMM", u"Edici\u00f3n", None))
        ___qtablewidgetitem = self.table_dcell.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UGMM", u"Entrada", None));
        ___qtablewidgetitem1 = self.table_dcell.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UGMM", u"Salida", None));
        ___qtablewidgetitem2 = self.table_dcell.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UGMM", u"X", None));
        ___qtablewidgetitem3 = self.table_dcell.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UGMM", u"Y", None));
        ___qtablewidgetitem4 = self.table_dcell.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("UGMM", u"Z", None));

        __sortingEnabled = self.table_dcell.isSortingEnabled()
        self.table_dcell.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.table_dcell.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("UGMM", u"2", None));
        ___qtablewidgetitem6 = self.table_dcell.item(1, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("UGMM", u"2", None));
        ___qtablewidgetitem7 = self.table_dcell.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("UGMM", u"2", None));
        self.table_dcell.setSortingEnabled(__sortingEnabled)

        self.label_13.setText(QCoreApplication.translate("UGMM", u"Tama\u00f1o de bloque", None))
        self.bmName.setPlaceholderText("")
        self.toolButton_3.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.label_2.setText(QCoreApplication.translate("UGMM", u"Puntos de Extracci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("UGMM", u"Modelo de Bloque", None))
        self.label_4.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Archivos</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Ruta de Salida</span></p></body></html>", None))
        self.stop.setText(QCoreApplication.translate("UGMM", u"Detener", None))
        self.simButton.setText(QCoreApplication.translate("UGMM", u"Simular", None))
        self.sim_status.setText("")
        self.salida_button.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.stress_model.setText(QCoreApplication.translate("UGMM", u"Modelo de Esfuerzo", None))
        self.frag_model.setText(QCoreApplication.translate("UGMM", u"Modelo de Fragmentaci\u00f3n", None))
        self.titulografica.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Gr\u00e1fica</span></p></body></html>", None))
        self.gif.setText(QCoreApplication.translate("UGMM", u"Animaci\u00f3n de extracciones", None))
        self.grapher.setText(QCoreApplication.translate("UGMM", u"Visualizar", None))
        self.mincut.setText(QCoreApplication.translate("UGMM", u"M\u00ednimo", None))
        self.coord.setText(QCoreApplication.translate("UGMM", u"Coordenada", None))
        self.maxcut.setText(QCoreApplication.translate("UGMM", u"M\u00e1ximo", None))
        self.label_11.setText(QCoreApplication.translate("UGMM", u"Periodo", None))
        self.label_14.setText(QCoreApplication.translate("UGMM", u"Categoria a visualizar", None))
        self.graphy.setText(QCoreApplication.translate("UGMM", u"Eje Y", None))
        self.graphx.setText(QCoreApplication.translate("UGMM", u"Eje X", None))
        self.graphz.setText(QCoreApplication.translate("UGMM", u"Eje Z", None))
        self.save_graph_axe.setText(QCoreApplication.translate("UGMM", u"Guardar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.dimension2), QCoreApplication.translate("UGMM", u"Vista 2D", None))
        self.label_15.setText(QCoreApplication.translate("UGMM", u"Categoria a visualizar", None))
        self.view3d.setText(QCoreApplication.translate("UGMM", u"Visualizar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.dimension3), QCoreApplication.translate("UGMM", u"Vista 3D", None))
        self.menuFile.setTitle(QCoreApplication.translate("UGMM", u"Archivo", None))
        self.menuView.setTitle(QCoreApplication.translate("UGMM", u"Ver", None))
        self.menuHelp.setTitle(QCoreApplication.translate("UGMM", u"Ayuda", None))
        self.menuModelos.setTitle(QCoreApplication.translate("UGMM", u"Configuraci\u00f3n", None))
        self.menuResultados.setTitle(QCoreApplication.translate("UGMM", u"Resultados", None))
    # retranslateUi

