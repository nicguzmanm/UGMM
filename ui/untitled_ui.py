# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_UGMM(object):
    def setupUi(self, UGMM):
        if not UGMM.objectName():
            UGMM.setObjectName(u"UGMM")
        UGMM.resize(966, 630)
        UGMM.setMaximumSize(QSize(16777215, 12777215))
        UGMM.setLayoutDirection(Qt.LeftToRight)
        UGMM.setStyleSheet(u"QFrame {\n"
"	color=rgb(222, 222, 222)\n"
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
        self.actionSimulation_Results = QAction(UGMM)
        self.actionSimulation_Results.setObjectName(u"actionSimulation_Results")
        self.actionModelo_de_fragmentacion = QAction(UGMM)
        self.actionModelo_de_fragmentacion.setObjectName(u"actionModelo_de_fragmentacion")
        self.actionModelo_de_Esfuerzo = QAction(UGMM)
        self.actionModelo_de_Esfuerzo.setObjectName(u"actionModelo_de_Esfuerzo")
        self.centralwidget = QWidget(UGMM)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 12777215))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 281, 571))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(211, 211, 211)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 261, 551))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.simButton = QPushButton(self.gridLayoutWidget_4)
        self.simButton.setObjectName(u"simButton")

        self.gridLayout_4.addWidget(self.simButton, 0, 0, 1, 1, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.gridLayoutWidget_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout_4.addWidget(self.progressBar, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 7, 0, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_5.addWidget(self.checkBox, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.gridLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.inputMVC = QLineEdit(self.gridLayoutWidget_4)
        self.inputMVC.setObjectName(u"inputMVC")

        self.gridLayout_3.addWidget(self.inputMVC, 3, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.inputperiod = QLineEdit(self.gridLayoutWidget_4)
        self.inputperiod.setObjectName(u"inputperiod")

        self.gridLayout_3.addWidget(self.inputperiod, 4, 1, 1, 1)

        self.inputN = QLineEdit(self.gridLayoutWidget_4)
        self.inputN.setObjectName(u"inputN")

        self.gridLayout_3.addWidget(self.inputN, 2, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 2, Qt.AlignHCenter)


        self.gridLayout_5.addLayout(self.gridLayout_3, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dpName = QLineEdit(self.gridLayoutWidget_4)
        self.dpName.setObjectName(u"dpName")
        self.dpName.setEnabled(False)

        self.gridLayout_2.addWidget(self.dpName, 2, 1, 1, 1)

        self.toolButton_3 = QToolButton(self.gridLayoutWidget_4)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setEnabled(False)

        self.gridLayout_2.addWidget(self.toolButton_3, 3, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 3, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.bmName = QLineEdit(self.gridLayoutWidget_4)
        self.bmName.setObjectName(u"bmName")
        self.bmName.setEnabled(False)

        self.gridLayout_2.addWidget(self.bmName, 1, 1, 1, 1)

        self.dpImportButton = QToolButton(self.gridLayoutWidget_4)
        self.dpImportButton.setObjectName(u"dpImportButton")

        self.gridLayout_2.addWidget(self.dpImportButton, 2, 2, 1, 1)

        self.bmImportButton = QToolButton(self.gridLayoutWidget_4)
        self.bmImportButton.setObjectName(u"bmImportButton")

        self.gridLayout_2.addWidget(self.bmImportButton, 1, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_4)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1, Qt.AlignLeft)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_5.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(300, 10, 651, 191))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.horizontalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(211, 211, 211)\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 671, 171))

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(300, 210, 651, 371))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(223, 223, 223)\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 651, 371))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 5, 0, 0)
        self.graphicsView = QGraphicsView(self.gridLayoutWidget_5)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 1, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        UGMM.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UGMM)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 966, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuModelos = QMenu(self.menubar)
        self.menuModelos.setObjectName(u"menuModelos")
        UGMM.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UGMM)
        self.statusbar.setObjectName(u"statusbar")
        UGMM.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuModelos.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.bmMenubar)
        self.menuFile.addAction(self.dpMenubar)
        self.menuFile.addAction(self.actionImport_File)
        self.menuView.addAction(self.actionSimulation_Results)
        self.menuHelp.addAction(self.actionAun_nada)
        self.menuModelos.addAction(self.actionModelo_de_fragmentacion)
        self.menuModelos.addAction(self.actionModelo_de_Esfuerzo)

        self.retranslateUi(UGMM)

        QMetaObject.connectSlotsByName(UGMM)
    # setupUi

    def retranslateUi(self, UGMM):
        UGMM.setWindowTitle(QCoreApplication.translate("UGMM", u"MainWindow", None))
        self.bmMenubar.setText(QCoreApplication.translate("UGMM", u"Importar Modelo de bloques", None))
        self.dpMenubar.setText(QCoreApplication.translate("UGMM", u"Importar Puntos de extraccion", None))
        self.actionImport_File.setText(QCoreApplication.translate("UGMM", u"Importar Plan de extraccion", None))
        self.actionAun_nada.setText(QCoreApplication.translate("UGMM", u"Sobre", None))
        self.actionSimulation_Results.setText(QCoreApplication.translate("UGMM", u"Resultados de simulacion", None))
        self.actionModelo_de_fragmentacion.setText(QCoreApplication.translate("UGMM", u"Modelo de fragmentacion", None))
        self.actionModelo_de_Esfuerzo.setText(QCoreApplication.translate("UGMM", u"Modelo de Esfuerzo", None))
        self.simButton.setText(QCoreApplication.translate("UGMM", u"Correr", None))
        self.checkBox.setText(QCoreApplication.translate("UGMM", u"Modelo de Fragmentacion", None))
        self.label_7.setText(QCoreApplication.translate("UGMM", u"Ingresar Periodo", None))
        self.label_6.setText(QCoreApplication.translate("UGMM", u"Ingresar MVC", None))
        self.label_5.setText(QCoreApplication.translate("UGMM", u"Ingresar N", None))
        self.label_8.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Parametros</span></p></body></html>", None))
        self.toolButton_3.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.label_4.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Archivos</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("UGMM", u"Plan de extraccion", None))
        self.dpImportButton.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.bmImportButton.setText(QCoreApplication.translate("UGMM", u"...", None))
        self.label.setText(QCoreApplication.translate("UGMM", u"Modelo de Bloque", None))
        self.label_2.setText(QCoreApplication.translate("UGMM", u"Punto de Extraccion", None))
        self.checkBox_2.setText(QCoreApplication.translate("UGMM", u"Modelo de Esfuerzo", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UGMM", u"Periodo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UGMM", u"\u03c3v promedio", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UGMM", u"Tonelaje", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UGMM", u"Ley", None));
        self.label_9.setText(QCoreApplication.translate("UGMM", u"<html><head/><body><p><span style=\" font-weight:600;\">Grafica</span></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("UGMM", u"Archivo", None))
        self.menuView.setTitle(QCoreApplication.translate("UGMM", u"Vista", None))
        self.menuHelp.setTitle(QCoreApplication.translate("UGMM", u"Ayuda", None))
        self.menuModelos.setTitle(QCoreApplication.translate("UGMM", u"Modelos", None))
    # retranslateUi

