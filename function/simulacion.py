
import numpy as np

# Para trabajar con arreglos de datos:
import pandas as pd
# CÃ¡lculo de la fragmentaciÃ³n:
# from functions.BCCM import fragmentation

# CÃ¡lculo de la zona de movimiento:
# from functions.MovementZone import geometry

# TraslaciÃ³n de puntos y modelo al origen:
from translation import translate_model, translate_points
from optimizar import buscar_indices_nb, compute_tonnage_and_fines
# Funcionamiento del autÃ³mata celular:
from flowmarkI import draw
# from core.flowmarkI import draw1
# from core.old_versions.flowmark_III_remake import draw
from reblock_1 import generar_modelo_peque
from orden_modelo import orden
from scipy.spatial import distance_matrix
# CÃ¡lculo de esfuerzos:
# from functions.PLOAD import stress
import plotly.express as px
import webbrowser
import os
import time
tiempo_total_inicio = time.time()

# ParÃ¡metros de la simulaciÃ³n:
mining_method = 1           # Tipo de mÃ©todo de explotaciÃ³n
min_extraction = 0          # ExtracciÃ³n inicial
max_extraction = 1e100       # ExtracciÃ³n final
step_extraction = 1         # Paso de las extracciones
num_simulations = 1         # NÃºmero de simulaciones
tam_bloque = 2
block_dim = (tam_bloque,tam_bloque,tam_bloque)
# Constantes iniciales del modelo:
initial_N = final_N = 2
initial_MVC = final_MVC = 3
# ParÃ¡metros de esfuerzosâº:
vload = 1
size = [2.85, 1.59, 1.27, 0.65, 0.3]
fu = [1.0, 0.91, 0.78, 0.22, 0.05]

# ParÃ¡metros del punto de extracciÃ³n:
dp_width = 4
dp_length = 4


# Cargar el modelo de bloques:
block_model1 = np.loadtxt("model1.csv", dtype=float, delimiter=',', skiprows=1)
t_inicio_rebloqueo = time.time()
block_model2 = generar_modelo_peque(block_model1, tam_bloque)
t_fin_rebloqueo = time.time()
print(f"Tiempo del rebloqueo: {t_fin_rebloqueo - t_inicio_rebloqueo:.2f} segundos")
block_model = orden(block_model2)
block_model, origin_x, origin_y, origin_z = translate_model(block_model)


# Cargar los puntos de extracciÃ³n:
drawpoints = np.loadtxt("drawpoints1.csv", dtype=str, delimiter=',', skiprows=1)
if drawpoints.ndim == 1:
    drawpoints = drawpoints.reshape(1, -1)

# Convertir coordenadas a nÃºmeros:
drawpoints_coords = drawpoints[:, [1,2,3]].astype(float)
drawpoints_coords = translate_points(drawpoints_coords, origin_x, origin_y, origin_z)
# Filtrar solo los puntos vÃ¡lidos (columna 6 == '1')
valid_drawpoints_mask = drawpoints[:, 6] == '1'
drawpoints = drawpoints[valid_drawpoints_mask]
drawpoints_coords = drawpoints_coords[valid_drawpoints_mask]

# Extraer las coordenadas de forma individual:
drawpoints_x = drawpoints_coords[:, 0]
drawpoints_y = drawpoints_coords[:, 1]
drawpoints_z = drawpoints_coords[:, 2]

block_volume = block_dim[0] * block_dim[1] * block_dim[2]


