# Flujo del material
#este codigo ya NO realiza busqueda de bloques sino que calcula las coordenadas de cada bloque
#funciona con modelo de bloques en formato txt y csv

from function.intercambio import procesar_voids_paralelo, contar_estados, intercambiar_bloques_numba, actualizar_probabilidades, calcular_vecinos, calcular_indices_extraccion, calcular_vecinos_paralelo, elegir_direccion
from function.search import voids
import pandas as pd
from random import random
import numpy as np
import math as mt
from time import time
from itertools import repeat
#import matplotlib.pyplot as plt
#import matplotlib.colors
class Flow():
    def __init__(self):
        pass
    def draw(bmodel, PE, dcell, ancho, largo, n, m, mvc, extractions, simula, wr):
    #dcell: diametro de bloque con sus dimensiones (este caso 2 [m])
        t1 = time()
        d1x = dcell[0]
        d1y = dcell[1]
        d1z = dcell[2]
        size = [2.85, 1.59, 1.27, 0.65, 0.3]
        FU = [1.0, 0.91, 0.78, 0.22, 0.05]
        size2 = size * len(bmodel)
        FU2 = [FU] * len(bmodel)
        FU3 = FU2
    #distancias celdas superiores
        d2xz = mt.sqrt((d1x * d1x) + (d1z * d1z))
        d2xy = mt.sqrt((d1x * d1x) + (d1y * d1y))
        d2yz = mt.sqrt((d1y * d1y) + (d1z * d1z))
        d3 = mt.sqrt((d1x * d1x) + (d1y * d1y) + (d1z * d1z))
    #/d1: para normalizar y que vaya de 1 en 1 y no dcell en dcell (asi funciona codigo)
        x = list(set(bmodel[:,0] / d1x))
        y = list(set(bmodel[:,1] / d1y))
        z = list(set(bmodel[:,2] / d1z))
        a1 = 1
        b1 = len(x)
        c1 = len(z) * b1
        cc2 = 0
        h = max(bmodel[:,1])
        ul = 0
        void8 = np.zeros((len(bmodel),1))
    #probabilidad
        p1 = 0.2 / 2.5
        p2 = 0.3 / 2.5
        p3 = p1
        p4 = p2
        p5 = 0.5 / 2.5
        p6 = p2
        p7 = p1
        p8 = p2
        p9 = p1
        p01 = p1
        p02 = p2
        p03 = p3
        p04 = p4
        p05 = p5
        p06 = p6
        p07 = p7
        p08 = p8
        p09 = p9
        r = 0
        k = 0
        eee2 = 0
        eee3 = 0
        # d12 = [d3,d2xy,d3,d2yz,d1y,d2yz,d3,d2xy,d3]
        d12 = np.array([d3, d2xy, d3, d2yz, float(d1y), d2yz, d3, d2xy, d3], dtype=np.float64)
        #masafino = 0
        ext = extractions
        void = 0
        mpp = list(range(0,len(bmodel)))
        mposic = np.zeros((len(bmodel),8),dtype=int)#bloques = cota
        mpossc = np.zeros((len(bmodel),9),dtype=int)#bloques > cota
    #PE: punto de extraccion con sus respectivas dimensiones
        PEx = int(PE[0][0] / d1x)
        PEy = int(PE[0][1] / d1y)
        PEz = int(PE[0][2] / d1z)
    #ancho,largo: dimensiones del PE
        tp1 = int(largo / d1z)
        tp2 = int(ancho / d1x)
        c = 1
        d = 4
    #perten: es pertenencia, guarda hacia que PE esta asociado cada bloque (ayuda medir interaccion entre PE)
    #kk0: rango de posiciones de bloques coordenadas
    #define rango distancia x,y,z en que estara un bloque que se va a extraer
    #iezi: guarda bloques que se extraen para definir IEZ
    #-99: para iniciar el valor
        perten = -99 * np.ones((len(bmodel),1))
        kk0x = list(range(PEx,PEx + tp2))
        kk0y = list(range(PEy,PEy + 2))
        kk0z = list(range(PEz,PEz + tp1))
        kk0 = [[0,0,0]] * len(kk0x) * len(kk0y) * len(kk0z)
        kk02 = [0] * len(kk0)
        contador = 0
        pmpx = [max(kk0x),min(kk0x)]
        pmpz = [max(kk0z),min(kk0z)]
        iezi = [-99] * len(bmodel)
        kk02 = calcular_indices_extraccion(kk0x, kk0y, kk0z, a1, c1, b1, iezi)
    #extraido: guarda extracciones de tonelaje
        void2 = np.array(sorted(kk02))
        void2m = kk0
        extraido = [-99] * (len(void2) * ext + 0)
        extraido3 = np.array(np.zeros((1,9)))
        leyy = [-99] * (len(void2) * ext + 0)
        void9 = void8
        perten[void2] = 1 * np.ones((len(void2),1))
        abcdd = 0
        abcd1 = 0
        th = 0
        tiez = 0
    #for hace trabajo principal del codigo (razonamiento for en Anexos Matias Pereira (2020)
        for ij in range(1,len(PE)):
            PEx = int(PE[ij][0] / d1x)
            PEy = int(PE[ij][1] / d1y)
            PEz = int(PE[ij][2] / d1z)
            kk0x = list(range(PEx,PEx + tp2))
            kk0y = list(range(PEy,PEy + 2))
            kk0z = list(range(PEz,PEz + tp1))
            kk0 = [[0,0,0]] * len(kk0x) * len(kk0y) * len(kk0z)
            kk02 = [0] * len(kk0)
            contador = 0
            pmpx = [max(kk0x),min(kk0x)]
            pmpz = [max(kk0z),min(kk0z)]
            for kk in range(len(kk0y)):
                for ll in range(len(kk0x)):
                    for zzz in range(len(kk0z)):
                        kk0[contador] = [kk0x[ll],kk0y[kk],kk0z[zzz]]
                        kk02[contador] = a1 * kk0x[ll] + c1 * kk0y[kk] + b1 * kk0z[zzz]
                        contador = contador + 1
            b = np.array(kk02)
            bb = np.array(kk0)
            perten[kk02] = (ij + 1) * np.ones((len(kk02),1))
            void2 = np.concatenate((void2, b), axis=0)
            void2m = np.concatenate((void2m, bb), axis=0)
    #dilo: guarda intercambio de bloques (ayuda a que bloque se intercambio con cual)
        dilo = list(range(len(bmodel)))
        dilo2 = dilo
        leyex = bmodel[:,8]
        leyex2 = bmodel[:,8]
        frag = bmodel[:,4]
        frag2 = bmodel[:,4]
        extraido[0:len(void2)] = void2
        leyy[0:len(void2)] = bmodel[void2,8]
        eee = 0
        void5 = void2
        void3 = void2
        void4 = np.array(void2)
        bmodel[void2,3] = np.ones((1,len(void2)))
        #bmodel[:,9]=perten[:,0] #se omitio por codigo VerticalStress.py
        iiii = 1
        possc = [0] * 9
        posic = [0] * 8
        void6 = [-1] * 2
        audio = 0
        audio2 = 0
        void55 = np.array(void5)
        #bmodel[:,9]=perten[:,0] #se omitio por codigo VerticalStress.py
        abcd3 = 0
        abcdd2 = 0
    #d1d1: analiza la distancia (ayuda registrar que se esta moviendo alrededor del bloque)
    #-1 se esta moviendo en coord anterior al bloq, 0 misma coord del bloq, 1 coord siguiente al bloq
        mpossc, mposic = calcular_vecinos_paralelo(
            np.array(void2, dtype=np.int32),
            c1, b1,
            int(min(x)), int(max(x)),
            int(min(y)), int(max(y)),
            int(min(z)), int(max(z))
        )
        m22 = [1000]
    #ext-1: porque se habia hecho 1 ext antes
    #m22: guarda cantidad de vacios alrededor del vacio
        num_extraction = 0
        
        for i in repeat(None,ext - 1):
            p = 0
            v = 0
            a = np.array(void5)
            b = np.array(void3)
            # void4 = np.concatenate((void4,b),axis=0)
            # void4 = sorted(list(set(void4)))
            void4 = set(void4)
            void4.update(b)
            void4 = np.fromiter(void4, dtype=np.int32)  # Convierte a array solo si necesitas
            # void2 = np.concatenate((a, b), axis=0)
            # void2 = sorted(list(set(void2)))
            void2 = list(set(np.concatenate((a, b), axis=0)))
            void2.sort(key=lambda idx: bmodel[idx, 1], reverse=True)
            m22 = [None] * len(void2)
            void3 = void2
            bmodel[void2,3] = np.ones((1,len(void2)))
            v1 = 0
            eee2 = eee
            cota=list(set(bmodel[:,1]))
            
            m22_arr, destinos, mv_arr, pos_arr = procesar_voids_paralelo(
                np.array(void2, dtype=np.int32),
                bmodel,
                c1, b1,
                int(min(x)), int(max(x)),
                int(min(y)), int(max(y)),
                int(min(z)), int(max(z)),
                d12, n, mvc
            )
            
            # Ahora aplicamos tu lógica de intercambio sin perder nada:
            void2_i32 = np.array(void2, dtype=np.int32)

            for idx_i, origen in enumerate(void2_i32):
                mv  = mv_arr[idx_i]
                pos = pos_arr[idx_i]     # esto viene de Numba, es np.ndarray
                dest= destinos[idx_i]
            
                if m22_arr[idx_i] > mvc and np.prod(mv[1:10]) == 0:
                    probs     = actualizar_probabilidades(d12, n)
                    direccion = elegir_direccion(probs, np.random.rand())
                    if direccion != -1:
                        destino = pos[direccion]
                        if destino != -1:
                            # — Aquí haces las conversiones a int32 —
                            pos_i32  = np.array(pos,    dtype=np.int32)
                            idx_i32  = np.int32(idx_i)
                            dest_i32 = np.int32(destino)
            
                            # Llamada a Numba con tipos coincidentes
                            bmodel = intercambiar_bloques_numba(
                                bmodel,
                                void2_i32,
                                pos_i32,
                                idx_i32,
                                dest_i32
                            )
                            perten[destino] = perten[origen]
            
                            if 'bloques_nuevos_en_esta_iteracion' not in locals():
                                bloques_nuevos_en_esta_iteracion = set()
                            bloques_nuevos_en_esta_iteracion.add(destino)
            
                            if origen in void5:
                                lp = np.array([dilo[origen]])
                                iezi[int(lp)] = 1
                                void55 = np.concatenate((void55, lp), axis=0)
                                void55 = list(set(void55))
                                # void55.add(dilo[origen])  # Si void55 lo defines como set()
                                # void55 = np.array(list(void55), dtype=np.int32)
            
                            bmodel[origen,3]  = 2
                            bmodel[destino,3] = 1
                            void3[idx_i]      = destino
                            frag[origen]      = frag2[destino]

                        
            b = np.array(void3)
            boid4 = np.concatenate((void4,b),axis=0)
            boid4 = sorted(list(set(boid4)))
            void8[boid4] = 1 + void8[boid4]
            iiii = iiii + 1
            num_extraction += 1
        bloques_en_movimiento, bloques_extraidos = contar_estados(bmodel)
        
        print(f"[Extracción #{num_extraction}] En movimiento: {bloques_en_movimiento} | Extraídos: {bloques_extraidos}")
        flowmodel = bmodel
        blocksmoved = len(void4)
        flowmodel[:,8] = leyex
        flowmodel[:,4] = frag
        iii = 0
        t2 = time()-t1
        #print("tiempo flowmarkIII = " + str(round(t2, 2)) + " s")
        return flowmodel,void4,blocksmoved,num_extraction,void3