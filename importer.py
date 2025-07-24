from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal
import os

class Importbm(QtWidgets.QDialog):

    imported = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi('ui\\Importbm.ui', self)
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))
        self.setWindowTitle('Importar modelo de bloques...')

        self.searchbm.clicked.connect(self.select_file)
        
        self.aceptar.clicked.connect(self.emit_ruta)
        self.cancel.clicked.connect(self.back)

    def select_file(self):
        self.ruta, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Seleccionar archivo de puntos de extracción', '', 'CSV Files (*.csv);; Excel Files (*.xlsx);; Text Files (*.txt);; All files (*)'
        )
        if self.ruta:
            self.bmname.setText(f'{self.ruta}')

    def emit_ruta(self):

        self.imported.emit(self.ruta)
        self.accept()
    
    def back(self):
        self.accept()