# block_model[:, [1, 2]] = block_model[:, [2, 1]]
drawpoints_coords[:, [1, 2]] = drawpoints_coords[:, [2, 1]]
# Convertir drawpoints en DataFrame para facilitar el trabajoâ
drawpoints_df = pd.DataFrame({
    'codigo': drawpoints[:, 0],
    'x': drawpoints_coords[:, 0],
    'y': drawpoints_coords[:, 1],
    'z': drawpoints_coords[:, 2]
})
########################################
# Leer tonelaje objetivo desde archivo
df_periodos = pd.read_csv("periodo1.csv", index_col=0)
tonelaje_objetivo_por_periodo = {
    int(periodo): df_periodos[periodo].dropna().to_dict()
    for periodo in df_periodos.columns
}
final_period = len(tonelaje_objetivo_por_periodo)          # Cantidad de perÃ­odos
# Realizar las simulaciones:
for i in range(num_simulations):
    
    bloques_por_id = {}            # ids Ãºnicos de bloques extraÃ­dos
    tonelaje_por_id = {}           # tonelaje acumulado por id
    ley_total_por_id = {}          # ley acumulada por id
    fines_por_id = {}              # metal fino por id
    ids_ya_registrados = set()
    # Inicializar variables:
    n = initial_N
    mvc = initial_MVC
    period = 1
    model_len = len(block_model)

    # Lista con los estados:
    old_blocks = []
    new_blocks = []

    # Bucle para actualizar la constante MVC:
    while mvc <= final_MVC:

        # Bucle para actualizar al constante N:
        while n <= final_N:
            
            # Bucle para actualizar el perÃ­odo:
            while period <= final_period:
                t_inicio_periodo = time.time()
                tonelaje_por_punto_objetivo = tonelaje_objetivo_por_periodo.get(period, {})
                tonelaje_por_punto = {codigo: 0 for codigo in drawpoints_df['codigo']}
                tonelaje_por_id = {}


                # Actualizar las extracciones:
                extractions = min_extraction if period == 1 else min_extraction + 1

                # Variable para guardar bloques extraidos por perÃ­odo:
                blocks_per_period = []
                # Bucle para actualizar las extracciones:
                while extractions <= max_extraction:
                    t_inicio_extraccion = time.time()
                    block_model_anterior = block_model.copy()
                    print('Peri­odo = ', period)
                    print('Extracciones = ', extractions)
                    puntos_activos_df = drawpoints_df[drawpoints_df['codigo'].isin([
                        codigo for codigo, tonelaje in tonelaje_por_punto.items()
                        if tonelaje < tonelaje_por_punto_objetivo.get(codigo, float('inf'))
                    ])]
                    t_puntos_activos= time.time()
                    print(f"Tiempo puntos activos {extractions}: {t_puntos_activos - t_inicio_extraccion:.2f} s")
                    # Si no hay puntos activos, romper el bucle
                    if puntos_activos_df.empty:
                        print("Todos los puntos han alcanzado su li­mite.")
                        break
                    
                    # Coordenadas de puntos activos
                    drawpoints_coords_activos = puntos_activos_df[['x', 'y', 'z']].to_numpy()
                    # Recuperar las coordenadas de los bloques:
                    x = block_model[:, 0]
                    y = block_model[:, 1]
                    z = block_model[:, 2]

                    # MÃ¡ximos de cada coordenada:
                    min_x, max_x = min(x), max(x)
                    min_y, max_y = min(y), max(y)
                    min_z, max_z = min(z), max(z)
                    t_antes_flujo = time.time()
                    print(f"Tiempo antes flujo {extractions}: {t_antes_flujo - t_inicio_extraccion:.2f} s")
                    # # CÃ¡lculo de la fragmentaciÃ³n:
                    # sizem = fragmentation(size, fu, vload)
                    # frag50 = (sizem[3] * 10) / (max_y - min_y)

                    # BÃºsqueda de vacÃ­os y cambios de estado:                  
                    flow_outputs = draw(
                        bmodel=block_model,
                        PE=drawpoints_coords_activos,
                        dcell=block_dim,
                        ancho=dp_width,
                        largo=dp_length,
                        n=n,                        
                        m=3,
                        mvc=mvc,
                        extractions=extractions,
                        simula=None,
                        wr=-99
                    )
                    t_despues_flujo = time.time()
                    print(f"Tiempo despues flujo {extractions}: {t_despues_flujo - t_inicio_extraccion:.2f} s")
                    # Recuperar modelo despuÃ©s del flujo:
                    flow_block_model = flow_outputs[0]

                    # 1) Mapea cada id extraÃ­do (state==1) a la primera posiciÃ³n donde aparece:
                    mask_ex = flow_block_model[:, 3] == 1
                    indices_ex = np.where(mask_ex)[0]
                    ids_ex = flow_block_model[indices_ex, 5].astype(int)
                    # Marcar el perÃ­odo actual en los bloques nuevos extraÃ­dos
                    # flow_block_model[indices_ex, 11] = period
                    
                    first_idx = {}
                    t_rec_model=time.time()
                    print(f"Tiempo recuperar modelo {extractions}: {t_rec_model - t_inicio_extraccion:.2f} s")
                    for pos, idv in zip(indices_ex, ids_ex):
                        if idv not in first_idx:
                            first_idx[idv] = pos
                    # 2) Preâacumula el tonelaje por id en un solo barrido:
                    dens_arr = flow_block_model[:, 9]  # densidad por bloque
                    vol = block_volume  # <- ya calculado antes
                    from collections import defaultdict
                    dens_sum = defaultdict(float)
                    for pos, idv in zip(indices_ex, ids_ex):
                        dens_sum[idv] += dens_arr[pos] * vol
                    
                    # 3) Extrae de golpe las coordenadas de los DP en un array Nx3:
                    dp_coords = drawpoints_df[['x', 'y', 'z']].to_numpy()
                    # Primero convierte a float32 tus coordenadas y objetivos:
                    coords_y    = block_model[:,1].astype(np.float32)
                    targets_y   = drawpoints_df['y'].to_numpy(dtype=np.float32)
                    offset_y    = float(block_dim[1])
                    
                    coords_x    = block_model[:,0].astype(np.float32)
                    targets_x   = drawpoints_df['x'].to_numpy(dtype=np.float32)
                    offset_x    = float(block_dim[0])
                    
                    coords_z    = block_model[:,2].astype(np.float32)
                    targets_z   = drawpoints_df['z'].to_numpy(dtype=np.float32)
                    offset_z    = float(block_dim[2])
                    
                    # Ahora llama a la versiÃ³n Numba:
                    index_x = buscar_indices_nb(coords_x, targets_x, offset_x)
                    index_y = buscar_indices_nb(coords_y, targets_y, offset_y)
                    index_z = buscar_indices_nb(coords_z, targets_z, offset_z)

                    state_x = flow_block_model[index_x, 3].copy()
                    state_y = flow_block_model[index_y, 3].copy()
                    state_z = flow_block_model[index_z, 3].copy()
                    
                   
                    # Hallar los bloques que han ingresado:
                    new_blocks = np.where(flow_block_model[:, 3] == 1)[0].tolist()
                    new_ids = set(flow_block_model[new_blocks, 5])  # IDs Ãºnicos de nuevos bloques
                    old_ids = set(flow_block_model[old_blocks, 5]) if old_blocks else set()
                    
                    ids_actuales = set(flow_block_model[flow_block_model[:, 3] == 1, 5])
                    ids_nuevos = ids_actuales - ids_ya_registrados
                    bloques_id_nuevos = [int(i) for i in ids_nuevos if not np.isnan(i)] 
                    # Crear una mÃ¡scara booleana para los bloques cuyo ID estÃ¡ en new_ids
                    mask_nuevos_ids = np.isin(flow_block_model[:, 5], list(ids_nuevos))
                    
                    # Asignar el perÃ­odo solo a esas filas
                    flow_block_model[mask_nuevos_ids, 11] = period

                    # print('\n')
                    # print('new_ids = ', new_ids)
                    # print('old_ids = ', old_ids)
                    # print(f'IDs nuevos agregados = {bloques_id_nuevos}')                             
                    # Actualizar el listado de bloques:
                    old_blocks = new_blocks.copy()
                    t_fin_extraccion = time.time()
                    print(f"Tiempo de extraccion {extractions}: {t_fin_extraccion - t_inicio_extraccion:.2f} s")

                    # Actualizar la extracciÃ³n:
                    extractions += step_extraction

                    # Calcular tonelajes:
                    
                    # ids de los bloques reciÃ©n extraÃ­dos
                    ids_arr = np.array(bloques_id_nuevos, dtype=np.int64)
                    
                    # Calcula tonelaje, fines y ley media de cada ID en JIT
                    tons_arr, fines_arr, ley_arr = compute_tonnage_and_fines(flow_block_model, ids_arr, block_volume)
                    t_dic1 = time.time()
                    print(f"diccionario1 tiempo {extractions}: {t_dic1 - t_inicio_extraccion:.2f} segundos")
                    # Actualiza tus diccionarios
                    # Preprocesar: crear un Ã­ndice booleano por cada ID solo una vez
                    ids_unicos, idx_inverso = np.unique(ids_arr, return_inverse=True)
                    
                    for i, idv in enumerate(ids_unicos):
                        mask = flow_block_model[:, 5] == idv
                        count_cells = np.sum(mask)
                    
                        # Filtrar Ã­ndices originales que corresponden a este idv
                        k_idx = np.where(idx_inverso == i)[0]
                    
                        # Sumamos directamente los valores de todos los k con este idv
                        bloques_por_id[idv]   = bloques_por_id.get(idv, 0) + count_cells
                        tonelaje_por_id[idv]  = tonelaje_por_id.get(idv, 0) + np.sum(tons_arr[k_idx])
                        fines_por_id[idv]     = fines_por_id.get(idv, 0) + np.sum(fines_arr[k_idx])
                        ley_total_por_id[idv] = ley_total_por_id.get(idv, 0) + np.sum(ley_arr[k_idx])
                    
                    # Actualizar los IDs ya registrados
                    ids_ya_registrados.update(bloques_id_nuevos)
                    t_dic = time.time()
                    print(f"diccionario tiempo {extractions}: {t_dic - t_inicio_extraccion:.2f} segundos")
                    if 'primeros_cambios' not in locals():
                        primeros_cambios = {}

                    for pos in indices_ex:
                        idv = int(flow_block_model[pos, 5])
                        x_b, y_b, z_b = flow_block_model[pos, 0:3]
                    
                        # Revisar si el bloque está dentro de alguna zona de influencia de los puntos activos
                        dentro_de_zona = False
                        for _, dp in puntos_activos_df.iterrows():
                            x_dp, y_dp, z_dp = dp[['x', 'y', 'z']]
                    
                            if (
                                (x_b >= x_dp - dp_width / 2 - block_dim[0]) and (x_b <= x_dp + dp_width / 2 + block_dim[0]) and
                                (z_b >= z_dp - dp_length / 2 - block_dim[2]) and (z_b <= z_dp + dp_length / 2 + block_dim[2]) and
                                (y_b >= y_dp) and (y_b <= y_dp + 2 * block_dim[1])
                            ):
                                dentro_de_zona = True
                                break
                    
                        if not dentro_de_zona:
                            continue  # Saltar bloque si no está en la zona de influencia
                    
                        # Clave única para evitar duplicados
                        clave_unica = f"{idv}_{x_b}_{y_b}_{z_b}"
                        if clave_unica in primeros_cambios:
                            continue
                    
                        # Coordenadas del bloque
                        coord = np.array([x_b, y_b, z_b])
                    
                        # Buscar el punto de extracción más cercano
                        diffs = dp_coords - coord
                        d2 = np.einsum('ij,ij->i', diffs, diffs)
                        j = np.argmin(d2)
                        punto = drawpoints_df.iloc[j, 0]
                    
                        # Guardar la información del bloque extraído
                        primeros_cambios[clave_unica] = {
                            "x": x_b,
                            "y": y_b,
                            "z": z_b,
                            "id": idv,
                            "densidad": flow_block_model[pos, 9],
                            "ley": flow_block_model[pos, 8],
                            "periodo": period,
                            "punto_extraccion": punto,
                            "extraccion": extractions,
                        }
                    
                        # Tonelaje acumulado por punto
                        tonelaje = dens_sum.get(idv, 0)
                        tonelaje_por_punto[punto] = tonelaje_por_punto.get(punto, 0) + tonelaje

                    t_bloques_nuevos = time.time()
                    print(f"index tiempo {extractions}: {t_bloques_nuevos - t_inicio_extraccion:.2f} segundos")
                    print("Tonelaje por punto de extraccion:")
                    for punto, t in tonelaje_por_punto.items():#############
                        print(f"  Punto {punto}: {t:.2f} t")####################
                    # Comprobar si continÃºa la extracciÃ³n:
                    extraccion_completa = all(
                        tonelaje_por_punto.get(codigo, 0) >= tonelaje_por_punto_objetivo.get(codigo, float('inf'))
                        for codigo in drawpoints_df['codigo']
                    )
                    t_fin_extraccion_punto = time.time()
                    print(f"Tiempo paso de extraccion {extractions}: {t_fin_extraccion_punto - t_inicio_extraccion:.2f} s")
                    if extraccion_completa:
                        # Exportar un archivo con los bloques extraÃ­dos por perÃ­odo:
                        # filtered_blocks = flow_block_model[blocks_per_period]
                        filtered_blocks = flow_block_model[:,11]==period
                        # col_names = 'x z y state d50 id dist distacum grade dens mi period'
                        # np.savetxt(f'bloques_extraidos_periodo{period}.txt', filtered_blocks, header=col_names, comments='')
                        # flow_block_model[flow_block_model[:, 11] > 0, 3] = 1
                        # Exportar el modelo actualizado:
                        col_names = 'x z y state d50 id dist distacum grade dens mi period'
                        np.savetxt(f'modelo_actualizado_periodo_{period}.txt', flow_block_model, header=col_names, comments='')
                        # ğ Exportar a Excel las primeras apariciones:
                        df_cambios = pd.DataFrame.from_dict(primeros_cambios, orient="index")
                        df_cambios.reset_index(inplace=True)
                        df_cambios.rename(columns={"index": "ID"}, inplace=True)
                        # FunciÃ³n para encontrar el punto de extracciÃ³n asociado
                        def encontrar_punto_extraccion(row, drawpoints_df):
                            distancias = np.sqrt(
                                (drawpoints_df['x'] - row['x'])**2 +
                                (drawpoints_df['y'] - row['y'])**2 +
                                (drawpoints_df['z'] - row['z'])**2
                            )
                            idx_min = distancias.idxmin()
                            return drawpoints_df.loc[idx_min, 'codigo']
                        
                        # Aplicar la funciÃ³n para asignar el punto de extracciÃ³n
                        df_cambios['punto_extraccion'] = df_cambios.apply(
                            lambda row: encontrar_punto_extraccion(row, drawpoints_df),
                            axis=1
                        )
                        
                        # ğ Final: Guardar Excel con la nueva columna
                        df_cambios.to_excel(f"bloques_extraidos_periodo_{period}.xlsx", index=False)
                        break
                    # Actualizar el modelo de bloques:
                    block_model = flow_block_model
                
                # Actualizar el perÃ­odo:
                column_names = ['x', 'y', 'z', 'state', 'd50', 'id', 'dist', 'distacum', 'grade', 'density', 'mi', 'period']
                df_model = pd.DataFrame(block_model, columns=column_names)
                column_names1 =  ['x', 'z', 'y', 'state', 'd50', 'id', 'dist', 'distacum', 'grade', 'density', 'mi', 'period']
                df_model1 = pd.DataFrame(block_model, columns=column_names1)
                fig = px.scatter_3d(
                    df_model1[df_model1['state'] == 2],  # Filtra si quieres solo bloques extraÃ­dos
                    x="x", y="y", z="z",               # AtenciÃ³n: estÃ¡s invirtiendo y/z para mejor visualizaciÃ³n
                    color="state",
                    color_continuous_scale="Viridis",
                    opacity=0.7,
                    title=f"Modelo de Bloques - Estado - Período {period}"
                )
                fig.update_traces(marker=dict(size=6))
                fig.update_layout(scene=dict(aspectmode="data"))
                fig.show()

                # # Guardar archivo HTML
                nombre_archivo = f"modelo_3d_interactivo_periodo{period}.html"
                fig.write_html(nombre_archivo)

                # Abrir automÃ¡ticamente en el navegador
                ruta_completa = os.path.abspath(nombre_archivo)
                webbrowser.open(f"file://{ruta_completa}")
                t_fin_periodo = time.time()
                print(f"Tiempo para el peri­odo {period}: {t_fin_periodo - t_inicio_periodo:.2f} segundos")

                period += 1
            
            block_model_df = pd.DataFrame(block_model, columns=['x', 'y', 'z', 'state', 'd50', 'id', 'dist', 'distacum', 'grade', 'density', 'mi', 'period'])

            # Actualizar constante N:
            n += 1
            
        # Actualizar la constante MVC:
        mvc += 1
        tiempo_total_fin = time.time()
        print(f"Tiempo total de simulacion: {tiempo_total_fin - tiempo_total_inicio:.2f} segundos")
        # Modelo de bloques diluido
        volumen_bloque = block_volume
        dp_coords_array = drawpoints_df[['x', 'y', 'z']].to_numpy()
        dmat = distance_matrix(dp_coords_array, dp_coords_array)
        np.fill_diagonal(dmat, np.inf)
        min_distancia = np.min(dmat)
        ancho_bloque = largo_bloque = min_distancia
        
        resultados_agregados = []
        altura_base_por_pe = {}  # Guarda la altura acumulada en Y por cada PE
        
        for (periodo, punto), grupo in df_cambios.groupby(['periodo', 'punto_extraccion']):
            tonelajes = grupo['densidad'] * volumen_bloque
            tonelaje_total = tonelajes.sum()
            densidad_prom = tonelaje_total / (volumen_bloque * len(grupo))
            ley_prom = np.average(grupo['ley'], weights=tonelajes)
            
            # Coordenadas del punto de extracción (se usan como base para cada bloque)
            pe_info = drawpoints_df[drawpoints_df['codigo'] == punto].iloc[0]
            x_pe, y_pe, z_pe = pe_info[['x', 'y', 'z']]
        
            # Determinar la altura del bloque
            altura = tonelaje_total / (ancho_bloque * largo_bloque * densidad_prom)
        
            # Altura base acumulada (inicia en 0 si es el primer bloque del PE)
            altura_base = altura_base_por_pe.get(punto, 0)
            y_base_bloque = y_pe + altura_base
        
            # Centroide ajustado (x, z se mantienen, y es al centro del bloque actual)
            y_centroide = y_base_bloque + altura / 2
        
            resultados_agregados.append({
                'periodo': periodo,
                'punto_extraccion': punto,
                'x_centroide': x_pe,
                'y_centroide': y_centroide,
                'z_centroide': z_pe,
                'ancho': ancho_bloque,
                'largo': largo_bloque,
                'altura': altura,
                'ley_promedio': ley_prom,
                'densidad_promedio': densidad_prom,
                'tonelaje_total': tonelaje_total
            })
        
            # Actualizar altura acumulada del PE para el siguiente bloque
            altura_base_por_pe[punto] = altura_base + altura
        
        # Exportar a Excel
        df_bloques_agregados = pd.DataFrame(resultados_agregados)
        df_bloques_agregados.to_excel("modelo_diluido.xlsx", index=False)
        print("✅ Archivo 'modelo_diluido.xlsx' generado con éxito.")