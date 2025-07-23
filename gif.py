from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QIcon

class GifDialog(QtWidgets.QDialog):
    """ Pestaña que muestra la animación de las extracciones """

    def __init__(self, gif_path):
        super().__init__()

        # Configura la ventana
        self.setWindowTitle("Animación de Extracciones")
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))
        self.setGeometry(100, 100, 300, 350)

        # Crear un QLabel para mostrar el GIF
        self.label = QtWidgets.QLabel(self)
        self.save = QtWidgets.QLabel(self)
        self.save.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.save.setWordWrap(True) 

        # Cargar el GIF usando QMovie
        movie = QtGui.QMovie(gif_path)
        self.label.setMovie(movie)

        # Iniciar la animación
        movie.start()

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.save)  # Agregar QLabel para la ruta
        self.setLayout(layout)

    def set_save_path(self, save_path):
        """ Método para actualizar la etiqueta con la ruta donde se guardó """

        self.save.setText(f"Gif guardado en: {save_path}")