from PyQt6.QtCore import QThread, pyqtSignal
from function.mainSim import sim
import traceback

class SimulationThread(QThread):
    """ 
    Clase que permite que la aplicacion principal
    no se pegue, corriendo en esta clase la funcion
    principal de simulacion
    """

    progress_updated = pyqtSignal(int)
    simulation_finished = pyqtSignal(object, object, object, object, object, object) # Salidas
    simulation_error = pyqtSignal(str)
    simulation_stop = pyqtSignal(bool)

    def __init__(self, n, mvc, extfile, bmfile, dpfile, stress_activate, folder, ruta, dcell): # Entradas
        
        """ Constructor """

        super().__init__()
        
        self.n = n
        self.mvc = mvc
        self.extfile = extfile
        self.bmfile = bmfile
        self.dpfile = dpfile
        self.stress_activate = stress_activate
        self.folder = folder
        self.ruta = ruta
        self.dcell = dcell
        self.stop_sim = False

    def run(self):
        """ Ejecucion de la simulacion """
        
        try:
            # Ejecutar la simulación

            self.stress, self.ton, self.grade, self.subfolder, self.error, self.fine_metal = sim(
                int(self.n),
                int(self.mvc),
                self.extfile,
                self.bmfile,
                self.dpfile,
                self.stress_activate, 
                self.folder, self.ruta,
                self.dcell,
                self.progress_updated.emit,
                self.check_stop_sim
            )

            # Emitir los resultados
            
            self.simulation_finished.emit(self.stress, self.ton, self.grade, self.subfolder, self.error, self.fine_metal) # Salidas
        except Exception as e:
            self.simulation_error.emit(str(e))
            traceback.print_exc()
            
    def check_stop_sim(self):
        """ Revisa la bandera de detención cada vez que se actualiza el progreso """

        if self.stop_sim:
            self.simulation_stop.emit(True)
            return True
        return False

    def stop(self):
        """ Método para detener la simulación desde fuera del hilo """
        
        self.stop_sim = True