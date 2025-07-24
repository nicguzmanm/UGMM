from numba import njit, prange
import numpy as np
from search_voids import search_voids
@njit
def intercambiar_bloques_numba(bmodel, void2, pos, v1, destino_idx):
    """
    Intercambia dos bloques en bmodel, optimizado con numba.
    void2[v1] es el índice del bloque actual, destino_idx es el nuevo.
    """
    # Copiar columnas 3 en adelante (estado en adelante)
    fila_origen = bmodel[void2[v1], 3:].copy()
    fila_destino = bmodel[destino_idx, 3:].copy()

    # Intercambio de datos entre bloques
    bmodel[void2[v1], 3:] = fila_destino
    bmodel[destino_idx, 3:] = fila_origen
    if bmodel[void2[v1], 3] != 1:
        bmodel[void2[v1], 3] = 2  # Siempre que un bloque cae, se vuelve "en movimiento"

    # Marcar destino como vacío
    bmodel[destino_idx, 3] = 1

    return bmodel

@njit
def actualizar_probabilidades(d12, n):
    """
    Calcula probabilidades normalizadas basadas en distancia d12 y parámetro n.
    """
    p = np.empty(9)
    total = 0.0
    for i in range(9):
        p[i] = d12[i] ** -n
        total += p[i]
    for i in range(9):
        p[i] /= total
    return p

@njit
def calcular_vecinos(v22m, c1, b1, max_x, min_x, max_y, min_y, max_z, min_z):
    d1d1 = (-1, 0, 1)
    possc = np.full(9, -1, dtype=np.int64)
    posic = np.full(8, -1, dtype=np.int64)
    conta = 0
    conta2 = 0
    for ab in d1d1:
        for abc in d1d1:
            idx_sup = (v22m[0] + ab) + c1 * (v22m[1] + 1) + b1 * (v22m[2] + abc)
            if (min_x <= v22m[0] + ab <= max_x and
                min_y <= v22m[1] + 1 <= max_y and
                min_z <= v22m[2] + abc <= max_z):
                possc[conta] = idx_sup
            else:
                possc[conta] = -1
            conta += 1

            if ab == 0 and abc == 0:
                conta2 -= 1
            else:
                idx_nivel = (v22m[0] + ab) + c1 * v22m[1] + b1 * (v22m[2] + abc)
                if (min_x <= v22m[0] + ab <= max_x and
                    min_z <= v22m[2] + abc <= max_z):
                    posic[conta2] = idx_nivel
                else:
                    posic[conta2] = -1
                conta2 += 1
    return possc, posic

@njit
def calcular_indices_extraccion(kk0x, kk0y, kk0z, a1, c1, b1, iezi):
    kk02 = []
    for kk in range(len(kk0y)):
        for ll in range(len(kk0x)):
            for zz in range(len(kk0z)):
                idx = a1 * kk0x[ll] + c1 * kk0y[kk] + b1 * kk0z[zz]
                kk02.append(idx)
                if idx < len(iezi):
                    iezi[idx] = 1
    return kk02

@njit(parallel=True)
def calcular_vecinos_paralelo(void2, c1, b1, x_min, x_max, y_min, y_max, z_min, z_max):
    n = len(void2)
    mpossc = np.full((n, 9), -1, dtype=np.int32)
    mposic = np.full((n, 8), -1, dtype=np.int32)

    for i in prange(n):
        idx = void2[i]
        x = int(idx - c1 * int(idx / c1) - b1 * (int((idx - c1 * int(idx / c1)) / b1)))
        y = int(idx / c1)
        z = int((idx - c1 * int(idx / c1)) / b1)

        d1d1 = [-1, 0, 1]
        conta = 0
        conta2 = 0

        for ab in d1d1:
            for abc in d1d1:
                # mpossc
                xx = x + ab
                yy = y + 1
                zz = z + abc
                if x_min <= xx <= x_max and y_min <= yy <= y_max and z_min <= zz <= z_max:
                    mpossc[i, conta] = xx + c1 * yy + b1 * zz
                conta += 1

                # mposic
                if not (ab == 0 and abc == 0):
                    xx = x + ab
                    yy = y
                    zz = z + abc
                    if x_min <= xx <= x_max and z_min <= zz <= z_max:
                        mposic[i, conta2] = xx + c1 * yy + b1 * zz
                    conta2 += 1

    return mpossc, mposic


