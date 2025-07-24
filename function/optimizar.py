from numba import njit
import numpy as np

@njit
def buscar_indices_nb(coords, targets, offset):
    # coords = array de float32
    # targets = array de float32
    # offset  = float
    n = coords.shape[0]
    m = targets.shape[0]
    out = np.empty(m, dtype=np.int64)
    for i in range(m):
        tgt = targets[i] + offset
        best = -1
        # búsqueda lineal (o binaria si coords está ordenado)
        for j in range(n):
            if coords[j] == tgt:
                best = j
                break
        out[i] = best
    return out

@njit
def calcular_tonelaje_y_finos(densidades, leyes, block_volume):
    tonelaje = np.sum(densidades * block_volume)
    fines = np.sum((leyes / 100) * densidades * block_volume)
    ley_media = (fines / tonelaje * 100) if tonelaje > 0 else 0
    return tonelaje, fines, ley_media

@njit
def compute_tonnage_and_fines(model, ids, block_volume):
    n_ids = ids.shape[0]
    tons  = np.zeros(n_ids, dtype=np.float64)
    fines = np.zeros(n_ids, dtype=np.float64)
    ley   = np.zeros(n_ids, dtype=np.float64)
    # Para cada ID
    for i in range(n_ids):
        idv   = ids[i]
        t_acc = 0.0
        f_acc = 0.0
        # Recorre todas las filas del modelo
        for j in range(model.shape[0]):
            if model[j,5] == idv:
                dens  = model[j,9]
                grade = model[j,8]
                ton   = dens * block_volume
                t_acc += ton
                f_acc += (grade/100.0) * ton
        tons[i]  = t_acc
        fines[i] = f_acc
        ley[i]   = (f_acc/t_acc*100.0) if t_acc > 0.0 else 0.0
    return tons, fines, ley

