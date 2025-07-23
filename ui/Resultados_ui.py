# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Resultados.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(522, 381)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 501, 361))
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
        self.tableresult = QTableWidget(self.frame_2)
        if (self.tableresult.columnCount() < 4):
            self.tableresult.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableresult.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableresult.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableresult.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableresult.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableresult.setObjectName(u"tableresult")
        self.tableresult.setGeometry(QRect(10, 10, 481, 341))
        self.tableresult.setLayoutDirection(Qt.LeftToRight)
        self.tableresult.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableresult.setTextElideMode(Qt.ElideMiddle)
        self.tableresult.setShowGrid(True)
        self.tableresult.horizontalHeader().setDefaultSectionSize(120)

        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.tableresult.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Extracci\u00f3n", None));
        ___qtablewidgetitem1 = self.tableresult.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u03c3\u1d65\n"
"promedio [MPa]", None));
        ___qtablewidgetitem2 = self.tableresult.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Tonelaje [Ton]", None));
        ___qtablewidgetitem3 = self.tableresult.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Ley [%]", None));
    # retranslateUi

