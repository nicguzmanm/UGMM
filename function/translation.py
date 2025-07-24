import numpy as np

class Move():
    def __init__(self):
        pass

    @staticmethod
    def translate_model(model: np.array):
        '''
        Traslada las coordenadas del modelo de bloques para que
        el origen se encuentre en (0,0,0)
        '''

        # Obtener las coordenadas mínimas en XYZ:
        min_x = np.min(model[:, 0])
        min_y = np.min(model[:, 1])
        min_z = np.min(model[:, 2])

        # Calcular el desplazamiento necesario:
        offset = np.array([min_x, min_y, min_z])

        # Trasladar el modelo:
        translated_model = model.copy()
        translated_model[:, 0:3] -= offset

        # Devolver modelo y mínimos:
        return translated_model, min_x, min_y, min_z

    @staticmethod
    def translate_points(points, origin_x, origin_y, origin_z):
        '''Traslada los puntos de extracción a un nuevo origen'''
        
        # Copiar el vector original para no modificarlo:
        translated_points = points.copy()
        
        # Trasladar las coordenadas restando el origen:
        translated_points[:, 0] -= origin_x
        translated_points[:, 1] -= origin_z
        translated_points[:, 2] -= origin_y
        
        # Devolver los puntos trasladados:
        return translated_points