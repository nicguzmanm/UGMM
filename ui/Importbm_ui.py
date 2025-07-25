# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Importbm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(576, 385)
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
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.load = QPushButton(Dialog)
        self.load.setObjectName(u"load")

        self.gridLayout.addWidget(self.load, 3, 5, 1, 1)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.cancel, 13, 5, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.valdens = QLineEdit(Dialog)
        self.valdens.setObjectName(u"valdens")
        self.valdens.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valdens.sizePolicy().hasHeightForWidth())
        self.valdens.setSizePolicy(sizePolicy)
        self.valdens.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.valdens, 11, 3, 1, 3)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.sepbox = QComboBox(Dialog)
        self.sepbox.addItem("")
        self.sepbox.addItem("")
        self.sepbox.addItem("")
        self.sepbox.addItem("")
        self.sepbox.setObjectName(u"sepbox")
        sizePolicy.setHeightForWidth(self.sepbox.sizePolicy().hasHeightForWidth())
        self.sepbox.setSizePolicy(sizePolicy)
        self.sepbox.setMinimumSize(QSize(90, 0))
        self.sepbox.setInsertPolicy(QComboBox.InsertAfterCurrent)

        self.gridLayout.addWidget(self.sepbox, 1, 1, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.caty = QComboBox(Dialog)
        self.caty.setObjectName(u"caty")

        self.gridLayout.addWidget(self.caty, 8, 1, 1, 2)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.aceptar = QPushButton(Dialog)
        self.aceptar.setObjectName(u"aceptar")
        self.aceptar.setMinimumSize(QSize(110, 0))

        self.gridLayout.addWidget(self.aceptar, 13, 3, 1, 2)

        self.catz = QComboBox(Dialog)
        self.catz.setObjectName(u"catz")

        self.gridLayout.addWidget(self.catz, 9, 1, 1, 2)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 11, 0, 1, 1)

        self.catdens = QComboBox(Dialog)
        self.catdens.setObjectName(u"catdens")

        self.gridLayout.addWidget(self.catdens, 11, 1, 1, 2)

        self.catley = QComboBox(Dialog)
        self.catley.setObjectName(u"catley")

        self.gridLayout.addWidget(self.catley, 10, 1, 1, 2)

        self.valz = QLineEdit(Dialog)
        self.valz.setObjectName(u"valz")
        self.valz.setEnabled(False)
        sizePolicy.setHeightForWidth(self.valz.sizePolicy().hasHeightForWidth())
        self.valz.setSizePolicy(sizePolicy)
        self.valz.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.valz, 9, 3, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 6)

        self.searchbm = QToolButton(Dialog)
        self.searchbm.setObjectName(u"searchbm")

        self.gridLayout.addWidget(self.searchbm, 0, 4, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_10, 6, 3, 1, 2)

        self.bmname = QLineEdit(Dialog)
        self.bmname.setObjectName(u"bmname")
        self.bmname.setEnabled(True)

        self.gridLayout.addWidget(self.bmname, 0, 1, 1, 3)

        self.catx = QComboBox(Dialog)
        self.catx.setObjectName(u"catx")

        self.gridLayout.addWidget(self.catx, 7, 1, 1, 2)

        self.valley = QLineEdit(Dialog)
        self.valley.setObjectName(u"valley")
        self.valley.setEnabled(False)
        sizePolicy.setHeightForWidth(self.valley.sizePolicy().hasHeightForWidth())
        self.valley.setSizePolicy(sizePolicy)
        self.valley.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.valley, 10, 3, 1, 3)

        self.valy = QLineEdit(Dialog)
        self.valy.setObjectName(u"valy")
        self.valy.setEnabled(False)
        sizePolicy.setHeightForWidth(self.valy.sizePolicy().hasHeightForWidth())
        self.valy.setSizePolicy(sizePolicy)
        self.valy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.valy, 8, 3, 1, 3)

        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)

        self.valx = QLineEdit(Dialog)
        self.valx.setObjectName(u"valx")
        self.valx.setEnabled(False)
        sizePolicy.setHeightForWidth(self.valx.sizePolicy().hasHeightForWidth())
        self.valx.setSizePolicy(sizePolicy)
        self.valx.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.valx, 7, 3, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 12, 0, 1, 6)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.load.setText(QCoreApplication.translate("Dialog", u"Cargar", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Encabezado", None))
        self.valdens.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Categoria", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Separador", None))
        self.sepbox.setItemText(0, QCoreApplication.translate("Dialog", u",", None))
        self.sepbox.setItemText(1, QCoreApplication.translate("Dialog", u".", None))
        self.sepbox.setItemText(2, QCoreApplication.translate("Dialog", u";", None))
        self.sepbox.setItemText(3, QCoreApplication.translate("Dialog", u"tabulaci\u00f3n", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Ruta del modelo", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Ley", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Coordenada Y", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Si", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Coordenada X", None))
        self.aceptar.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Coordenada Z", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Densidad", None))
        self.valz.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.searchbm.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Valores default", None))
        self.valley.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.valy.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.valx.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

