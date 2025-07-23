from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap
import re
import os
import pandas as pd
from gif import GifDialog
from PIL import Image

class Visualizador(QtWidgets.QDialog):
    """ Abre una pestaña para visualizar todas las simulaciones hechas
    tanto como las recientes que ya se guardaron, como las que se hicieron anteriormente """


    def __init__(self, ruta, col1_2d, col2_2d, col1_3d, col2_3d, size2d, size3d):
        super().__init__()
        uic.loadUi('ui\\Visualizador.ui', self)

        self.setWindowTitle('Visualizador de simulaciones')
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))

        self.ruta = ruta
        self.size2d = size2d
        self.size3d = size3d
        self.col1_2d = col1_2d
        self.col2_2d = col2_2d
        self.col1_3d = col1_3d
        self.col2_3d = col2_3d
        self.show_ruta.setText(self.ruta)
        self.show_ruta.setReadOnly(True)

        # Ordenar las carpetas numéricamente
        try:
            self.fold = sorted([name for name in os.listdir(self.ruta) if os.path.isdir(os.path.join(self.ruta, name))], 
                        key=lambda name: int(re.search(r'\d+', name[3:]).group()))
        except (ValueError, FileNotFoundError):
            QtWidgets.QMessageBox.warning(
                self, "Error", "No se ha encontrado ninguna carpeta con el formato 'report', esto se puede deber a que no se han realizado simulaciones en esta carpeta."
            )
            return
        self.browse.clicked.connect(self.browse_file)
        self.folders.clear()
        self.folders.addItems(self.fold)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphlayout.addWidget(self.canvas)

        self.figure3d = plt.figure()
        self.canvas3d = FigureCanvas(self.figure3d)
        self.graphlayout3d.addWidget(self.canvas3d)

        self.save_fold.clicked.connect(self.activate)

        # Guardar los ejes que se quieran graficar
        self.save_graph_axe.clicked.connect(self.ejes)
        self.corte.valueChanged.connect(self.update_value)
        self.grapher.clicked.connect(self.select_graph) # Graficar 2d
        self.grapher3d.clicked.connect(self.graficar3d) # Graficar 3d

        self.gif.clicked.connect(self.giftear)

    def activate(self):
        """ Funcion que ya al haber elegido una carpeta a simular activa los botones
        para elegir la coordenada a graficar y rellena el combo box con las extracciones
        respectivas de la carpeta seleccionada """

        if not self.folders.currentText():
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Porfavor, seleccione la carpeta de la simulacion a visualizar.')
            return
        try:
            self.period = []
            pattern = re.compile(rf'modelo_actualizado_(\d+)\_{os.path.basename(self.folders.currentText())}.csv')
            folder_path = os.path.join(self.ruta, self.folders.currentText())
            
            for filename in os.listdir(folder_path):
                match = pattern.search(filename)
                if match:
                    self.period.append(int(match.group(1)))

            if not self.period:
                QtWidgets.QMessageBox.warning(
                    self, 'Alerta', 'No se ha encontrado el modelo modificado, puede haber sido eliminado o cambiaron su nombre default.'
                )
            else:
                self.period.sort()  # Ordenar valores
                self.extrbox.clear()
                self.graphx.setEnabled(True)
                self.graphy.setEnabled(True)
                self.graphz.setEnabled(True)
                self.save_graph_axe.setEnabled(True)
                self.extrbox.setEnabled(True)
                self.grapher3d.setEnabled(True)

                self.item = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi","period"]
                self.item3d = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi","period"]
                self.cat2dbox.clear()
                self.cat3dbox.clear()
                self.figure.clear()
                self.figure3d.clf()
                self.cat2dbox.addItems(self.item)
                self.cat3dbox.addItems(self.item3d)
                self.cat2dbox.setEnabled(True)
                self.cat3dbox.setEnabled(True)
                
                for i in self.period:
                    self.extrbox.addItem(str(i))

        except (ValueError, FileNotFoundError):
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'No se ha seleccionado ninguna carpeta con el formato simX o la carpeta no existe.'
            )

    def browse_file(self):

        try:
            ruta_seleccionada = QtWidgets.QFileDialog.getExistingDirectory(self, 'Seleccionar la carpeta de la simulación a visualizar.')

            if ruta_seleccionada:  
                self.ruta = ruta_seleccionada
                self.folders.clear()
                self.show_ruta.setText(self.ruta)
                self.show_ruta.setReadOnly(True)

                # Filtrar solo carpetas dentro de la ruta seleccionada
                self.fold = [name for name in os.listdir(self.ruta) if os.path.isdir(os.path.join(self.ruta, name))]

                # Ordenar considerando que las carpetas tienen números en su nombre
                def extract_number(name):
                    match = re.search(r'\d+', name[3:])  # Buscar números en la carpeta después de los primeros 3 caracteres
                    return int(match.group()) if match else float('inf')  # Si no hay número, ponerlo al final

                self.fold = sorted(self.fold, key=extract_number)

                self.folders.addItems(self.fold)
            
            if os.path.basename(self.ruta) != "report":  # Verifica que la carpeta seleccionada sea 'report'
                raise ValueError("Selecciona la carpeta con el nombre 'report'.")

        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, 'Error', str(e))

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error inesperado', f'Ocurrió un error: {str(e)}')

    def ejes(self):
        """ Ver que no esta seleccionado mas de dos ejes a graficar en pestaña 2D """

        self.checkboxes = [self.graphx, self.graphy, self.graphz]
        self.value_axe=[checkbox.isChecked() for checkbox in self.checkboxes]
        num_check = sum(self.value_axe)
        if num_check != 2:
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Seleccionar solo dos ejes de coordenadas a graficar.')
            return
        
            
        self.corte.setEnabled(True)
        self.grapher.setEnabled(True)
        self.update_axe.setEnabled(True)
        self.axe_corte()
    
    def axe_corte(self):
        """ 
        Segun la coordenada elejida se importara el archivo elejido por el usuario y 
        se vera la cota en que se encuentra la coordenada a realizar el corte
        """

        self.coordstepx=2 # Cambiar
        self.coordstepy=2
        self.coordstepz=2
        try:
            self.bmodel=pd.read_csv(rf'{self.ruta}\\{self.folders.currentText()}\\modelo_actualizado_{self.extrbox.currentText()}_{os.path.basename(self.folders.currentText())}.csv')
        except:
            self.corte.setEnabled(False)
            self.grapher.setEnabled(False)
            self.update_axe.setEnabled(False)
            QtWidgets.QMessageBox.critical(self, 'Error', 'La carpeta donde se guardó la simulación reciente ha sido eliminada. Por favor, vuelve a simular para poder visualizar los resultados.')
            
            return
        if self.value_axe[0] == False:
            # Se realizara el corte en el eje X
            self.corte.setMinimum(int(round(min(self.bmodel.iloc[:,0]),0)))
            self.corte.setMaximum(int(round(max(self.bmodel.iloc[:,0]),0)))

            # Funcion que busca los valores unicos de las coordenadas y sus diferencias para asi
            # en el QSlider donde se elija el corte no se elijan coordenadas a cortar que no existen
            self.corte.setSingleStep(self.coordstepx)
            self.coordstep = self.coordstepx
            
            self.mincut.setText(f'{min(self.bmodel.iloc[:,0])}')
            self.maxcut.setText(f'{max(self.bmodel.iloc[:,0])}')
            self.coord.setText('X')
        
        elif self.value_axe[1] == False:
            # Se realizara el corte en el eje Y
            self.corte.setMinimum(int(round(min(self.bmodel.iloc[:,1]),0)))
            self.corte.setMaximum(int(round(max(self.bmodel.iloc[:,1]),0)))

            # Funcion que busca los valores unicos de las coordenadas y sus diferencias para asi
            # en el QSlider donde se elija el corte no se elijan coordenadas a cortar que no existen
            self.corte.setSingleStep(self.coordstepy)
            self.coordstep = self.coordstepy

            self.mincut.setText(f'{min(self.bmodel.iloc[:,1])}')
            self.maxcut.setText(f'{max(self.bmodel.iloc[:,1])}')
            self.coord.setText('Y')

        else:
            # Se realizara el corte en el eje Z
            self.corte.setMinimum(int(round(min(self.bmodel.iloc[:,2]),0)))
            self.corte.setMaximum(int(round(max(self.bmodel.iloc[:,2]),0)))

            # Funcion que busca los valores unicos de las coordenadas y sus diferencias para asi
            # en el QSlider donde se elija el corte no se elijan coordenadas a cortar que no existen
            self.corte.setSingleStep(self.coordstepz)
            self.coordstep = self.coordstepz

            self.mincut.setText(f'{min(self.bmodel.iloc[:,2])}')
            self.maxcut.setText(f'{max(self.bmodel.iloc[:,2])}')
            self.coord.setText('Z')

    def update_value(self):
        """ Obtener el valor del slider y actualizar el label """
        value = self.corte.value()
    
        # Ajustar el valor al múltiplo más cercano el singleStep
        # Segun la coordenada que se quiera cortar
        if value % self.coordstep != 0:
            value = value - (value % self.coordstep)
        
        # Establecer el valor actualizado
        self.corte.setValue(value) 
        
        # Mostrar el valor en el label
        self.update_axe.setText(f"{value}")

    def select_graph(self):
        # Configurar el lineEdit del corte para que no se salga de la cota
        
        try:
            if self.update_axe.text() == None or self.update_axe.text() == '':
                QtWidgets.QMessageBox.warning(
                self, 'Error', 'Porfavor, seleccionar una coordenada para continuar.'
                )
                return
            update_axe = int(self.update_axe.text()) # No borrar
            
        except ValueError:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Coordenada debe ser un número entero para continuar.'
            )
        if  int(self.update_axe.text())<float(self.mincut.text()) or int(self.update_axe.text())>float(self.maxcut.text()):
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Coordenada se encuentra fuera de rango.'
                )
            return
        if int(self.update_axe.text()) % 2 != 0:
            self.update_axe.setText(str(int(self.update_axe.text())+1))
        
        self.bmodel = pd.read_csv(rf'{self.ruta}\\{self.folders.currentText()}\\modelo_actualizado_{self.extrbox.currentText()}_{os.path.basename(self.folders.currentText())}.csv')

        # Columna que le da color (0: x, 1: y, 2: z, 3:State, 4:d50, 5:id, 6:dist, 7:distacum, grade, dens, mi) 
        
        self.column_color = self.cat2dbox.currentIndex() 

        if self.value_axe[0] == False:    
            # Graficar Y vs Z    
            self.cut_filter = self.bmodel[self.bmodel.iloc[:,0] == int(self.update_axe.text())] # Filtra en X
            self.figure = self.graficar(self.cut_filter.iloc[:,1],
                 self.cut_filter.iloc[:,2],
                 self.cut_filter.iloc[:,self.column_color],
                 self.extrbox.currentText())
            # Renderizar el canvas con la grafica
            self.figure.tight_layout()
            self.canvas.draw()
            
        elif self.value_axe[1] == False:    
            # Graficar Y vs Z
            self.cut_filter = self.bmodel[self.bmodel.iloc[:,1] == int(self.update_axe.text())] # Filtra en Y
            self.figure = self.graficar(self.cut_filter.iloc[:,0],
                 self.cut_filter.iloc[:,2],
                 self.cut_filter.iloc[:,self.column_color],
                 self.extrbox.currentText())
            # Renderizar el canvas con la grafica
            self.figure.tight_layout()
            self.canvas.draw()
        else:                               
            # Graficar X vs Y
            self.cut_filter = self.bmodel[self.bmodel.iloc[:,2] == int(self.update_axe.text())] # Filtra en Z
            self.figure = self.graficar(self.cut_filter.iloc[:,0],
                 self.cut_filter.iloc[:,1],
                 self.cut_filter.iloc[:,self.column_color],
                 self.extrbox.currentText())
            # Renderizar el canvas con la grafica
            self.figure.tight_layout()
            self.canvas.draw()
        self.gif.setEnabled(True)
    
    def graficar(self,x,y,color,ex):
        """ Graficar 2D 
        con variables de entrada:
        * La columna que vaya en el eje X de la grafica 2D
        * La columna que vaya en el eje Y de la grafica 2D
        * Columna que le dara color a la grafica (State)
        * Extraccion a graficar
        """
        self.figure.clear()

        size = self.size2d
        norm = mcolors.Normalize(vmin=min(color), vmax=max(color))  
        cmap = LinearSegmentedColormap.from_list("custom_cmap", [self.col1_2d, self.col2_2d])
        colors = cmap(norm(color))

        if self.value_axe[0] == False:

            # Graficar Y vs Z
            ax = self.figure.add_subplot(111)
            ax.scatter(y, x, c=colors, marker='s', s=size)
            ax.set_title(f"Periodo {ex} (Corte X = {int(self.update_axe.text())})")
            ax.set_xlabel("Eje Y")
            ax.set_ylabel("Eje Z")

        elif self.value_axe[1] == False:
            # Graficar X vs Z
            ax = self.figure.add_subplot(111)
            ax.scatter(x, y, c=colors, marker='s', s=size)
            ax.set_title(f"Periodo {ex} (Corte Y = {int(self.update_axe.text())})")
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Z")

        else:
            # Graficar X vs Y
            ax = self.figure.add_subplot(111)
            ax.scatter(x, y, c=colors, marker='s', s=size)
            ax.set_title(f"Periodo {ex} (Corte Z = {int(self.update_axe.text())})")
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Y")
        return self.figure
        
    def giftear(self):
            image = [None] * len(self.period)
            i=0
            if self.value_axe[0] == False:  
                
                for value in self.period:
                    # Graficar Y vs Z
                    self.bmodel=pd.read_csv(f'{self.ruta}\\{self.folders.currentText()}\\modelo_actualizado_{value}_{self.folders.currentText()}.csv')    
                    self.cut_filter = self.bmodel[self.bmodel.iloc[:,0] == int(self.update_axe.text())] # Filtra en X
                    self.figif = self.graficar(self.cut_filter.iloc[:,1],
                        self.cut_filter.iloc[:,2],
                        self.cut_filter.iloc[:,self.column_color],
                        value)
                    image[i] = f'per{value}_cut{self.update_axe.text()}'
                    self.figif.savefig(f'{self.ruta}\\{self.folders.currentText()}\\per{value}_cut{self.update_axe.text()}.png',format='png')
                    i+=1
            elif self.value_axe[1] == False:    
                for value in self.period:
                    # Graficar X vs Z
                    self.bmodel=pd.read_csv(f'{self.ruta}\\{self.folders.currentText()}\\modelo_actualizado_{value}_{self.folders.currentText()}.csv')    
                    self.cut_filter = self.bmodel[self.bmodel.iloc[:,1] == int(self.update_axe.text())] # Filtra en X
                    self.figif = self.graficar(self.cut_filter.iloc[:,0],
                        self.cut_filter.iloc[:,2],
                        self.cut_filter.iloc[:,self.column_color],
                        value)
                    image[i] = f'per{value}_cut{self.update_axe.text()}'
                    self.figif.savefig(f'{self.ruta}\\{self.folders.currentText()}\\per{value}_cut{self.update_axe.text()}.png',format='png')
                    i+=1
            else:                 
                for value in self.period:
                        # Graficar Y vs Y
                        self.bmodel=pd.read_csv(f'{self.ruta}\\{self.folders.currentText()}\\modelo_actualizado_{value}_{self.folders.currentText()}.csv')    
                        self.cut_filter = self.bmodel[self.bmodel.iloc[:,2] == int(self.update_axe.text())] # Filtra en X
                        self.figif = self.graficar(self.cut_filter.iloc[:,0],
                            self.cut_filter.iloc[:,1],
                            self.cut_filter.iloc[:,self.column_color],
                            value)
                        image[i] = f'per{value}_cut{self.update_axe.text()}.png'
                        self.figif.savefig(f'{self.ruta}\\{self.folders.currentText()}\\per{value}_cut{self.update_axe.text()}.png',format='png')
                        i+=1
            frames = [Image.open(f'{self.ruta}\\{self.folders.currentText()}\\{img}') for img in image]
            frames[0].save(
                f"{self.ruta}\\{self.folders.currentText()}\\gif_per{self.period}_cut{self.update_axe.text()}.gif",
                save_all=True,
                append_images=frames[1:],
                optimize=True,
                duration=500,  # Duración entre cuadros [ms]
                loop=0         # 0 para bucle infinito
            )
            for img in image: # Borrar fotos de la grafica
                os.remove(f'{self.ruta}\\{self.folders.currentText()}\\{img}')
            gif_dialog = GifDialog(f"{self.ruta}\\{self.folders.currentText()}\\gif_ext{self.period}_cut{self.update_axe.text()}.gif")
            gif_dialog.set_save_path(f"{self.ruta}\\{self.folders.currentText()}")
            gif_dialog.exec()
    
    def graficar3d(self):
        """ Funcion para mostrar la grafica 3D """
        
        self.figure3d.clf()
        self.state_graph3d = True # Esto sirve para cuando se usan las configuraciones
                                  # si es que se grafico y se modifico algo, se graficara denuevo
        
        ax = self.figure3d.add_subplot(111, projection='3d')
        try:
            bm3d = pd.read_csv(rf'{self.ruta}\\{self.folders.currentText()}\\modelo_actualizado_{self.period[-1]}_{self.folders.currentText()}.csv')
        except:
            self.state_graph3d = False
            QtWidgets.QMessageBox.critical(self, 'Error', 'La carpeta donde se guardó la simulación reciente ha sido eliminada. Por favor, vuelve a simular para poder visualizar los resultados.')
            return
        bm3d = bm3d[bm3d.iloc[:,3].isin([1, 2])]

        self.column_color = self.cat3dbox.currentIndex()
        color3d = bm3d.iloc[:,self.column_color]

        norm3d = mcolors.Normalize(vmin=min(color3d), vmax=max(color3d))  
        cmap3d = LinearSegmentedColormap.from_list("custom_cmap", [self.col1_3d, self.col2_3d])
        colors3d = cmap3d(norm3d(color3d))

        ax.scatter(
            bm3d.iloc[:, 0], 
            bm3d.iloc[:, 1], 
            bm3d.iloc[:, 2], 
            c=colors3d, 
            s=self.size3d, 
            marker='o'
        )
        cbar = self.figure.colorbar(plt.cm.ScalarMappable(norm=norm3d, cmap=cmap3d), ax=ax)
        cbar.set_label(f'{self.item3d[self.column_color]}')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        self.canvas3d.draw()