from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtCore import Qt

import sys
import pandas as pd
import os
import numpy as np
import traceback

from result import Resultados
from thread import SimulationThread
from gif import GifDialog
from viewer import Visualizador
from config import Configuration
from save import SaveDialog
from importer import Importbm

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap
import subprocess
import shutil
from PIL import Image

#. , ; tabulacion
class MainWindow(QtWidgets.QMainWindow):
    """ Aplicacion principal a ejecutar """
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui\\main_window.ui', self)

        self.setWindowTitle('Gravity Flow Simulator (beta)')
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))
        self.setMinimumSize(0, 0)
        self.setMaximumSize(16777215, 16777215)
        self.setWindowFlags(Qt.WindowType.Window)
        
        # Variables de control
        self.control_val()
        self.bmName.setReadOnly(True)
        self.dpName.setReadOnly(True)
        self.extName.setReadOnly(True)

        # Importar BM
        self.bmImportButton.clicked.connect(self.verifiedbm)
        self.bmMenubar.triggered.connect(self.verifiedbm)

        # Importar DP
        self.dpImportButton.clicked.connect(self.importdp)
        self.dpMenubar.triggered.connect(self.importdp)

        # Importar Plan de extracción (ext)
        self.extImportButton.clicked.connect(self.importext)
        self.extMenubar.triggered.connect(self.importdp)

        # Ver la carpeta de resultados
        self.fold = 'report' # Ruta donde se iran las carpetas de la simulacion
        self.salida.triggered.connect(self.select_fold)
        self.salida_button.clicked.connect(self.select_fold)

        # Mostrar la ruta de salida
        
        self.showsimruta.setReadOnly(True)
        self.show_ruta()
        self.result_folders.triggered.connect(lambda: self.open_result_folder(self.ruta_completa))

        #self.change_dcell.toggled.connect(self.show_table_dcell)
        #self.show_table_dcell()
        self.validator()
        
        # Ver resultados
        self.Ver_Resultados_de_Simulacion = self.findChild(QtGui.QAction, 'Ver_Resultados_de_Simulacion')
        self.Ver_Resultados_de_Simulacion.triggered.connect(self.openresult)

        # Correr Simulación
        self.simButton.clicked.connect(self.corrector)

        # Poner un canvas en el lugar donde ira la grafica
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphlayout2d.addWidget(self.canvas)

        self.figure3d = plt.figure()
        self.canvas3d = FigureCanvas(self.figure3d)
        self.graphlayout3d.addWidget(self.canvas3d)

        # Graficar en 3D
        self.view3d.clicked.connect(self.graficar3d)

        # Guardar los ejes que se quieran graficar
        self.cortex.valueChanged.connect(self.update_value)
        self.cortey.valueChanged.connect(self.update_value)
        self.cortez.valueChanged.connect(self.update_value)
        self.grapher.clicked.connect(self.select_graph) # Graficar

        # Detener simulacion
        self.stop.clicked.connect(self.simulation_stop)

        # Mostrar animacion
        self.gif.clicked.connect(self.giftear)

        # Fragmentacion depende del esfuerzo
        self.stress_model.toggled.connect(self.update_frag_model_state)
        self.update_frag_model_state()

        # Abrir visualizador
        self.viewer.triggered.connect(self.go_viewer)

        # Abrir pestaña de configuracion
        self.config.triggered.connect(self.open_config)
 
    def cargar_ruta(self):
        """ Carga la ruta guardada en 'simsavefile.txt' al iniciar el programa. """
        
        # Obtener la ruta del archivo dentro de la carpeta "memory"
        directorio_memory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory")
        ruta_archivo = os.path.join(directorio_memory, "simsavefile.txt")

        # Si el archivo existe, cargar la ruta guardada
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                self.ruta_completa = archivo.read().strip()

    def select_fold(self):
        """ Seleccionar la carpeta donde se guardarán las simulaciones y guardar la ruta. """
        
        ruta_seleccionada = QtWidgets.QFileDialog.getExistingDirectory(self, 'Seleccionar carpeta donde se guardarán las simulaciones')
        
        if ruta_seleccionada:  
            self.ruta_completa = ruta_seleccionada  # Actualizar la ruta solo si el usuario selecciona una
            directorio_memory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory")
             
            if not os.path.exists(directorio_memory):
                os.makedirs(directorio_memory)
            ruta_archivo = os.path.join(directorio_memory, "simsavefile.txt")

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                if os.path.basename(self.ruta_completa) != 'report':
                    self.ruta_completa = os.path.normpath(os.path.join(self.ruta_completa, self.fold))
                else:
                    self.ruta_completa = os.path.normpath(self.ruta_completa)
                archivo.write(self.ruta_completa)
            self.showsimruta.setText(self.ruta_completa)

    def show_ruta(self):
        """ Mostrar la ruta de salida y guardarla en un archivo. """

        # Si no hay un archivo de memoria es porque se inicia por primera vez a la app por lo que 
        # se crea el archivo de memoria y se ingresa en la ruta de salida la carpeta report que esta donde
        # se instala la aplicacion, de otra manera si ya hay creada una carpeta, es porque el usuario ya eligio
        # donde guardar independiente si ha ingresado una ruta manual o esta la default, esta funcion leera
        # la ruta que estara en el texto y se abrira a partir de esta.

        if not os.path.exists('memory\\simsavefile.txt'): # Caso que no existe el archivo (Primera vez ingresando)
            direct = os.path.dirname(os.path.abspath(__file__))
            self.ruta_completa = os.path.normpath(os.path.join(direct, self.fold))
        else: # Ya se eligio donde se guardaran las simulaciones
            self.cargar_ruta()

        # HACER MAYÚSCULA EN WINDOWS
        if self.ruta_completa[1] == ':':
            self.ruta_completa = self.ruta_completa[0].upper() + self.ruta_completa[1:]

        # Guardar la ruta en el archivo para futuras sesiones
        directorio_memory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory")
        
        if not os.path.exists(directorio_memory):
            os.makedirs(directorio_memory)  # Crear "memory" si fue eliminada

        ruta_archivo = os.path.join(directorio_memory, "simsavefile.txt")

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(self.ruta_completa)

        self.showsimruta.setText(self.ruta_completa)

    def control_val(self):
        """ Asignar variables """

        self.bmfile = None
        self.dpfile = None
        self.extfile = None
        self.bmpreceed = None
        self.dppreceed = None
        self.extpreceed = None
        self.stress = None
        self.fine_metal = None
        self.num_period = None
        self.ton = None
        self.acum_ton = None
        self.grade = None
        self.acum_grade = None
        self.simfolder = None
        self.state_graph2d = False
        self.state_graph3d = False

        # Configuracion Visual default de las graficas 
        self.col1_2d = '#FF5733'
        self.col2_2d = '#33FF57'
        self.col1_3d = '#FF5733'
        self.col2_3d = '#33FF57'
        self.size2d = 20 
        self.size3d = 20 
        
    def validator(self):
        """ Valida numero entero en los lineEdit de:
        * N
        * MVC
        * Intervalo de periodo
        * Periodo maximo
        * Ingreso manual de coordenada de corte
        """

        int_valide_N_MVC = QtGui.QIntValidator(0, 99)
        self.inputN.setValidator(int_valide_N_MVC)
        self.inputMVC.setValidator(int_valide_N_MVC)
    
    def verifiedbm(self):

        win = Importbm(self)
        win.imported.connect(self.namefile)
        win.exec()
        
            # try:
            #     # Calculo de tamaño del bloque

            #     x_value = np.unique(pd.to_numeric(bm.iloc[:, 0], errors="coerce").dropna().astype(float).tolist())
            #     y_value = np.unique(pd.to_numeric(bm.iloc[:, 1], errors="coerce").dropna().astype(float).tolist())
            #     z_value = np.unique(pd.to_numeric(bm.iloc[:, 2], errors="coerce").dropna().astype(float).tolist())
               
            #     x_value = np.sort(np.unique(np.array(x_value)))
            #     y_value = np.sort(np.unique(np.array(y_value)))
            #     z_value = np.sort(np.unique(np.array(z_value)))

            #     x_value = np.unique(np.diff(x_value))
            #     y_value = np.unique(np.diff(y_value))
            #     z_value = np.unique(np.diff(z_value))
                
            #     self.coordstepx = int([x for x in x_value if x > 0][0]) # self.coordstepx = 2
            #     self.coordstepy = int([y for y in y_value if y > 0][0]) # self.coordstepy = 2
            #     self.coordstepz = int([z for z in z_value if z > 0][0]) # self.coordstepz = 2
            # except:
            #     QtWidgets.QMessageBox.warning(
            #         self, 'Error', 'Formato inconsistente para un modelo de bloques.'
            #     )
            #     return
        
    def namefile(self,ruta):
        """ Devolver la ruta de la pestaña emergente """

        if ruta is not None:
            self.bmfile = ruta
            self.bmName.setText(f'{os.path.basename(self.bmfile)}')
            self.bmpreceed = self.bmfile
        
    def importdp(self):
        self.dpfile, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Seleccionar archivo de puntos de extracción', '', 'CSV Files (*.csv);; Excel Files (*.xlsx);; Text Files (*.txt);; All files (*)'
        )
        if self.dpfile:
            self.dpName.setText(f'{os.path.basename(self.dpfile)}')
            self.dppreceed = self.dpfile

    def importext(self):
        self.extfile, _  = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Seleccionar archivo de plan de extracción', '', 'CSV Files (*.csv);; Excel Files (*.xlsx);; Text Files (*.txt);; All files (*)'
        )
        if self.extfile:
            self.extName.setText(f'{os.path.basename(self.extfile)}')
            self.extpreceed = self.extfile
            df_periodos = pd.read_csv(self.extpreceed, index_col=0)
            tonelaje_objetivo_por_periodo = {
            int(periodo): df_periodos[periodo].dropna().to_dict()
            for periodo in df_periodos.columns
            }
            self.num_period = len(tonelaje_objetivo_por_periodo)


    def update_frag_model_state(self):
        """ Actualiza el estado de frag_model dependiendo del estado de stress_model """

        if self.stress_model.isChecked():
            self.frag_model.setCheckable(True)  # Habilitar la opción de marcar el modelo de fragmentación
            self.frag_model.setEnabled(True)
        else:
            self.frag_model.setCheckable(False)  # Deshabilitar la opción de marcar el modelo de fragmentación
            self.frag_model.setEnabled(False)

    def corrector(self): 
        try:
            if not self.dppreceed or not self.bmpreceed or not self.extpreceed:
                QtWidgets.QMessageBox.warning(
                    self, '¡Advertencia!', 'Se necesita importar todos los archivos para continuar.'
                )
                return

            # Obtener valores de entrada
            self.n = self.inputN.text()
            self.mvc = self.inputMVC.text()

            # Verificar que todos los parámetros estén presentes
            if not self.n:
                QtWidgets.QMessageBox.warning(
                    self, '¡Advertencia!', 'Debe ingresar el parametro N para continuar la simulación.'
                )
                return
            if not self.mvc:
                QtWidgets.QMessageBox.warning(
                    self, '¡Advertencia!', 'Debe ingresar el parametro MVC para continuar la simulación.'
                )
                return
            
            # Ejecutar 
            self.sim_status.setText('')
            self.resimulate()
            self.run_simulation()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            traceback.print_exc()
            print(e)

    def run_simulation(self):
        """ Ejecuta la simulacion en un hilo diferente """

        self.exit = True
        self.desactivate()
        self.simButton.setText('Simulando...')
        if self.stress_model.isChecked(): # Si el usuario elije el modelo de esfuerzo
            self.stress_activate = True
        else:
            self.stress_activate = False
        self.ruta = os.path.dirname(os.path.normpath(self.ruta_completa))
        self.dcell = [2,2,2]
        
        """ Entra a la simulación"""

        self.sim_thread = SimulationThread(
            self.n, self.mvc,self.extpreceed, self.bmpreceed, 
            self.dppreceed,self.stress_activate, self.fold, self.ruta, self.dcell # Parametros de entrada
        )
        self.sim_thread.progress_updated.connect(self.update_progress)
        self.sim_thread.simulation_finished.connect(self.simulation_finished) # En esta funcion se define la salida
        self.sim_thread.simulation_error.connect(self.simulation_error)
        self.sim_thread.simulation_stop.connect(self.simulation_stop)
        self.sim_thread.start()

    def update_progress(self, progress_value):
        self.progressBar.setValue(progress_value)

    def simulation_stop(self):
        """ Detiene la simulación """
        self.stop_warn = QtWidgets.QMessageBox(self)
        self.stop_warn.setWindowTitle('Advertencia')
        self.stop_warn.setText('Estas a punto de detener la simulación.\n¿Deseas continuar?')
        self.stop_warn.setIcon(QtWidgets.QMessageBox.Icon.Question)
        self.stop_warn.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)

        if  self.stop_warn.exec() == QtWidgets.QMessageBox.StandardButton.Ok:        
            self.exit = False
            self.sim_thread.stop()
            self.sim_status.setText('Deteniendo simulación ...')    
    
    def simulation_finished(self, stress, period, ton, grade, simfolder, error, fine_metal):
        """ Funcion que retorna los resultados de la simulacion"""

        # self.error = 0 => No se genero ningun error dentro de la simulacion
        # self.error = 1 => La simulacion dio error

        # self.exit = True => La simulacion se completo sin detenerse
        # self.exit = False => La simulacion se detuvo manualmente

        self.error = error
        if self.exit and self.error == 0:
            # Salida sin detenerse y exitosa
            # Parametros de salida
            self.progressBar.setValue(100)
            QtWidgets.QMessageBox.information(
                self, 'Éxito', '¡Simulación completada con éxito!'
            )
            self.fine_metal = fine_metal
            self.stress = stress
            self.num_period = period
            self.ton = ton
            self.simfolder = simfolder
            self.ton = ton
            self.grade = grade
            simfolder = os.path.normpath(simfolder)
            self.sim_status.setText(rf'Simulación guardada en {os.path.join(*simfolder.split(os.sep)[-3:])}')

            # Creacion del archivo de resultados
            # Extraccion, Esfuerzo, Ton, Ton acumulada, Ley, Ley acumulada
            inforesult = {"Periodo": self.num_period, "Esfuerzos": self.stress,
                          "Tonelaje": self.ton, "Tonelaje metal fino": self.fine_metal,
                          "Ley": self.grade }
            df = pd.DataFrame(inforesult)
            result_namefile = f"{simfolder}\\simresult_{os.path.basename(simfolder)}.csv"
            df.to_csv(result_namefile, index=False)

            # Se agregan las extracciones que se simularon en la pestaña de grafica para poder visualizarlas
            self.extrbox = self.findChild(QtWidgets.QComboBox,'extrbox')
            for i in self.num_period:
                self.extrbox.addItem(f'{i}')

            # Categorias que el usario eligira para visualizar los colores en la grafica
            self.item = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi","period"]
            self.item3d = ["x", "y", "z", "State", "d50", "id", "dist", "distacum", "grade", "dens", "mi", "period"]
            self.cat.addItems(self.item)
            self.cat3d.addItems(self.item3d)
            self.simButton.setText('Simular') 
            
            
            self.activate()
        elif not self.exit and self.error == 0: 
            # Se detuvo la Simulacion
            # Nos desahacemos de las variables que creo a medias la funcion
            # al ser interrumpida

            self.stress = None
            self.num_period = None
            self.ton = None
            self.grade = None
            self.fine_metal = None

            self.afterstop()
            shutil.rmtree(simfolder) # Borrar la carpeta ya que se detuvo la simulacion
            self.simfolder = None
            
            self.simButton.setText('Simular')
            self.sim_status.setText('Simulación no guardada')
            self.stop_warn.close()
            QtWidgets.QMessageBox.information(
                self, 'Éxito', 'Simulación detenida'
            )
        else: # self.exit = False, self.error = 1
            # Se detuvo la Simulacion
            # debido a un error

            self.stress = None
            self.num_period = None
            self.ton = None
            self.grade = None
            self.fine_metal = None

            self.afterstop()
            #shutil.rmtree(simfolder) # Borrar la carpeta ya que se detuvo la simulacion
            self.simfolder = None
            
            self.simButton.setText('Simular')
            self.sim_status.setText('Simulación no guardada')
            QtWidgets.QMessageBox.critical(
                self, 'Error', 'La simulación presento un error, porfavor revisar archivos importados junto al tamaño de bloque.'
            )
        
    def ejes(self):
        """ Ver que no esta seleccionado mas de dos ejes a graficar en pestaña 2D """

        self.checkboxes = [self.graphx, self.graphy, self.graphz]
        self.value_axe=[checkbox.isChecked() for checkbox in self.checkboxes]
        num_check = sum(self.value_axe)
        if num_check != 2:
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Seleccionar solo dos ejes de coordenadas a graficar.')
            return
        if not self.extrbox.currentText():
            QtWidgets.QMessageBox.warning(self, 'Alerta', 'Seleccionar la extracción a graficar.')
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
        try:
            self.bmodel=pd.read_csv(rf'{self.simfolder}\\modelo_actualizado_periodo_{self.extrbox.currentText()}.txt')
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
            self.corte.setSingleStep(self.dcell[0])
            self.coordstep = self.dcell[0]
            
            self.mincut.setText(f'{min(self.bmodel.iloc[:,0])}')
            self.maxcut.setText(f'{max(self.bmodel.iloc[:,0])}')
            self.coord.setText('X')
        
        elif self.value_axe[1] == False:
            # Se realizara el corte en el eje Y
            self.corte.setMinimum(int(round(min(self.bmodel.iloc[:,1]),0)))
            self.corte.setMaximum(int(round(max(self.bmodel.iloc[:,1]),0)))

            # Funcion que busca los valores unicos de las coordenadas y sus diferencias para asi
            # en el QSlider donde se elija el corte no se elijan coordenadas a cortar que no existen
            self.corte.setSingleStep(self.dcell[1])
            self.coordstep = self.dcell[1]

            self.mincut.setText(f'{min(self.bmodel.iloc[:,1])}')
            self.maxcut.setText(f'{max(self.bmodel.iloc[:,1])}')
            self.coord.setText('Y')

        else:
            # Se realizara el corte en el eje Z
            self.corte.setMinimum(int(round(min(self.bmodel.iloc[:,2]),0)))
            self.corte.setMaximum(int(round(max(self.bmodel.iloc[:,2]),0)))

            # Funcion que busca los valores unicos de las coordenadas y sus diferencias para asi
            # en el QSlider donde se elija el corte no se elijan coordenadas a cortar que no existen
            self.corte.setSingleStep(self.dcell[2])
            self.coordstep = self.dcell[2]

            self.mincut.setText(f'{min(self.bmodel.iloc[:,2])}')
            self.maxcut.setText(f'{max(self.bmodel.iloc[:,2])}')
            self.coord.setText('Z')
    
    def update_value(self):
        """ Obtener el valor del slider y actualizar el label """
        value = self.corte.value()
    
        # Ajustar el valor al multiplo más cercano el singleStep
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
            update_axe = int(self.update_axe.text()) # No borrar, fuerza el error si esque se llegara a tener un numero decimal
            
        except ValueError:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Coordenada debe ser numero entero para continuar.'
            )
        if  int(self.update_axe.text())<float(self.mincut.text()) or int(self.update_axe.text())>float(self.maxcut.text()):
            QtWidgets.QMessageBox.warning(
                    self, 'Error', 'Coordenada se encuentra fuera de rango.'
                )
            return
        if int(self.update_axe.text()) % 2 != 0:
            self.update_axe.setText(str(int(self.update_axe.text())+1))
        
        try:
            self.bmodel = pd.read_csv(rf'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\modelo_actualizado_{self.extrbox.currentText()}_{os.path.basename(self.simfolder)}.csv')
        except Exception:
            QtWidgets.QMessageBox.critical(
                self,'Error','La carpeta de la simulación reciente ha sido eliminada. Ejecute una nueva simulación para visualizar los resultados.'
            )
            
            return
        # Columna que le da color (0: x, 1: y, 2: z, 3:State, 4:d50, 5:id, 6:dist, 7:distacum, 8:grade, 9:dens, 10:mi) 
        
        self.column_color = self.cat.currentIndex()

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
        self.state_graph2d = True # Esto sirve para cuando se usan las configuraciones
                                  # si es que se grafico y se modifico algo, se graficara denuevo
        # Crear una nueva columna con los colores
        norm = mcolors.Normalize(vmin=min(color), vmax=max(color))  
        cmap = LinearSegmentedColormap.from_list("custom_cmap", [self.col1_2d, self.col2_2d])
        colors = cmap(norm(color))


        if self.value_axe[0] == False:
            # Graficar Y vs Z
            ax = self.figure.add_subplot(111)
            ax.scatter(x, y, c=colors, marker='s', s = self.size2d)
            cbar = self.figure.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
            cbar.set_label(f'{self.item[self.column_color]}') # Leyenda
            ax.set_title(f"Periodo {ex} (Corte X = {int(self.update_axe.text())})")
            ax.set_xlabel("Eje Y")
            ax.set_ylabel("Eje Z")

        elif self.value_axe[1] == False:
            # Graficar X vs Z
            ax = self.figure.add_subplot(111)
            ax.scatter(x, y, c=colors, marker='s', s = self.size2d)
            cbar = self.figure.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
            cbar.set_label(f'{self.item[self.column_color]}')
            ax.set_title(f"Periodo {ex} (Corte Y = {int(self.update_axe.text())})")
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Z")

        else:
            # Graficar X vs Y
            ax = self.figure.add_subplot(111)
            ax.scatter(x, y, c=colors, marker='s', s=self.size2d)
            cbar = self.figure.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
            cbar.set_label(f'{self.item[self.column_color]}')
            ax.set_title(f"Periodo {ex} (Corte Z = {int(self.update_axe.text())})")
            ax.set_xlabel("Eje X")
            ax.set_ylabel("Eje Y")
        return self.figure
        
    def giftear(self):
        image = [None] * len(self.num_period)
        i=0
        if self.value_axe[0] == False:  
            
            for value in self.num_period:
                # Graficar Y vs Z
                self.bmodel=pd.read_csv(rf'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\modelo_actualizado_periodo_{value}.txt')    
                self.cut_filter = self.bmodel[self.bmodel.iloc[:,0] == int(self.update_axe.text())] # Filtra en X
                self.figif = self.graficar(self.cut_filter.iloc[:,1],
                    self.cut_filter.iloc[:,2],
                    self.cut_filter.iloc[:,self.column_color],
                    value)
                image[i] = f'ext{value}_cut{self.update_axe.text()}.png'
                self.figif.savefig(f'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\ext{value}_cut{self.update_axe.text()}.png',format='png')
                i+=1
        elif self.value_axe[1] == False:    
            for value in self.num_period:
                # Graficar X vs Z
                self.bmodel=pd.read_csv(rf'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\modelo_actualizado_periodo_{value}.txt')    
                self.cut_filter = self.bmodel[self.bmodel.iloc[:,1] == int(self.update_axe.text())] # Filtra en X
                self.figif = self.graficar(self.cut_filter.iloc[:,0],
                    self.cut_filter.iloc[:,2],
                    self.cut_filter.iloc[:,self.column_color],
                    value)
                image[i] = f'ext{value}_cut{self.update_axe.text()}.png'
                self.figif.savefig(f'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\ext{value}_cut{self.update_axe.text()}.png',format='png')
                i+=1
        else:                 
            for value in self.num_period:
                # Graficar X vs Y
                self.bmodel=pd.read_csv(rf'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\modelo_actualizado_periodo_{value}.txt')    
                self.cut_filter = self.bmodel[self.bmodel.iloc[:,2] == int(self.update_axe.text())] # Filtra en X
                self.figif = self.graficar(self.cut_filter.iloc[:,0],
                    self.cut_filter.iloc[:,1],
                    self.cut_filter.iloc[:,self.column_color],
                    value)
                image[i] = f'ext{value}_cut{self.update_axe.text()}.png'
                self.figif.savefig(f'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\ext{value}_cut{self.update_axe.text()}.png',format='png')
                i+=1
        frames = [Image.open(f'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\{img}') for img in image]
        frames[0].save(
            f"{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\gif_ext{self.num_period}_cut{self.update_axe.text()}.gif",
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=500,  # Duración entre cuadros (ms)
            loop=0         # 0 para bucle infinito
        )
        for img in image: # Borrar fotos de la grafica
            os.remove(f'{self.simfolder}\\{img}')
        gif_dialog = GifDialog(f"{self.simfolder}\\gif_ext{self.num_period}_cut{self.update_axe.text()}.gif")
        gif_dialog.set_save_path(f"{self.fold}\\{os.path.basename(self.simfolder)}")
        gif_dialog.exec()
    
    def graficar3d(self):
        """ Funcion para mostrar la grafica 3D """
        
        self.figure3d.clf()
        self.state_graph3d = True # Esto sirve para cuando se usan las configuraciones
                                  # si es que se grafico y se modifico algo, se graficara denuevo
        
        ax = self.figure3d.add_subplot(111, projection='3d')
        
        try:
            bm3d = pd.read_csv(rf'{self.ruta_completa}\\{os.path.basename(self.simfolder)}\\bloques_extraidos_periodo_{self.extrbox3d.currentText()}.csv', sep=';')
            
        except:
            self.state_graph3d = False
            QtWidgets.QMessageBox.critical(self, 'Error', 'La carpeta donde se guardó la simulación reciente ha sido eliminada. Por favor, vuelve a simular para poder visualizar los resultados.')
            return
        bm3d = bm3d[bm3d.iloc[:, 3].isin([1, 2])]
        self.column_color = self.cat3d.currentIndex()
        color3d = bm3d.iloc[:,self.column_color]

        norm3d = mcolors.Normalize(vmin=min(color3d), vmax=max(color3d))  
        cmap3d = LinearSegmentedColormap.from_list("custom_cmap", [self.col1_3d, self.col2_3d])
        colors3d = cmap3d(norm3d(color3d))

        x = bm3d.iloc[:, 0].values
        y = bm3d.iloc[:, 1].values
        z = bm3d.iloc[:, 2].values

        ax.scatter(
            x, 
            y, 
            z, 
            c=colors3d, 
            s=self.size3d, 
            marker='o'
        )

        cbar = self.figure.colorbar(plt.cm.ScalarMappable(norm=norm3d, cmap=cmap3d), ax=ax)
        cbar.set_label(f'{self.item3d[self.column_color]}') # Leyenda
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        self.canvas3d.draw()

    def simulation_error(self, error_message):
        QtWidgets.QMessageBox.critical(self, 'Error', f'An error occurred: {error_message}')

    def desactivate(self):
        """ Funcion para desactivar los botones mientras la funcion esta corriendo """

        self.simButton.setEnabled(False)
        self.inputN.setEnabled(False)
        self.inputMVC.setEnabled(False)
        self.stress_model.setEnabled(False)
        self.frag_model.setEnabled(False)
        self.bmImportButton.setEnabled(False)
        self.dpImportButton.setEnabled(False)
        self.extImportButton.setEnabled(False)
        self.bmMenubar.setEnabled(False)
        self.dpMenubar.setEnabled(False)
        self.extMenubar.setEnabled(False)
        self.salida.setEnabled(False)
        self.gif.setEnabled(False)
        self.view3d.setEnabled(False)

    def activate(self):
        """ Funcion para activar los botones una vez terminada la simulacion """

        self.simButton.setEnabled(True)
        self.inputN.setEnabled(True)
        self.inputMVC.setEnabled(True)
        self.stress_model.setEnabled(False)
        self.update_frag_model_state()
        self.bmImportButton.setEnabled(True)
        self.dpImportButton.setEnabled(True)
        self.extImportButton.setEnabled(True)
        self.graphx.setEnabled(True)
        self.graphy.setEnabled(True)
        self.graphz.setEnabled(True)
        self.stop.setEnabled(False)
        self.bmMenubar.setEnabled(True)
        self.dpMenubar.setEnabled(True)
        self.extMenubar.setEnabled(True)
        self.salida.setEnabled(True)
        self.view3d.setEnabled(True)

    def afterstop(self):
        """ Funcion para activar/desactivar botons luego de detener el usuario la simulacion """

        self.simButton.setEnabled(True)
        self.inputN.setEnabled(True)
        self.inputMVC.setEnabled(True)
        self.stress_model.setEnabled(False)
        self.update_frag_model_state()
        self.bmImportButton.setEnabled(True)
        self.dpImportButton.setEnabled(True)
        self.extImportButton.setEnabled(True)
        self.graphx.setEnabled(False)
        self.graphy.setEnabled(False)
        self.graphz.setEnabled(False)
        self.stop.setEnabled(False)
        self.bmMenubar.setEnabled(True)
        self.dpMenubar.setEnabled(True)
        self.extMenubar.setEnabled(True)
        self.progressBar.setValue(0)
        self.view3d.setEnabled(False)

    def resimulate(self):
        """ Volver al estado inicial si se desea simular de nuevo """

        self.cortex.setEnabled(False)
        self.cortex.setValue(0)
        self.cortey.setEnabled(False)
        self.cortey.setValue(0)
        self.cortez.setEnabled(False)
        self.cortez.setValue(0)
        self.grapher.setEnabled(False)
        self.update_axex.setEnabled(False)
        self.update_axex.clear()
        self.update_axey.setEnabled(False)
        self.update_axey.clear()
        self.update_axez.setEnabled(False)
        self.update_axez.clear()
        self.grapher.setEnabled(False)
        self.gif.setEnabled(False)
        self.graphx.setEnabled(False)
        self.graphy.setEnabled(False)
        self.graphz.setEnabled(False)
        self.graphx.setChecked(False)
        self.graphy.setChecked(False)
        self.graphz.setChecked(False)
        self.extrbox.clear()
        self.extrbox3d.clear()
        self.cat.clear()
        self.cat3d.clear()
        self.figure.clear()
        self.figure3d.clf()
        self.state_graph2d = False
        self.state_graph3d = False
        self.canvas.draw()
        self.progressBar.setValue(0)
        self.stop.setEnabled(True)
        self.view3d.setEnabled(False)

    def openresult(self):
        """ Mostrar resultados concretos en una ventana aparte """
        win = Resultados(stress = self.stress, period = self.num_period, ton = self.ton, acum_ton = self.acum_ton, grade = self.grade, acum_grade = self.acum_grade, ruta = self.simfolder, fine_metal = self.fine_metal)
        win.exec()

    def open_result_folder(self,fold):
        """ Mostrar donde se guardan las simulaciones, y si no existe esta carpeta, se crea
        con el nombre de 'report'. """

        # Crear la carpeta si no existe
        if not os.path.exists(fold):
            os.makedirs(fold)
            QtWidgets.QMessageBox.information(self, "Carpeta creada", "Se creó la carpeta 'report' donde se guardaran las carpetas de simulación.")

        # Abrir la carpeta en el explorador de archivos
        if os.name == "nt":  # Para Windows
            subprocess.Popen(f'explorer "{fold}"')
        elif os.name == "posix":  # Para macOS/Linux
            subprocess.Popen(["open", fold])

    def go_viewer(self):
        """ Llama a la clase para visualizar simulaciones anteriores """

        win = Visualizador(self.ruta_completa, self.col1_2d, self.col2_2d, self.col1_3d, self.col2_3d, self.size2d, self.size3d)
        win.exec()

    def open_config(self):
        """ Llama a la clase de configuraciones para cambiar el estilo de las graficas """

        config_ventana = Configuration(self.col1_2d, self.col2_2d, self.col1_3d, self.col2_3d, self.size2d, self.size3d)
        config_ventana.config_finished.connect(self.apply_config)
        config_ventana.exec()
    
    def apply_config(self, col1_2d, col2_2d, col1_3d, col2_3d, size2d, size3d, save):
        """ Funcion que revisa si los archivos no fueron modificados y los remplaza 
        por los default que se encontraban anteriormente, y al momento de cambiar algo
        en configuraciones revisa si los canvas estan siendo ocupados para asi realizar
        la modificacion instantanea """
        
        if col1_2d is not None:
            self.col1_2d = col1_2d
        if col2_2d is not None:
            self.col2_2d = col2_2d
        if col1_3d is not None:
            self.col1_3d = col1_3d
        if col2_3d is not None:
            self.col2_3d = col2_3d
        if size2d is not None:
            self.size2d = size2d
        if size3d is not None:
            self.size3d = size3d
        if self.state_graph2d and save:
            self.select_graph() # Graficar en 2D
        if self.state_graph3d and save:
            self.graficar3d() # Graficar en 3D


app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QIcon('asset\\dark_UGMM.png'))
win = MainWindow()
win.show()
sys.exit(app.exec())