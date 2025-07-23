# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

from superqt.sliders import QRangeSlider

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1037, 627)
        icon = QIcon()
        icon.addFile(u"../assets/dark_UGMM.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet(u"*{\n"
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
        self.bmMenubar = QAction(main_window)
        self.bmMenubar.setObjectName(u"bmMenubar")
        self.dpMenubar = QAction(main_window)
        self.dpMenubar.setObjectName(u"dpMenubar")
        self.actionImportar_Plan_de_Extracci_n = QAction(main_window)
        self.actionImportar_Plan_de_Extracci_n.setObjectName(u"actionImportar_Plan_de_Extracci_n")
        self.salida = QAction(main_window)
        self.salida.setObjectName(u"salida")
        self.result_folders = QAction(main_window)
        self.result_folders.setObjectName(u"result_folders")
        self.viewer = QAction(main_window)
        self.viewer.setObjectName(u"viewer")
        self.Ver_Resultados_de_Simulacion = QAction(main_window)
        self.Ver_Resultados_de_Simulacion.setObjectName(u"Ver_Resultados_de_Simulacion")
        self.config = QAction(main_window)
        self.config.setObjectName(u"config")
        self.actionManual_de_Usuario = QAction(main_window)
        self.actionManual_de_Usuario.setObjectName(u"actionManual_de_Usuario")
        self.actionAcerca_de = QAction(main_window)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(340, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dpImportButton = QToolButton(self.frame)
        self.dpImportButton.setObjectName(u"dpImportButton")

        self.gridLayout.addWidget(self.dpImportButton, 2, 2, 1, 1)

        self.toolButton_3 = QToolButton(self.frame)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.gridLayout.addWidget(self.toolButton_3, 3, 2, 1, 1)

        self.bmImportButton = QToolButton(self.frame)
        self.bmImportButton.setObjectName(u"bmImportButton")

        self.gridLayout.addWidget(self.bmImportButton, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dpName = QLineEdit(self.frame)
        self.dpName.setObjectName(u"dpName")

        self.gridLayout.addWidget(self.dpName, 2, 1, 1, 1)

        self.bmName = QLineEdit(self.frame)
        self.bmName.setObjectName(u"bmName")

        self.gridLayout.addWidget(self.bmName, 1, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.showsimruta = QLineEdit(self.frame)
        self.showsimruta.setObjectName(u"showsimruta")

        self.gridLayout.addWidget(self.showsimruta, 4, 1, 1, 1)

        self.salida_button = QToolButton(self.frame)
        self.salida_button.setObjectName(u"salida_button")

        self.gridLayout.addWidget(self.salida_button, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(340, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 2)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 0))

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.inputMVC = QLineEdit(self.frame_3)
        self.inputMVC.setObjectName(u"inputMVC")

        self.gridLayout_3.addWidget(self.inputMVC, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 0))

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.inputN = QLineEdit(self.frame_3)
        self.inputN.setObjectName(u"inputN")

        self.gridLayout_3.addWidget(self.inputN, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(340, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-weight: bold;")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 2)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 7, 0, 1, 2)

        self.stress_model = QCheckBox(self.frame_4)
        self.stress_model.setObjectName(u"stress_model")
        self.stress_model.setEnabled(False)

        self.gridLayout_4.addWidget(self.stress_model, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.simButton = QPushButton(self.frame_4)
        self.simButton.setObjectName(u"simButton")
        self.simButton.setMinimumSize(QSize(90, 25))
        self.simButton.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.simButton)

        self.stop = QPushButton(self.frame_4)
        self.stop.setObjectName(u"stop")
        self.stop.setEnabled(False)
        self.stop.setMinimumSize(QSize(90, 25))
        self.stop.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.stop)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)

        self.frag_model = QCheckBox(self.frame_4)
        self.frag_model.setObjectName(u"frag_model")
        self.frag_model.setEnabled(False)

        self.gridLayout_4.addWidget(self.frag_model, 3, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.extrbox = QComboBox(self.tab)
        self.extrbox.setObjectName(u"extrbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.extrbox.sizePolicy().hasHeightForWidth())
        self.extrbox.setSizePolicy(sizePolicy1)
        self.extrbox.setMinimumSize(QSize(150, 0))

        self.gridLayout_5.addWidget(self.extrbox, 0, 1, 1, 1)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)

        self.graphx = QCheckBox(self.tab)
        self.graphx.setObjectName(u"graphx")

        self.gridLayout_5.addWidget(self.graphx, 2, 0, 1, 1)

        self.cortex = QSlider(self.tab)
        self.cortex.setObjectName(u"cortex")
        self.cortex.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.cortex, 2, 1, 1, 1)

        self.update_axex = QLineEdit(self.tab)
        self.update_axex.setObjectName(u"update_axex")
        self.update_axex.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.update_axex, 2, 2, 1, 1)

        self.cat = QComboBox(self.tab)
        self.cat.setObjectName(u"cat")
        sizePolicy1.setHeightForWidth(self.cat.sizePolicy().hasHeightForWidth())
        self.cat.setSizePolicy(sizePolicy1)
        self.cat.setMinimumSize(QSize(150, 0))

        self.gridLayout_5.addWidget(self.cat, 1, 1, 1, 1)

        self.graphy = QCheckBox(self.tab)
        self.graphy.setObjectName(u"graphy")

        self.gridLayout_5.addWidget(self.graphy, 3, 0, 1, 1)

        self.cortey = QSlider(self.tab)
        self.cortey.setObjectName(u"cortey")
        self.cortey.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.cortey, 3, 1, 1, 1)

        self.update_axey = QLineEdit(self.tab)
        self.update_axey.setObjectName(u"update_axey")
        self.update_axey.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.update_axey, 3, 2, 1, 1)

        self.graphz = QCheckBox(self.tab)
        self.graphz.setObjectName(u"graphz")

        self.gridLayout_5.addWidget(self.graphz, 4, 0, 1, 1)

        self.cortez = QSlider(self.tab)
        self.cortez.setObjectName(u"cortez")
        self.cortez.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.cortez, 4, 1, 1, 1)

        self.update_axez = QLineEdit(self.tab)
        self.update_axez.setObjectName(u"update_axez")
        sizePolicy1.setHeightForWidth(self.update_axez.sizePolicy().hasHeightForWidth())
        self.update_axez.setSizePolicy(sizePolicy1)
        self.update_axez.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.update_axez, 4, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.grapher = QPushButton(self.tab)
        self.grapher.setObjectName(u"grapher")
        self.grapher.setMinimumSize(QSize(90, 25))
        self.grapher.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.grapher)

        self.gif = QPushButton(self.tab)
        self.gif.setObjectName(u"gif")
        self.gif.setMinimumSize(QSize(90, 25))
        self.gif.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.gif)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.graphlayout2d = QGraphicsView(self.tab)
        self.graphlayout2d.setObjectName(u"graphlayout2d")

        self.verticalLayout_2.addWidget(self.graphlayout2d)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(100, 0))

        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.tab_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setMinimumSize(QSize(150, 0))

        self.gridLayout_6.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 1, 0, 1, 1)

        self.horizontalSlider_4 = QRangeSlider(self.tab_2)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_4, 2, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.tab_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_6.addWidget(self.lineEdit_12, 2, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.tab_2)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy1.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy1)
        self.comboBox_4.setMinimumSize(QSize(150, 0))

        self.gridLayout_6.addWidget(self.comboBox_4, 1, 1, 1, 1)

        self.horizontalSlider_5 = QRangeSlider(self.tab_2)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_5, 3, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_6.addWidget(self.lineEdit_13, 3, 2, 1, 1)

        self.horizontalSlider_6 = QRangeSlider(self.tab_2)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_6, 4, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.tab_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy1.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy1)
        self.lineEdit_14.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_6.addWidget(self.lineEdit_14, 4, 2, 1, 1)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 4, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.view3d = QPushButton(self.tab_2)
        self.view3d.setObjectName(u"view3d")
        self.view3d.setMinimumSize(QSize(90, 25))
        self.view3d.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.view3d)

        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(90, 25))
        self.pushButton_6.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.graphicsView_2 = QGraphicsView(self.tab_2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_3.addWidget(self.graphicsView_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuResultados = QMenu(self.menubar)
        self.menuResultados.setObjectName(u"menuResultados")
        self.menuConfiguraci_n = QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName(u"menuConfiguraci_n")
        self.menuAyud = QMenu(self.menubar)
        self.menuAyud.setObjectName(u"menuAyud")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuResultados.menuAction())
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())
        self.menubar.addAction(self.menuAyud.menuAction())
        self.menuArchivo.addAction(self.bmMenubar)
        self.menuArchivo.addAction(self.dpMenubar)
        self.menuArchivo.addAction(self.actionImportar_Plan_de_Extracci_n)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.salida)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.result_folders)
        self.menuVer.addAction(self.viewer)
        self.menuResultados.addAction(self.Ver_Resultados_de_Simulacion)
        self.menuConfiguraci_n.addAction(self.config)
        self.menuAyud.addAction(self.actionManual_de_Usuario)
        self.menuAyud.addAction(self.actionAcerca_de)

        self.retranslateUi(main_window)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"UGMM - Gravity Flow Module", None))
        self.bmMenubar.setText(QCoreApplication.translate("main_window", u"Importar Modelo de Bloques", None))
        self.dpMenubar.setText(QCoreApplication.translate("main_window", u"Importar Puntos de Extracci\u00f3n", None))
        self.actionImportar_Plan_de_Extracci_n.setText(QCoreApplication.translate("main_window", u"Importar Plan de Extracci\u00f3n", None))
        self.salida.setText(QCoreApplication.translate("main_window", u"Seleccionar Ruta de Salida", None))
        self.result_folders.setText(QCoreApplication.translate("main_window", u"Ver Carpeta de Simulaciones", None))
        self.viewer.setText(QCoreApplication.translate("main_window", u"Visualizador de Simulaci\u00f3n", None))
        self.Ver_Resultados_de_Simulacion.setText(QCoreApplication.translate("main_window", u"Ver Resultados de Simulaci\u00f3n", None))
        self.config.setText(QCoreApplication.translate("main_window", u"Ajustes de Visualizaci\u00f3n", None))
        self.actionManual_de_Usuario.setText(QCoreApplication.translate("main_window", u"Manual de Usuario", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("main_window", u"Acerca de", None))
        self.dpImportButton.setText(QCoreApplication.translate("main_window", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("main_window", u"...", None))
        self.bmImportButton.setText(QCoreApplication.translate("main_window", u"...", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Modelo de bloques", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"Plan de extracci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Puntos de extracci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Archivos y directorios:", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"Ruta de salida", None))
        self.salida_button.setText(QCoreApplication.translate("main_window", u"...", None))
        self.label_6.setText(QCoreApplication.translate("main_window", u"Par\u00e1metros del modelo:", None))
        self.label_7.setText(QCoreApplication.translate("main_window", u"Constante N", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"Constante MVC", None))
        self.label_12.setText(QCoreApplication.translate("main_window", u"Simulaci\u00f3n:", None))
        self.stress_model.setText(QCoreApplication.translate("main_window", u"Modelo de Esfuerzo", None))
        self.simButton.setText(QCoreApplication.translate("main_window", u"Simular", None))
        self.stop.setText(QCoreApplication.translate("main_window", u"Detener", None))
        self.frag_model.setText(QCoreApplication.translate("main_window", u"Modelo de Fragmentaci\u00f3n", None))
        self.label_13.setText(QCoreApplication.translate("main_window", u"Periodo", None))
        self.label_14.setText(QCoreApplication.translate("main_window", u"Categor\u00eda", None))
        self.graphx.setText(QCoreApplication.translate("main_window", u"Eje X", None))
        self.graphy.setText(QCoreApplication.translate("main_window", u"Eje Y", None))
        self.graphz.setText(QCoreApplication.translate("main_window", u"Eje Z", None))
        self.grapher.setText(QCoreApplication.translate("main_window", u"Graficar", None))
        self.gif.setText(QCoreApplication.translate("main_window", u"Animaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_window", u"Vista 2D", None))
        self.label_15.setText(QCoreApplication.translate("main_window", u"Periodo", None))
        self.label_16.setText(QCoreApplication.translate("main_window", u"Categor\u00eda", None))
        self.label_17.setText(QCoreApplication.translate("main_window", u"Eje X", None))
        self.label_18.setText(QCoreApplication.translate("main_window", u"Eje Y", None))
        self.label_19.setText(QCoreApplication.translate("main_window", u"Eje Z", None))
        self.view3d.setText(QCoreApplication.translate("main_window", u"Graficar", None))
        self.pushButton_6.setText(QCoreApplication.translate("main_window", u"Animaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main_window", u"Vista 3D", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("main_window", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("main_window", u"Ver", None))
        self.menuResultados.setTitle(QCoreApplication.translate("main_window", u"Resultados", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("main_window", u"Configuraci\u00f3n", None))
        self.menuAyud.setTitle(QCoreApplication.translate("main_window", u"Ayuda", None))
    # retranslateUi

