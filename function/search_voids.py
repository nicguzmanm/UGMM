import numpy as np


def locate_voids(model, void_id, dcell):
    '''
    Busca vacíos alrededor de un bloque vacío (pos) y devuelve el
    número de vacíos encontrados, la ubicación y el tamaño medio
    en el siguiente orden:

    [n_vacios, vacio_1, ..., vacio_9, d50_1, ..., d50_9]
    '''

    # Posición del bloque vacío:
    x0, y0, z0 = model[void_id, 0:3]

    # Posición de los bloques (superiores y laterales):
    pos_above = [-1] * 9
    pos_level = [-1] * 8

    # Factores de dimensión para la ubicación de los bloques:
    offset_above = [[-1, 1, -1], [-1, 1,  0], [-1, 1, 1],
                    [ 0, 1, -1], [ 0, 1,  0], [ 0, 1, 1],
                    [ 1, 1, -1], [ 1, 1,  0], [ 1, 1, 1]]
    offset_level = [[-1, 0, -1], [-1, 0,  0], [-1, 0, 1], [0, 0, -1],
                    [ 0, 0,  1], [ 1, 0, -1], [ 1, 0, 0], [1, 0,  1]]
    
    # Recorrer cada uno de los bloques:
    for row in range(len(model)):

        # Recuperar las coordenadas del bloque:
        x1, y1, z1 = model[row, 0:3]

        # Comprobar las posiciones superiores:
        for i, (nx, ny, nz) in enumerate(offset_above):
            if (x1, y1, z1) == (x0 + nx * dcell, y0 + ny * dcell, z0 + nz * dcell):
                pos_above[i] = row

        # Comprobar las posiciones laterales:
        for i, (nx, ny, nz) in enumerate(offset_level):
            if (x1, y1, z1) == (x0 + nx * dcell, y0 + ny * dcell, z0 + nz * dcell):
                pos_level[i] = row

    # Devolver las posiciones:
    return pos_above, pos_level


def search_voids(model, pos_above, pos_level):
    '''Cuenta la cantidad de vacíos'''

    # Datos de los bloques superiores:
    num_voids, state, d50 = 1, 0, 0.5
    voids_data = [num_voids] + [state] * 9 + [d50] * 9

    # Caso con menos de 9 bloques (paredes del modelo):
    pos_level = [n for n in pos_level if n >= 0]

    # Calcular el número de vacíos:
    voids_data[0] = (np.sum(model[pos_above, 3] == 1) + 
                     np.sum(model[pos_level, 3] == 1))
    
    # Guardar la fragmentación de los bloques:
    voids_data[10:20] = model[pos_above, 4]
    
    # Guardar el estado de los bloques:
    pos = [n for n in pos_above if n >= 0]
    voids_data[1:10] = np.where(model[pos, 3] == 1)[0].tolist()

    # Devolver la información de los bloques:
    return voids_data, pos_above

    # DEBERÍA EVALUAR LOS BLOQUES DE ABAJO