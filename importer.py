from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal
import pandas as pd
import os

class Importbm(QtWidgets.QDialog):

    imported = pyqtSignal(str)
    delimitadores = {
        0: ",",
        1: ".",
        2: ";",
        3: "\t"
    }
    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi('ui\\Importbm.ui', self)
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))
        self.setWindowTitle('Importar modelo de bloques...')
        self.bmname.setReadOnly(True)
        
        self.searchbm.clicked.connect(self.select_file)
        self.load.clicked.connect(self.cargar_bm)
        self.aceptar.clicked.connect(self.emit_ruta)
        self.cancel.clicked.connect(self.back)
        self.valx.setEnabled(False)
        self.valy.setEnabled(False)
        self.valz.setEnabled(False)
        self.setup_connections()

    def select_file(self):
        self.ruta, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Seleccionar archivo de puntos de extracción', '', 'CSV Files (*.csv);; Excel Files (*.xlsx);; Text Files (*.txt);; All files (*)'
        )
        if self.ruta:
            self.bmname.setText(f'{self.ruta}')
            
    def cargar_bm(self):
        header = pd.read_csv(self.ruta, nrows=0,sep=f"{self.delimitadores[self.sepbox.currentIndex()]}")
        header = list(header.columns)
        header.append("[Columna no disponible]")

        self.catx.clear()
        self.caty.clear()
        self.catz.clear()
        self.catley.clear()
        self.catdens.clear()

        self.catx.addItems(header)
        self.caty.addItems(header)
        self.catz.addItems(header)
        self.catley.addItems(header)
        self.catdens.addItems(header)

    def setup_connections(self):
        self.catx.currentIndexChanged.connect(self.on_combo_changed)
        self.caty.currentIndexChanged.connect(self.on_combo_changed)
        self.catz.currentIndexChanged.connect(self.on_combo_changed)
        self.catley.currentIndexChanged.connect(self.on_combo_changed)
        self.catdens.currentIndexChanged.connect(self.on_combo_changed)

    def on_combo_changed(self, index):
        combo = self.sender()

        if combo == self.catx:
            self.valx.setEnabled(index == combo.count() - 1)
        elif combo == self.caty:
            self.valy.setEnabled(index == combo.count() - 1)
        elif combo == self.catz:
            self.valz.setEnabled(index == combo.count() - 1)
        elif combo == self.catley:
            self.valley.setEnabled(index == combo.count() - 1)
        elif combo == self.catdens:
            self.valdens.setEnabled(index == combo.count() - 1)

    def emit_ruta(self):

        self.imported.emit(self.ruta)
        self.accept()
    
    def back(self):
        self.accept()