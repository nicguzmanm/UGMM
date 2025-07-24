#orden del modelo de bloque

import pandas as pd
import numpy as np

# Cargar el archivo CSV con separación por espacios
# Cambia 'archivo.csv' por la ruta real del archivo
def orden(block_model):
    columnas = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi", "period"]
    df = pd.DataFrame(block_model, columns=columnas)
    # Intercambiar los valores de las columnas 'y' y 'z'
    df[['y', 'z']] = df[['z', 'y']]
    
    # Asegurar que las columnas necesarias estén presentes
    if not all(col in df.columns for col in ['x', 'y', 'z', 'id']):
        raise ValueError("El archivo debe contener las columnas 'x', 'y', 'z', y 'id'.")
    
    # Ordenar las filas por y, luego por z, y luego por x
    df_sorted = df.sort_values(by=["y", "z", "x"]).reset_index(drop=True)
    
    # Reasignar la columna id con valores correlativos
    df_sorted["id"] = np.arange(1, len(df_sorted) + 1)
    return df_sorted.values


