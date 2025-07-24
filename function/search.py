import numpy as np
from numba import njit

@njit
def voids(model, pos_above, pos_level):
    '''Cuenta la cantidad de vacíos y devuelve estados + d50'''
    voids_data = np.zeros(19, dtype=np.float64)  # [num_voids] + 9 estados + 9 d50
    num_voids = 0

    # Superior (pos_above)
    for i in range(9):
        idx = pos_above[i]
        if idx >= 0 and model[idx, 3] == 1:
            num_voids += 1

    # Lateral (pos_level)
    for i in range(pos_level.shape[0]):
        idx = pos_level[i]
        if idx >= 0 and model[idx, 3] == 1:
            num_voids += 1

    voids_data[0] = num_voids

    # Guardar estados y d50
    for i in range(9):
        idx = pos_above[i]
        if idx >= 0:
            voids_data[1 + i]  = 1.0 if model[idx, 3] == 1 else 0.0
            voids_data[10 + i] = model[idx, 4]  # fragmentación

    return voids_data, pos_above
    # # Datos de los bloques superiores:
    # num_voids, state, d50 = 1, 0, 0.5
    # voids_data = [num_voids] + [state] * 9 + [d50] * 9

    # # Caso con menos de 9 bloques (paredes del modelo):
    # pos_level = [n for n in pos_level if n >= 0]

    # # Calcular el número de vacíos:
    # voids_data[0] = (np.sum(model[pos_above, 3] == 1) + 
    #                  np.sum(model[pos_level, 3] == 1))
    
    # # Guardar la fragmentación de los bloques:
    # voids_data[10:20] = model[pos_above, 4]
    
    # # Guardar el estado de los bloques:
    # pos = [n for n in pos_above if n >= 0]
    # voids_data[1:10] = np.where(model[pos, 3] == 1)[0].tolist()

    # Devolver la información de los bloques:


    # DEBERÍA EVALUAR LOS BLOQUES DE ABAJO