@njit
def elegir_direccion(probabilidades, r):
    p12 = np.zeros(10)
    for i in range(9):
        p12[i+1] = p12[i] + probabilidades[i]
    
    if p12[9] == 0.0:
        return -1  # No hay probabilidades válidas
    
    # Normalizar
    for i in range(10):
        p12[i] /= p12[9]
    
    r = np.random.rand()  # Usar rand de NumPy, compatible con Numba
    
    for i in range(9):
        if r >= p12[i] and r < p12[i+1]:
            return i
    
    return -1  # Si no entra en ningún rango, retorna -1

@njit
def contar_estados(modelo):
    mov = 0
    ext = 0
    for i in range(modelo.shape[0]):
        if modelo[i, 3] == 2:
            mov += 1
        elif modelo[i, 3] == 1:
            ext += 1
    return mov, ext


@njit(parallel=True)
def procesar_voids_paralelo(
    void2, bmodel, c1, b1,
    x_min, x_max, y_min, y_max, z_min, z_max,
    d12, n, mvc
):
    num = len(void2)
    # Ahora movemos 19 valores por fila (voids_data) y las 9 posiciones
    movimientos = np.zeros((num, 19), dtype=np.float64)
    posiciones  = np.full((num,  9), -1, dtype=np.int32)
    destinos    = np.full(num,    -1, dtype=np.int32)
    m22         = np.full(num,    -1, dtype=np.int32)

    for i in prange(num):
        mm = void2[i]
        # reconstruir coordenadas
        y_idx = mm // c1
        z_idx = (mm - c1*y_idx) // b1
        x_idx = mm - c1*y_idx - b1*z_idx

        # límite
        if not (x_min <= x_idx <= x_max and
                y_min <= y_idx <= y_max and
                z_min <= z_idx <= z_max):
            continue

        # calcular pos_above
        pos_above = np.full(9, -1, dtype=np.int32)
        cnt = 0
        for dx in (-1,0,1):
            for dz in (-1,0,1):
                x2, y2, z2 = x_idx+dx, y_idx+1, z_idx+dz
                if (x_min <= x2 <= x_max and
                    y_min <= y2 <= y_max and
                    z_min <= z2 <= z_max):
                    pos_above[cnt] = x2 + c1*y2 + b1*z2
                cnt += 1

        # calcular pos_level
        pos_level = np.full(8, -1, dtype=np.int32)
        cnt2 = 0
        for dx in (-1,0,1):
            for dz in (-1,0,1):
                if dx==0 and dz==0: 
                    continue
                x2, y2, z2 = x_idx+dx, y_idx, z_idx+dz
                if (x_min <= x2 <= x_max and
                    z_min <= z2 <= z_max):
                    pos_level[cnt2] = x2 + c1*y2 + b1*z2
                cnt2 += 1

        # Llama a tu search_voids original, en numba
        voids_data, pos_ab = search_voids(bmodel, pos_above, pos_level)
        movimientos[i, :] = voids_data
        posiciones[i, :]  = pos_ab

        # Condición de extracción
        num_voids = int(voids_data[0])
        if bmodel[mm,3] == 1 and num_voids > mvc:
            # elegir primer vacío (puedes usar tu lógica de probabilidades tras esto)
            for j in range(9):
                # voids_data[1+j] == 1 indica vacío
                if voids_data[1 + j] == 1.0:
                    destinos[i] = pos_above[j]
                    break
            m22[i] = num_voids

    return m22, destinos, movimientos, posiciones