from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtCore import pyqtSignal


class Configuration(QtWidgets.QDialog):

    config_finished = pyqtSignal(str, str, str, str, int, int, bool)

    def __init__(self, col1_2d, col2_2d, col1_3d, col2_3d, size2d, size3d):
        super().__init__()

        
        uic.loadUi('ui\\Configuracion.ui', self)
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))
        self.setWindowTitle('Resultados de Simulación')

        self.butcol1_2d.clicked.connect(lambda: self.seleccionar_color(self.butcol1_2d, "col1_2d"))
        self.butcol2_2d.clicked.connect(lambda: self.seleccionar_color(self.butcol2_2d, "col2_2d"))
        self.butcol1_3d.clicked.connect(lambda: self.seleccionar_color(self.butcol1_3d, "col1_3d"))
        self.butcol2_3d.clicked.connect(lambda: self.seleccionar_color(self.butcol2_3d, "col2_3d"))

        self.linesize2d.setValidator(QIntValidator(1, 100))
        self.linesize3d.setValidator(QIntValidator(1, 100))

        self.save.accepted.connect(self.save_config)

        self.col1_2d = col1_2d
        self.col2_2d = col2_2d
        self.col1_3d = col1_3d
        self.col2_3d = col2_3d

        self.size2d = size2d
        self.size3d = size3d
        
        self.emitsize2d = size2d
        self.emitsize3d = size3d

        self.butcol1_2d.setStyleSheet(f"background-color: {col1_2d}") 
        self.butcol2_2d.setStyleSheet(f"background-color: {col2_2d}") 
        self.butcol1_3d.setStyleSheet(f"background-color: {col1_3d}") 
        self.butcol2_3d.setStyleSheet(f"background-color: {col2_3d}")

        self.sizelist2d.itemClicked.connect(self.on_item_clicked2d)
        self.sizelist3d.itemClicked.connect(self.on_item_clicked3d)

        self.linesize2d.setText(str(self.size2d))
        self.linesize3d.setText(str(self.size3d))        

    def seleccionar_color(self, button, color_attr):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            button.setStyleSheet(f"background-color: {color.name()}")
            setattr(self, color_attr, color.name()) 
    
    def on_item_clicked2d(self, item):
        self.linesize2d.setText(item.text())
    
    def on_item_clicked3d(self, item):
        self.linesize3d.setText(item.text())

    def save_config(self):
        try:
            if self.linesize2d.text() == "":
                self.emitsize2d = self.size2d
            elif int(self.linesize2d.text()) != self.size2d:
                self.emitsize2d = int(self.linesize2d.text())

            if self.linesize3d.text() == "":
                self.emitsize3d = self.size3d
            elif int(self.linesize3d.text()) != self.size3d:
                self.emitsize3d = int(self.linesize3d.text())

            self.config_finished.emit(self.col1_2d, self.col2_2d, self.col1_3d, self.col2_3d, 
                                      self.emitsize2d, self.emitsize3d, True)
            self.accept()

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese un número válido en los tamaños.")
