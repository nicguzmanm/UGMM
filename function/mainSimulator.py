
import numpy as np
import math as mt
import pandas as pd
import os
from function.translation import Move
from function.flowmarkIII import Flow # Si se desea cambiar el flowmark, cambiar esta linea
import traceback

# def sim(N, MVC, range_ext, input_ext, bm, dp, stress_activate, fold, ruta, dcell, savelist, update_progress=None, stop_sim = False):
def sim(N, MVC, dp_tonnage_period, final_period, bm, dp, stress_activate, fold, ruta, dcell, savelist, update_progress=None, stop_sim = False):
    try:
        # Setear barra de progreso a 0
        if update_progress:
            progress_value = 0
            update_progress(int(round(progress_value,0)))
        
        """ Paramaetros iniciales """
        # Parametros de la simulacion
        method = 1
        min_ext = 0
        max_ext = 1e50
        step_ext = 1
        num_sim = 1
        dp_width = 4
        dp_length = 4
        dcell = tuple(dcell)

        # Constantes del modelo
        init_N = N
        init_MVC = MVC
        final_N = N 
        final_MVC = MVC
        
        # Constantes de esfuerzo
        size = [2.85, 1.59, 1.27, 0.65, 0.3]
        fu = [1.0, 0.91, 0.78, 0.22, 0.05]
        vload = 1

        # Se definen los periodos que el usuario guardara, en una lista con true y false
        period_save = [None] * sum(savelist)
        
        # Indices que se usan para guardar informacion
        num_iter = 0
        num_iter_saved = 0

        # Variables retornadas de la simulacion, que son mostradas en la pestaña de resultados
        if stress_activate:
            esf=[None] * int(sum(savelist)) # Variable retornada (Esfuerzos por periodo)
        else:
            esf=['-'] * int(sum(savelist)) # Variable retornada al no seleccionar el modelo de esfuerzo
                                            # (Esfuerzos por periodo)
        mean_grade = [0] * int(sum(savelist)) # Variable retornada (Ley media por periodo)
        tonnage = [0] * int(sum(savelist)) # Variable retornada (Tonelada por periodo)
        fine_metal = [0] * int(sum(savelist))
        
        # Alerta, que indica si la simulacion termino con error o si termino exitosamente o termino
        # por indicaciones del usuario
        error = 0

        """ Revisa si existe la carpetra report y guarda la carpeta donde estara el output de la simulacion """
        if not os.path.exists(f'{ruta}\\{fold}'):
            os.makedirs(f'{ruta}\\{fold}')

        # Nombre base para las subcarpetas
        simfolder_base = os.path.join(f'{ruta}\\{fold}', "sim")
        simfolder = f"{simfolder_base}1"
        i = 2

        # Verificar si la subcarpeta existe y generar un nombre único
        while os.path.exists(simfolder):
            simfolder = f"{simfolder_base}{i}"
            i += 1

        # Crear la subcarpeta única
        os.makedirs(simfolder)
        
        """ Lee el directorio y acepta csv/xlsx/txt para mayor compatibilidad del software"""

        # Carga de modelo de bloques
        file_extension = os.path.splitext(bm)[1].lower()
        if file_extension == '.csv' or file_extension == '.txt':
            try:
                block_model = pd.read_csv(bm, delimiter=',', skiprows=0, header=0)
                if block_model.shape[1] == 1:
                    raise ValueError("Archivo no separado por comas")
                
            except:
                block_model = pd.read_csv(bm, sep=r'\s+', skiprows=0, header=0)
                print(block_model.columns)

        elif file_extension == '.xlsx':
            block_model = pd.read_excel(bm, header=0, skiprows=0)
        
        block_model = block_model.to_numpy()

        """ Detectar irregularidades en X, Y y Z """

        x_coords = np.unique(block_model[:,0])
        y_coords = np.unique(block_model[:,1])
        z_coords = np.unique(block_model[:,2])

        irreg = 0
        
        # Verificación de planos en X
        for xval in x_coords:
            plano_yz = block_model[block_model[:, 0] == xval][:, 1:3]  # Fijar X, ver Y y Z
            esperado_yz = np.array(np.meshgrid(y_coords, z_coords)).T.reshape(-1, 2)
            if len(np.unique(plano_yz, axis=0)) != len(esperado_yz):
                irreg += 1
        # Verificación de planos en Y
        for yval in y_coords:
            plano_xz = block_model[block_model[:, 1] == yval][:, [0, 2]]  # Fijar Y, ver X y Z
            esperado_xz = np.array(np.meshgrid(x_coords, z_coords)).T.reshape(-1, 2)
            if len(np.unique(plano_xz, axis=0)) != len(esperado_xz):
                irreg += 1
        # Verificación de planos en Z
        for zval in z_coords:
            plano_xy = block_model[block_model[:, 2] == zval][:, 0:2]  # Fijar Z, ver X y Y
            esperado_xy = np.array(np.meshgrid(x_coords, y_coords)).T.reshape(-1, 2)
            if len(np.unique(plano_xy, axis=0)) != len(esperado_xy):
                irreg += 1

        # Por el momento solo notifica, pronta implementacion relleno del modelo, para el funcionamiento de modelos irregulares
        if irreg > 3:
            print('Modelo de bloque es irregular')
        else:
            print('Modelo de bloques es regular')
        
        block_model, origen_x, origen_y, origen_z = Move.translate_model(block_model)

        # Carga de los draw_points de extraccion
        draw_points = np.loadtxt(dp, dtype=str, delimiter=" ", skiprows=1)
        if draw_points.ndim == 1:
            draw_points = draw_points.reshape(1, -1)
        
        # Convertir coordenadas a numeros
        dp_coords = draw_points[:, [1, 2, 3]].astype(float)
        dp_coords = Move.translate_points(dp_coords, origen_x, origen_y, origen_z)
        
        # Extraer las coordenadas de forma individual
        dp_x = dp_coords[:, 0]
        dp_y = dp_coords[:, 1]
        dp_z = dp_coords[:, 2]
    
        # Calculo de tonelaje total
        total_tonnage = dp_tonnage_period * len(dp_coords)

        block_model[:, [1, 2]] = block_model[:, [2, 1]]
        dp_coords[:, [1, 2]] = dp_coords[:, [2, 1]]

        # Calculo del incremento segun las veces que se itere """
        # Cantidad de true (sum(savelist)) = (max_ext / ext) + 1
        
        inc_progress = ( dp_tonnage_period + 165 ) * len(dp_coords) * sum(savelist) # incremento en la barra de progreso
        
        
        """ Inicio de Simulacion"""

        for i in range(num_sim):

            # Inicializar variables
            period = 1
            model_len = len(block_model)

            # Estados
            old_blocks = []
            new_blocks = []

            while init_MVC <= final_MVC:

                while init_N <= final_N:
                    
                    while period <= final_period:
                        # Si el usuario selecciono guardar el periodo se realizara la simulacion de ese periodo
                        if savelist[num_iter]:
                            
                            period_save[num_iter_saved] = period
                            
                            #----------------------------------------------------------------------------------------------------------------------------------
                            progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                            if stop_requested:
                                return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
                            #----------------------------------------------------------------------------------------------------------------------------------
                            
                            # ¿Se elimina o no?
                            total_tonnage = dp_tonnage_period * len(dp_coords)

                            # Actualizar las extracciones
                            extractions = min_ext if period == 1 else min_ext + 1

                            # Variable para guardar bloques extraidos por periodo
                            blocks_per_period = []

                            while extractions <= max_ext:
                                
                                print('Período = ', period)
                                print('Extracciones = ', extractions)

                                # Recuperar las coordenadas de los bloques
                                x = block_model[:, 0]
                                y = block_model[:, 1]
                                z = block_model[:, 2]

                                # Maximos de cada coordenada
                                min_x, max_x = min(x), max(x)
                                min_y, max_y = min(y), max(y)
                                min_z, max_z = min(z), max(z)
                                
                                #----------------------------------------------------------------------------------------------------------------------------------
                                progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                                if stop_requested:
                                    return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
                                #----------------------------------------------------------------------------------------------------------------------------------
                                
                                # Simulacion flowmark
                                flow_outputs = Flow.draw(
                                    bmodel=block_model,
                                    PE=dp_coords,
                                    dcell=dcell,
                                    ancho=dp_width,
                                    largo=dp_length,
                                    n=N,
                                    m=3,
                                    mvc=MVC,
                                    extractions=extractions,
                                    simula=None,
                                    wr=-99
                                )
                                
                                # Recuperar el modelo despues del flujo
                                flow_block_model = flow_outputs[0]

                                # Índice y estado de los bloques:
                                index_x = [n for n in range(model_len) if np.all(y[n] == dp_y + dcell[1])]
                                index_y = [n for n in range(model_len) if np.all(x[n] == dp_x + dcell[0])]
                                index_z = [n for n in range(model_len) if np.all(z[n] == dp_z + dcell[2])]

                                state_x = flow_block_model[index_x, 3].copy()
                                state_y = flow_block_model[index_y, 3].copy()
                                state_z = flow_block_model[index_z, 3].copy()

                                # Posición de los bloques vacíos y en movimiento:
                                voids_and_movements = []
                                for k in range(len(flow_block_model)):
                                    if (flow_block_model[k, 3] == 1) or (flow_block_model[k, 3] == 2):
                                        voids_and_movements.append(k)

                                #----------------------------------------------------------------------------------------------------------------------------------
                                progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                                if stop_requested:
                                    return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
                                #----------------------------------------------------------------------------------------------------------------------------------
                                
                                # Hallar los bloques que han ingresado:
                                new_blocks = np.where(flow_block_model[:, 3] == 1)[0].tolist()

                                # Identificar los bloques con estado 1:
                                blocks_id = list(set(new_blocks) - set(old_blocks))

                                # Guardar bloques extraídos esta extracción:
                                blocks_per_period = blocks_per_period + blocks_id
                                
                                # Añadir el período de los bloques:
                                flow_block_model[blocks_id, 11] = period
                                
                                # Actualizar el listado de bloques:
                                old_blocks = new_blocks.copy()

                                # Actualizar la extracción:
                                extractions += step_ext

                                #***************************************************************************************************
                                """ Modelo de Esfuerzo """
                                if stress_activate: # Si el usuario chequea el modelo de esfuerzo se ejecuta la funcion stress
                                    swell = 0.0  # seditest
                                    empuje = 0.994
                                    d = 2
                                    xl = int(max(block_model[:, 0]) / d)
                                    yl = int(max(block_model[:, 1]) / d)
                                    zl = int(max(block_model[:, 2]) / d)
                                    
                                    massmodel = block_model.copy()
                                    
                                    # Cálculos de distancias
                                    m1 = d
                                    m2 = d * mt.sqrt(2)
                                    m3 = d * mt.sqrt(3)
                                    mdistance = np.array([m3, m2, m3, m2, m1, m2, m3, m2, m3])
                                    
                                    # Generar índices únicos
                                    xx = np.unique((block_model[:, 0] / d) + 1)
                                    yy = np.unique((block_model[:, 1] / d) + 1)
                                    zz = np.unique((block_model[:, 2] / d) + 1)
                                    b2 = len(xx)
                                    c2 = len(zz) * b2
                                    
                                    # Masas iniciales
                                    mask = block_model[:, 3] != 1
                                    massmodel[mask, 10] = (block_model[mask, 9] / (1 + swell)) * (d ** 3) * 9.8 / 4 / 1000
                                    
                                    # Baja sumando masas superiores sobre las inferiores
                                    pox = -np.ones(9, dtype=int)
                                    pond = np.zeros(9)
                                    
                                    for mii in range(len(block_model) - 1, -1, -1):
                                        #----------------------------------------------------------------------------------------------------------------------------------
                                        # Actualizar progreso dentro de la funcion stress
                                        progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                                        if stop_requested:
                                            return esf, period_save, tonnage, mean_grade, simfolder, error
                                        #----------------------------------------------------------------------------------------------------------------------------------
                                        
                                        if massmodel[mii, 3] != 1:
                                            # Cálculo de índices de los bloques vecinos
                                            pox[0] = int((massmodel[mii, 0] / d - 1) + b2 * (massmodel[mii, 2] / d + 1) + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[1] = int((massmodel[mii, 0] / d) + b2 * (massmodel[mii, 2] / d + 1) + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[2] = int((massmodel[mii, 0] / d + 1) + b2 * (massmodel[mii, 2] / d + 1) + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[3] = int((massmodel[mii, 0] / d - 1) + b2 * (massmodel[mii, 2] / d) + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[4] = int((massmodel[mii, 0] / d) + b2 * (massmodel[mii, 2] / d) + c2 * (massmodel[mii, 1] - d) / d - 1)
                                            pox[5] = int((massmodel[mii, 0] / d + 1) + b2 * (massmodel[mii, 2] / d) + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[6] = int((massmodel[mii, 0] / d - 1) + b2 * (massmodel[mii, 2] / d - 1) + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[7] = int((massmodel[mii, 0] / d) + b2 * (massmodel[mii, 2] - d) / d + c2 * (massmodel[mii, 1] / d - 1))
                                            pox[8] = int((massmodel[mii, 0] / d + 1) + b2 * (massmodel[mii, 2] / d - 1) + c2 * (massmodel[mii, 1] / d - 1))
                                            
                                            # Validar límites y bloques existentes
                                            valid_pox = np.clip(pox, 0, len(block_model) - 1)
                                            
                                            # Calcular la distancia total
                                            valid_pox_mask = valid_pox != -1
                                            totaldist = np.sum(mdistance[valid_pox_mask])
                                            
                                            # Calcular los pesos (pond)
                                            pond[valid_pox_mask] = mdistance[valid_pox_mask] / totaldist
                                            
                                            # Actualizar masas de bloques vecinos (usando np.add.at para eficiencia)
                                            for i, p in enumerate(valid_pox):
                                                if p != -1 and massmodel[p, 3] != 1:
                                                    np.add.at(massmodel[:, 10], p, massmodel[mii, 10] * pond[i] * empuje)
                                        else:
                                            massmodel[mii, 10] = 0
                                    # Visualización de esfuerzo en 2D
                                    esfuerzos = np.zeros((yl + 1) * (xl + 1))
                                    valid_mask = massmodel[:, 2] == 10
                                    esfuerzos[:np.sum(valid_mask)] = massmodel[valid_mask, 10]
                                    
                                    # Esfuerzo medio en la base
                                    base = 2 * (xl + 1) * (zl + 1)
                                    meanSV = np.mean(massmodel[base:base + (xl + 1) * (zl + 1), 10])

                                    stresses, esf[num_iter] = massmodel, meanSV
                                    np.savetxt(f'{simfolder}\\finalmodel1a.txt', stresses, fmt='%.2f')
                                #***************************************************************************************************

                                #----------------------------------------------------------------------------------------------------------------------------------
                                progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                                if stop_requested:
                                    return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
                                #----------------------------------------------------------------------------------------------------------------------------------
                                
                                # Calcular tonelajes:
                                density = flow_block_model[blocks_per_period, 9]
                                grade = flow_block_model[blocks_per_period, 8]
                                block_volume = dcell[0] * dcell[1] * dcell[2]
                                tonnage[num_iter_saved] = float((np.sum(density * block_volume)))
                                fine_metal[num_iter_saved] = float(np.sum(grade / 100 * block_volume))
                                mean_grade[num_iter_saved] = fine_metal[num_iter_saved] / tonnage[num_iter_saved] * 100

                                #----------------------------------------------------------------------------------------------------------------------------------
                                progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                                if stop_requested:
                                    return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
                                #----------------------------------------------------------------------------------------------------------------------------------
                                
                                
                                # Comprobar si el periodo ya cumplio el tonelaje pedido
                                if tonnage[num_iter_saved] > total_tonnage:

                                    # Exportar un archivo con los bloques extraídos por período:
                                    filtered_blocks = flow_block_model[blocks_per_period]
                                    
                                    filt_b = pd.DataFrame(filtered_blocks.copy())
                                    flow_bm = pd.DataFrame(flow_block_model.copy())

                                    # Exportar el modelo actualizado:
                                    head = ["x", "y", "z", "state", "d50", "id", "dist", "distacum", "grade", "dens", "mi","period"]
                                    filt_b.to_csv(f'{simfolder}\\bloques_extraidos_periodo{period}_{os.path.basename(simfolder)}.csv', header= head, index= False)
                                    flow_bm.to_csv(f'{simfolder}\\modelo_actualizado_{period}_{os.path.basename(simfolder)}.csv', header= head, index=False)
                                    
                                    break

                                # Actualizar el modelo de bloques:
                                block_model = flow_block_model
                                # *********************************************Salida******************************************************
                                #----------------------------------------------------------------------------------------------------------------------------------
                                progress_value, stop_requested = update_progress_check_stopped(progress_value, sum(tonnage)/inc_progress, update_progress, stop_sim)
                                if stop_requested:
                                    return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
                                #----------------------------------------------------------------------------------------------------------------------------------
                                print(tonnage)
                                print(progress_value)
                            num_iter_saved += 1
                            
                        num_iter +=1
                        period += 1
                    init_N += 1
                init_MVC += 1
                print(progress_value)
        return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
    except Exception as e:
        traceback.print_exc()
        error = 1
        return esf, period_save, tonnage, mean_grade, simfolder, error, fine_metal
        

def update_progress_check_stopped(progress_value, inc_progress, update_progress, stop_sim):
    progress_value = inc_progress * 100
    update_progress(int(progress_value))

    # Verificar si se debe detener la simulación
    if stop_sim():  # Si el usuario solicita parar, se devuelve el valor sin seguir
        return progress_value, True  # Retorna True para indicar que se detuvo
    return progress_value, False  # Si no se detuvo, sigue normalmente

def ordenar_modelo(df):
    
    # Intercambiar los valores de las columnas 'y' y 'z'
    # df[['y', 'z']] = df[['z', 'y']]

    # Asegurar que las columnas necesarias estén presentes
    if not all(col in df.columns for col in ['x', 'y', 'z', 'id']):
        raise ValueError("El archivo debe contener las columnas 'x', 'y', 'z', y 'id'.")

    # Ordenar las filas por y, luego por z, y luego por x
    df_sorted = df.sort_values(by=["y", "z", "x"]).reset_index(drop=True)

    # Reasignar la columna id con valores correlativos
    df_sorted["id"] = np.arange(1, len(df_sorted) + 1)

    # Guardar el DataFrame ordenado en un nuevo archivo CSV (opcional)
    # Cambia 'archivo_ordenado.csv' por la ruta deseada
    return df_sorted
