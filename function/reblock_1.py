#Rebloqueo #

import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
class Generate():
    def __init__(self):
        pass
    def modelo_peque(block_model, tam_bloque):
        medio_bloque = tam_bloque / 2
        
        # Archivos
        columnas = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi", "period"]
        df = pd.DataFrame(block_model, columns=columnas)
        # Calcular espaciado real (por si hay saltos irregulares)
        espaciado_x = np.gcd.reduce(np.diff(np.sort(df["x"].unique()).astype(int)))
        espaciado_y = np.gcd.reduce(np.diff(np.sort(df["y"].unique()).astype(int)))
        espaciado_z = np.gcd.reduce(np.diff(np.sort(df["z"].unique()).astype(int)))
        # Crear malla XY
        z_min = df["z"].min() - (espaciado_z/2)
        z_max = df["z"].max() + (espaciado_z/2)
        x_min = np.floor(df["x"].min()) - (espaciado_x/2)
        x_max = np.ceil(df["x"].max())+ (espaciado_x/2)
        y_min = np.floor(df["y"].min())- (espaciado_y/2)
        y_max = np.ceil(df["y"].max())+ (espaciado_y/2)
        
        x_centros = np.arange(x_min + medio_bloque, x_max, tam_bloque)
        y_centros = np.arange(y_min + medio_bloque, y_max, tam_bloque)
        
        
        # # Ajustar rangos para agregar una celda más en cada borde
        # x_centros = np.arange(x_min + medio_bloque, x_max, tam_bloque)
        # y_centros = np.arange(y_min + medio_bloque, y_max, tam_bloque)
        # =============================
        # 1. TOPOGRAFÍA REAL POR CELDA
        # =============================
        topografia = {}
        for x in x_centros:
            for y in y_centros:
                x_ini, x_fin = x - medio_bloque, x + medio_bloque
                y_ini, y_fin = y - medio_bloque, y + medio_bloque
        
                puntos = df[(df["x"] >= x_ini) & (df["x"] < x_fin) &
                            (df["y"] >= y_ini) & (df["y"] < y_fin)]
        
                if not puntos.empty:
                    z_max = df["z"].max() + (espaciado_z/2)
                    z_max_red = np.floor(z_max / tam_bloque) * tam_bloque  # ⚠️ REDONDEA HACIA ABAJO
                    topografia[(x, y)] = z_max_red
                else:
                    topografia[(x, y)] = None  # sin datos
        # print("z max topo real= ", z_max)
        # ===================================================
        # 2. RELLENAR HUECOS USANDO PROMEDIO DE VECINOS
        # ===================================================
        topografia_completa = {}
        for x in x_centros:
            for y in y_centros:
                if topografia.get((x, y)) is not None:
                    topografia_completa[(x, y)] = topografia[(x, y)]
                else:
                    vecinos = []
                    for dx in [-tam_bloque, 0, tam_bloque]:
                        for dy in [-tam_bloque, 0, tam_bloque]:
                            if dx == 0 and dy == 0:
                                continue
                            vecino = (x + dx, y + dy)
                            if vecino in topografia and topografia[vecino] is not None:
                                vecinos.append(topografia[vecino])
                    if vecinos:
                        topografia_completa[(x, y)] = np.mean(vecinos)
                    else:
                        topografia_completa[(x, y)] = 0  # sin vecinos, plano
        
    
        # ========================================
        # 3. GENERAR TODOS LOS BLOQUES DENTRO DE LA CAJA
        # ========================================
        bloques = []
        z_centros_global = np.arange(z_min + medio_bloque, z_max, tam_bloque)
        
        for x in x_centros:
            for y in y_centros:
                for z in z_centros_global:
                    bloques.append([x, y, z])
        # Guardar resultado final
        df_bloques = pd.DataFrame(bloques, columns=["x", "y", "z"])
        # df_bloques.to_csv(archivo_modelo_final, index=False)
        # El modelo diluido original debe tener las columnas X, Y, Altura Acumulada y Ley_Cu
        df_bloques = df_bloques[
            (df_bloques["x"] >= x_min) & (df_bloques["x"] <= x_max) &
            (df_bloques["y"] >= y_min) & (df_bloques["y"] <= y_max)
        ].copy()
        # Asegúrate de que no haya valores nulos
        df_validos = df.dropna(subset=["state","d50","id","dist","distacum","grade","dens","mi", "period", "x", "y", "z"]).copy()
        
        # Árbol KD para encontrar puntos cercanos en 3D
        tree = cKDTree(df_validos[["x", "y", "z"]].values)
        
        # Buscar 5 vecinos más cercanos
        k = 5
        distancias, indices_vecinos = tree.query(df_bloques[["x", "y", "z"]].values, k=k)
        
        # Buscar el punto más cercano para cada bloque del nuevo modelo
        distancias_min, indice_cercano = tree.query(df_bloques[["x", "y", "z"]].values)
        if len(distancias.shape) == 1:
            distancias = distancias[:, np.newaxis]
            indices_vecinos = indices_vecinos[:, np.newaxis]
        # Asignar los valores de Ley_Cu desde el modelo original al nuevo modelo
        columnas_por_vecino = [ "dist", "state", "id", "d50","distacum", "mi", "period"]  # Usa el punto más cercano
        columnas_promediadas = ["grade","dens" ]             # Usa promedio ponderado
        # Si solo devuelve 1 vecino, convertirlo en 2D manualmente
        if k == 1:
            indices_vecinos = indices_vecinos[:, np.newaxis]
            distancias = distancias[:, np.newaxis]
        
        # Asignar columnas por vecino más cercano (índice 0)
        for col in columnas_por_vecino:
            if col in df_validos.columns:
                df_bloques[col] = np.take(df_validos[col].values, indice_cercano)
        
        # Asignar columnas por promedio ponderado inverso a distancia
        for col in columnas_promediadas:
            if col in df_validos.columns:
                valores = df_validos[col].values[indices_vecinos]  # shape (n, k)
                pesos = 1 / (distancias + 1e-6)                     # shape (n, k)
                promedio_ponderado = np.sum(valores * pesos, axis=1) / np.sum(pesos, axis=1)
                df_bloques[col] = promedio_ponderado
        
        # Reordenar columnas en el orden deseado
        columnas_ordenadas = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi", "period"]
        df_bloques = df_bloques[columnas_ordenadas]

        return df_bloques