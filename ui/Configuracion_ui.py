# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Configuracion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(457, 448)
        Dialog.setStyleSheet(u"*{\n"
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
        self.save = QDialogButtonBox(Dialog)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(20, 410, 411, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        self.save.setOrientation(Qt.Horizontal)
        self.save.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 9, 431, 391))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 411, 371))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 394, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sizelist2d = QListWidget(self.verticalLayoutWidget)
        __qlistwidgetitem = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem5 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem6 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem7 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem8 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem9 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem10 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem11 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem12 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem13 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem14 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem15 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem16 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem17 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem18 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem19 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem20 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem21 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem22 = QListWidgetItem(self.sizelist2d)
        __qlistwidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.sizelist2d.setObjectName(u"sizelist2d")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizelist2d.sizePolicy().hasHeightForWidth())
        self.sizelist2d.setSizePolicy(sizePolicy1)
        self.sizelist2d.setMaximumSize(QSize(70, 140))

        self.gridLayout.addWidget(self.sizelist2d, 4, 2, 1, 2, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 4)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 4, Qt.AlignLeft)

        self.linesize2d = QLineEdit(self.verticalLayoutWidget)
        self.linesize2d.setObjectName(u"linesize2d")
        sizePolicy1.setHeightForWidth(self.linesize2d.sizePolicy().hasHeightForWidth())
        self.linesize2d.setSizePolicy(sizePolicy1)
        self.linesize2d.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.linesize2d, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 4)

        self.butcol1_2d = QPushButton(self.verticalLayoutWidget)
        self.butcol1_2d.setObjectName(u"butcol1_2d")
        sizePolicy1.setHeightForWidth(self.butcol1_2d.sizePolicy().hasHeightForWidth())
        self.butcol1_2d.setSizePolicy(sizePolicy1)
        self.butcol1_2d.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.butcol1_2d, 2, 1, 1, 1)

        self.butcol2_2d = QPushButton(self.verticalLayoutWidget)
        self.butcol2_2d.setObjectName(u"butcol2_2d")
        sizePolicy1.setHeightForWidth(self.butcol2_2d.sizePolicy().hasHeightForWidth())
        self.butcol2_2d.setSizePolicy(sizePolicy1)
        self.butcol2_2d.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.butcol2_2d, 2, 2, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1, Qt.AlignRight)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 0, 2, 4)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 394, 321))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.butcol2_3d = QPushButton(self.verticalLayoutWidget_2)
        self.butcol2_3d.setObjectName(u"butcol2_3d")
        sizePolicy1.setHeightForWidth(self.butcol2_3d.sizePolicy().hasHeightForWidth())
        self.butcol2_3d.setSizePolicy(sizePolicy1)
        self.butcol2_3d.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.butcol2_3d, 2, 2, 1, 1)

        self.butcol1_3d = QPushButton(self.verticalLayoutWidget_2)
        self.butcol1_3d.setObjectName(u"butcol1_3d")
        sizePolicy1.setHeightForWidth(self.butcol1_3d.sizePolicy().hasHeightForWidth())
        self.butcol1_3d.setSizePolicy(sizePolicy1)
        self.butcol1_3d.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.butcol1_3d, 2, 1, 1, 1)

        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1, Qt.AlignRight)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1, Qt.AlignRight)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 3, 0, 1, 4)

        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 4, Qt.AlignLeft)

        self.linesize3d = QLineEdit(self.verticalLayoutWidget_2)
        self.linesize3d.setObjectName(u"linesize3d")
        sizePolicy1.setHeightForWidth(self.linesize3d.sizePolicy().hasHeightForWidth())
        self.linesize3d.setSizePolicy(sizePolicy1)
        self.linesize3d.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.linesize3d, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 1, 0, 1, 4)

        self.sizelist3d = QListWidget(self.verticalLayoutWidget_2)
        __qlistwidgetitem23 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem24 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem25 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem26 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem27 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem28 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem29 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem30 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem31 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem32 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem33 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem34 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem35 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem36 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem37 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem38 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem39 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem40 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem41 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem42 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem43 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem43.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem44 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem44.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem45 = QListWidgetItem(self.sizelist3d)
        __qlistwidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.sizelist3d.setObjectName(u"sizelist3d")
        sizePolicy1.setHeightForWidth(self.sizelist3d.sizePolicy().hasHeightForWidth())
        self.sizelist3d.setSizePolicy(sizePolicy1)
        self.sizelist3d.setMaximumSize(QSize(70, 140))

        self.gridLayout_2.addWidget(self.sizelist3d, 4, 2, 1, 2, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 5, 0, 2, 4)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.frame.raise_()
        self.save.raise_()

        self.retranslateUi(Dialog)
        self.save.accepted.connect(Dialog.accept)
        self.save.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))

        __sortingEnabled = self.sizelist2d.isSortingEnabled()
        self.sizelist2d.setSortingEnabled(False)
        ___qlistwidgetitem = self.sizelist2d.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"6", None));
        ___qlistwidgetitem1 = self.sizelist2d.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"5", None));
        ___qlistwidgetitem2 = self.sizelist2d.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"7", None));
        ___qlistwidgetitem3 = self.sizelist2d.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"8", None));
        ___qlistwidgetitem4 = self.sizelist2d.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"9", None));
        ___qlistwidgetitem5 = self.sizelist2d.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qlistwidgetitem6 = self.sizelist2d.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"11", None));
        ___qlistwidgetitem7 = self.sizelist2d.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"12", None));
        ___qlistwidgetitem8 = self.sizelist2d.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"14", None));
        ___qlistwidgetitem9 = self.sizelist2d.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"16", None));
        ___qlistwidgetitem10 = self.sizelist2d.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"18", None));
        ___qlistwidgetitem11 = self.sizelist2d.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qlistwidgetitem12 = self.sizelist2d.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"22", None));
        ___qlistwidgetitem13 = self.sizelist2d.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"24", None));
        ___qlistwidgetitem14 = self.sizelist2d.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"26", None));
        ___qlistwidgetitem15 = self.sizelist2d.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"28", None));
        ___qlistwidgetitem16 = self.sizelist2d.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"36", None));
        ___qlistwidgetitem17 = self.sizelist2d.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"48", None));
        ___qlistwidgetitem18 = self.sizelist2d.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"72", None));
        ___qlistwidgetitem19 = self.sizelist2d.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Dialog", u"108", None));
        ___qlistwidgetitem20 = self.sizelist2d.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Dialog", u"144", None));
        ___qlistwidgetitem21 = self.sizelist2d.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Dialog", u"288", None));
        ___qlistwidgetitem22 = self.sizelist2d.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Dialog", u"576", None));
        self.sizelist2d.setSortingEnabled(__sortingEnabled)

        self.label_7.setText(QCoreApplication.translate("Dialog", u"Ajustes 2D", None))
        self.butcol1_2d.setText(QCoreApplication.translate("Dialog", u"Color 1", None))
        self.butcol2_2d.setText(QCoreApplication.translate("Dialog", u"Color 2", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Tama\u00f1o de los puntos:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Color de la gr\u00e1fica:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"2D", None))
        self.butcol2_3d.setText(QCoreApplication.translate("Dialog", u"Color 2", None))
        self.butcol1_3d.setText(QCoreApplication.translate("Dialog", u"Color 1", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Tama\u00f1o de los puntos:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Color de la gr\u00e1fica:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Ajustes 3D", None))

        __sortingEnabled1 = self.sizelist3d.isSortingEnabled()
        self.sizelist3d.setSortingEnabled(False)
        ___qlistwidgetitem23 = self.sizelist3d.item(0)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Dialog", u"5", None));
        ___qlistwidgetitem24 = self.sizelist3d.item(1)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Dialog", u"6", None));
        ___qlistwidgetitem25 = self.sizelist3d.item(2)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Dialog", u"7", None));
        ___qlistwidgetitem26 = self.sizelist3d.item(3)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Dialog", u"8", None));
        ___qlistwidgetitem27 = self.sizelist3d.item(4)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Dialog", u"9", None));
        ___qlistwidgetitem28 = self.sizelist3d.item(5)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qlistwidgetitem29 = self.sizelist3d.item(6)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Dialog", u"11", None));
        ___qlistwidgetitem30 = self.sizelist3d.item(7)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Dialog", u"12", None));
        ___qlistwidgetitem31 = self.sizelist3d.item(8)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Dialog", u"14", None));
        ___qlistwidgetitem32 = self.sizelist3d.item(9)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Dialog", u"16", None));
        ___qlistwidgetitem33 = self.sizelist3d.item(10)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Dialog", u"18", None));
        ___qlistwidgetitem34 = self.sizelist3d.item(11)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qlistwidgetitem35 = self.sizelist3d.item(12)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Dialog", u"22", None));
        ___qlistwidgetitem36 = self.sizelist3d.item(13)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Dialog", u"24", None));
        ___qlistwidgetitem37 = self.sizelist3d.item(14)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Dialog", u"26", None));
        ___qlistwidgetitem38 = self.sizelist3d.item(15)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Dialog", u"28", None));
        ___qlistwidgetitem39 = self.sizelist3d.item(16)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Dialog", u"36", None));
        ___qlistwidgetitem40 = self.sizelist3d.item(17)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("Dialog", u"48", None));
        ___qlistwidgetitem41 = self.sizelist3d.item(18)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("Dialog", u"72", None));
        ___qlistwidgetitem42 = self.sizelist3d.item(19)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("Dialog", u"108", None));
        ___qlistwidgetitem43 = self.sizelist3d.item(20)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("Dialog", u"144", None));
        ___qlistwidgetitem44 = self.sizelist3d.item(21)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("Dialog", u"288", None));
        ___qlistwidgetitem45 = self.sizelist3d.item(22)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("Dialog", u"576", None));
        self.sizelist3d.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"3D", None))
    # retranslateUi

