from PyQt6 import QtWidgets, QtGui, QtCore

class SaveDialog(QtWidgets.QDialog):
    cancelSignal = QtCore.pyqtSignal()
    savefile = QtCore.pyqtSignal(list)

    def __init__(self, ext):
        super().__init__()

        self.setWindowTitle("Guardar Archivos")
        self.setWindowIcon(QtGui.QIcon('asset\\dark_UGMM.png'))
        self.setFixedSize(350, 220) 
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowMaximizeButtonHint)
        
        layout = QtWidgets.QVBoxLayout()
        self.ext = ext
        self.label = QtWidgets.QLabel("Seleccione los archivos que desea guardar:")
        layout.addWidget(self.label)

        checkbox_widget = QtWidgets.QWidget()
        checkbox_layout = QtWidgets.QVBoxLayout()

        self.checkboxes = []
        for ext_value in ext:
            cb = QtWidgets.QCheckBox(f"Periodo {ext_value}")
            checkbox_layout.addWidget(cb)
            self.checkboxes.append(cb)

        self.all_cb = QtWidgets.QCheckBox("Todos")
        checkbox_layout.addWidget(self.all_cb)
        self.all_cb.stateChanged.connect(self.select_all)

        checkbox_widget.setLayout(checkbox_layout)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(checkbox_widget)

        layout.addWidget(scroll_area)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok |
                                                    QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.setLayout(layout)

    def select_all(self, state):
        """ Marca o desmarca todos los archivos si se selecciona 'Todos' """
        if self.all_cb.isChecked():
            for cb in self.checkboxes:
                cb.setChecked(True)
        else:
            for cb in self.checkboxes:
                cb.setChecked(False)

    def reject(self):
        """ Emitir la señal cuando se cancela """

        self.cancelSignal.emit()
        super().reject()

    def accept(self):
        """ Emitir la lista a guardar cuando acepta """
        
        save = [None] * len(self.ext)
        index = 0
        for cb in self.checkboxes:
            save[index] = cb.isChecked()
            index += 1
        if sum(save) == 0:
            self.cancelSignal.emit()
            super().reject()
        else:
            self.savefile.emit(save)
            super().accept()