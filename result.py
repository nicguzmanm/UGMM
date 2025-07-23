from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtGui import QIcon
import os

class Resultados(QtWidgets.QDialog):
    """ Pestaña que muestra los resultados de la simulacion"""

    def __init__(self, period = None, stress = None, ton = None, acum_ton = None, grade = None, acum_grade = None, ruta = None, fine_metal = None):

        """ 
        Constructor para mostrar resultados
        de la simulacion, entregando:
        * Periodo
        * Esfuerzo
        * Tonelaje
        * Ley
        """

        super().__init__()
        uic.loadUi('ui\\Resultados.ui', self)
        self.setWindowIcon(QIcon('asset\\dark_UGMM.png'))

        self.setWindowTitle('Resultados de Simulación')
        self.tableresult.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        # Variables de control 
        self.period = period
        self.stress = stress
        self.ruta = ruta
        self.grade = grade
        self.ton = ton
        self.fine_metal = fine_metal

        # Informar del estado de las simulaciones
        if self.ruta is not None:
            self.state.setText(f'Simulación: {os.path.basename(self.ruta)}')
        elif self.ruta is None:
            self.state.setText(f'Simulación: No se encuentra ninguna simulación realizada')
        
        self.tableresult = self.findChild(QtWidgets.QTableWidget,'tableresult')

        # Definir cuantas filas se informaran
        if self.period != None:
            self.tableresult.setRowCount(len(self.period))

        # Rellenar la tabla con los resultados entregados por la simulacion
        
        self.fill_result(self.period,0,0)
        if self.stress == None:
            self.fill_result(self.stress,2,2)
        elif self.stress[0] != '-':
            self.fill_result(self.stress,2,2)
        else:
            if self.stress != None:
                index=0
                for value in self.stress:
                    item = QtWidgets.QTableWidgetItem(value)
                    self.tableresult.setItem(index,2,item)
                    index+=1
        self.fill_result(self.ton,3,1)
        self.fill_result(self.grade,4,2)
        self.fill_result(self.fine_metal,1,2)
        
        
        
        
    def fill_result(self,result_to_show,col,dec):
        """ Funcion para mostrar los resultados en la tabla ingresando
        la lista que se quiere mostrar con su columna respectiva donde se ingresara 
        Las variables a ingresar a esta funcion son:
        * La variable a mostrar
        * La columna donde se ubicara
        * Decimales que se quieran mostrar
        """
        
        if result_to_show is not None:
            index=0
            for value in result_to_show:
                item = QtWidgets.QTableWidgetItem(str(f'{round(value,int(dec)):.{int(dec)}f}'))
                self.tableresult.setItem(index,col,item)
                index+=1