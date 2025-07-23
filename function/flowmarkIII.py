# Flujo del material
#este codigo ya NO realiza busqueda de bloques sino que calcula las coordenadas de cada bloque
#funciona con modelo de bloques en formato txt y csv


from function.search_voids import search_voids
import pandas as pd
from random import random
import numpy as np
import math as mt
from time import time
from itertools import repeat
#import matplotlib.pyplot as plt
#import matplotlib.colors

#genera el flujo de celdas vacias
#estados 0:fijo 1:vacio 2:en movimeinto 3:pueden moverse (4:finos pueden moverse)
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
        d12 = [d3,d2xy,d3,d2yz,d1y,d2yz,d3,d2xy,d3]
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
        for kk in range(len(kk0y)):
            for ll in range(len(kk0x)):
                for zzz in range(len(kk0z)):
                    kk0[contador] = [kk0x[ll],kk0y[kk],kk0z[zzz]]
                    kk02[contador] = a1 * kk0x[ll] + c1 * kk0y[kk] + b1 * kk0z[zzz]
                    iezi[kk02[contador]] = 1
                    contador = contador + 1
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
        for v in range(len(void2)):
            d1d1 = [-1,0,1]
            conta = 0
            conta2 = 0
            for ab in d1d1:
                for abc in d1d1:
                    possc[conta] = (void2m[v][0] + ab) * 1 + c1 * (void2m[v][1] + 1) + b1 * (void2m[v][2]+abc)
                    if (void2m[v][0] + ab) > max(x) or\
                    (void2m[v][0] + ab) < min(x) or\
                    (void2m[v][1] + 1) > max(y) or\
                    (void2m[v][1] + 1) < min(y) or\
                    (void2m[v][2] + abc) > max(z) or\
                    (void2m[v][2] + abc) < min(z):
                        possc[conta] = -1
                    conta = conta + 1
                    if ab == 0 and abc == 0:
                        conta2 = conta2 - 1
                    else:
                        posic[conta2] = (void2m[v][0] + ab) * 1 + c1 * (void2m[v][1]) + b1 * (void2m[v][2] + abc)
                        if (void2m[v][0] + ab) > max(x) or\
                        (void2m[v][0] + ab) < min(x) or\
                        (void2m[v][2] + abc) > max(z) or\
                        (void2m[v][2] + abc) < min(z):
                            posic[conta2] = -1
                    conta2 = conta2 + 1
            mpossc[void2[v],:] = possc
            mposic[void2[v],:] = posic
        m22 = [1000]
    #ext-1: porque se habia hecho 1 ext antes
    #m22: guarda cantidad de vacios alrededor del vacio
        num_extraction = 0
        for i in repeat(None,ext - 1):
            p = 0
            v = 0
            a = np.array(void5)
            b = np.array(void3)
            void4 = np.concatenate((void4,b),axis=0)
            void4 = sorted(list(set(void4)))
            void2 = np.concatenate((a, b), axis=0)
            void2 = sorted(list(set(void2)))
            m22 = [None] * len(void2)
            void3 = void2
            bmodel[void2,3] = np.ones((1,len(void2)))
            v1 = 0
            eee2 = eee
            cota=list(set(bmodel[:,1]))
            for cc in cota:
                cota_v=pd.DataFrame(bmodel[void3,1])
                voidc=list(cota_v[cota_v[0]==cc].index)
                void2c=[aux2 for aux2 in voidc] 
                #consulta si cambiaron los vacios y si supero la cota del vacío más alto
                #este if tiene la finalidad de que no recorra todas las cotas, si no que hasta exista propagación de vacios 
                if void3==void2 and max(bmodel[void3,1])<cc:
                    break
                else:
                    void2=void3
                for v1 in void2c:
                    if v1>len(bmodel):
                        
                        continue
                    else:
                        while v1 < len(void2):
                            d1d1 = [-1,0,1]
                            conta = 0
                            conta2 = 0
                #mm: guarda vacio usado en dicha iteracion
                #v22m: define un vector con las coord de cada bloq

                            for ab in d1d1:
                                    for abc in d1d1:
                                        mm = void2[v1]
                                        aic2 = mm
                                        v22m = [int(mm - c1 * int(mm/c1)-\
                                        b1 * (int((mm - c1 * int(mm / c1)) / b1))),\
                                        int(mm / c1),int((mm - c1 * int(mm / c1)) / b1)]
                                        possc[conta] = (v22m[0] + ab) * 1 + c1 * (v22m[1] + 1) + b1 * (v22m[2] + abc)
                                        if possc[conta] > len(bmodel) or (v22m[0] + ab) > max(x) or\
                                        (v22m[0] + ab) < min(x) or\
                                        (v22m[1] + 1) > max(y) or (v22m[1] + 1) < min(y) or\
                                        (v22m[2] + abc) > max(z) or\
                                        (v22m[2] + abc) < min(z):
                                            possc[conta] = -1
                                        conta = conta + 1
                                        if ab == 0 and abc == 0:
                                            conta2 = conta2 - 1
                                        else:
                                            posic[conta2] = (v22m[0] + ab) * 1 +\
                                            c1 * (v22m[1]) + b1 * (v22m[2] + abc)
                                            if possc[conta2] > len(bmodel) or\
                                            (v22m[0] + ab) > max(x) or\
                                            (v22m[0] + ab) < min(x) or\
                                            (v22m[2] + abc) > max(z) or (v22m[2] + abc) < min(z):
                                                posic[conta2] = -1
                                        conta2 = conta2 + 1
                            r = 0
                            
                            aux = search_voids(bmodel,possc,posic)
                            mv = aux[0]
                            m22[v1] = mv[0]
                            pos = aux[1]
                            if bmodel[void2[v1],3] == 1 and mv[0] > mvc:
                                audio2 = audio2 + 1
                #ve si todos los bloques superiores son vacios
                                if mv[1] + mv[2] + mv[3] + mv[4] + mv[5] + mv[6] + mv[7] + \
                                mv[8] + mv[9] == 9:
                                    #print('hola')
                                    r = 99
                                    pass
                #ve si al menos un bloque superior puede bajar?
                                if mv[1] * mv[2] * mv[3] * mv[4] * mv[5] * mv[6] * \
                                mv[7] * mv[8] * mv[9] == 0 :
                                    denominador = (d12[0] ** -n) + (d12[1] ** -n) + (d12[2] ** -n) +\
                                    (d12[3] ** -n) + (d12[4] ** -n) +\
                                    (d12[5] ** -n) + (d12[6] ** -n) + (d12[7] ** -n) + (d12[8] ** -n)
                                    p1 = (d12[0] ** -n) / denominador
                                    p2 = (d12[1] ** -n) / denominador
                                    p3 = (d12[2] ** -n) / denominador
                                    p4 = (d12[3] ** -n) / denominador
                                    p5 = (d12[4] ** -n) / denominador
                                    p6 = (d12[5] ** -n) / denominador
                                    p7 = (d12[6] ** -n) / denominador
                                    p8 = (d12[7] ** -n) / denominador
                                    p9 = (d12[8] ** -n) / denominador
                                    p01 = p1
                                    p02 = p2
                                    p03 = p3
                                    p04 = p4
                                    p05 = p5
                                    p06 = p6
                                    p07 = p7
                                    p08 = p8
                                    p09 = p9
                #se evita intercambio vacio-vacio
                #zero[im-1]==0: no se deberia estar ocupandose en esta condicion
                                zero = np.ones((9,1))
                                for im in range(1,10):
                                    if pos[im - 1] == -1 or mv[im] == 1 or zero[im - 1] == 0:
                                        if im == 1:
                                            p1 = 0
                                        if im == 2:
                                            p2 = 0
                                        if im == 3:
                                            p3 = 0
                                        if im == 4:
                                            p4 = 0
                                        if im == 5:
                                            p5 = 0
                                        if im == 6:
                                            p6 = 0
                                        if im == 7:
                                            p7 = 0
                                        if im == 8:
                                            p8 = 0
                                        if im == 9:
                                            p9 = 0
                                p12 = [0,p1,p1 + p2,p1 + p2 + p3,p1 + p2 + p3 + p4,p1 + p2 + p3 + p4 + p5,\
                                p1 + p2 + p3 + p4 + p5 + p6,\
                                p1 + p2 + p3 + p4 + p5 + p6 + p7,p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8,\
                                p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9]
                                
                                #print(p12)
                                p = random()
                                
                                for ii in range(9):
                                    if r < 1.0:
                                        p12=list(np.array(p12) / p12[9])
                                        if p12[9] == 0:
                                            print('hola')
                                            
                                        if p < p12[ii + 1] and p >= p12[ii]:
                                            dilo[void2[v1]] = dilo2[pos[ii]]
                                            # perten[pos[ii]] = perten[void2[v1]]
                                            # dilo2[pos[ii]] = void2[v1]
                                            # leyex[void2[v1]] = leyex2[pos[ii]]
                                            # leyex2[pos[ii]] = -99
                                            # Actualizar movimiento del bloque
                                            dilo[void2[v1]] = dilo2[pos[ii]]
                                            perten[pos[ii]] = perten[void2[v1]]
                                            dilo2[pos[ii]] = void2[v1]
                                        
                                            # Mover características del bloque
                                            leyex[void2[v1]] = leyex2[pos[ii]]
                                            frag[void2[v1]] = frag2[pos[ii]]
                                            frag2[pos[ii]] = 0  # Bloques de aire tienen fragmentación 0
                                        
                                            # Actualizar coordenadas del bloque en movimiento
                                            # bmodel[void2[v1], 0:3] = bmodel[pos[ii], 0:3]  # Nueva ubicación <-- Error
                                            # Cambiar el estado del bloque extraído a -1
                                            bmodel[pos[ii], 3] = -1  # Estado del bloque extraído
                                            
                                            # Guardar características del bloque extraído en una lista
                                            if 'extracted_blocks' not in locals():
                                                extracted_blocks = []
                                            extracted_blocks.append(bmodel[pos[ii]].copy())  # Guardar el bloque extraído
                                            # bmodel[pos[ii], 3] = 1  # Estado del bloque movido: "vacío"
                                            bmodel[void2[v1], 3] = 2  # Estado del bloque en movimiento
                                            for alau in void5:
                                                if void2[v1] == alau:
                                                    lp = np.array([dilo[void2[v1]]])
                                                    iezi[int(lp)] = 1
                                                    void55 = np.concatenate((void55,lp),axis=0)
                                                    void55 = list(set(void55))
                                            bmodel[void2[v1],3] = 2
                                            bmodel[pos[ii],3] = 1
                                            void3[v1] = pos[ii]
                                            # bmodel[pos[ii], 3] = -99  # Estado de bloque extraído
                                            # bmodel[pos[ii], 0:3] = [-99, -99, -99]  # Coordenadas fuera del rango
                                            frag[void2[v1]] = frag2[pos[ii]]    
                            p1 = p01
                            p2 = p02
                            p3 = p03
                            p4 = p04
                            p5 = p05
                            p6 = p06
                            p7 = p07
                            p8 = p08
                            p9 = p09                  
                            v1 = v1 + 1 
            eee4 = eee2 + 1
            b = np.array(void3)
            boid4 = np.concatenate((void4,b),axis=0)
            boid4 = sorted(list(set(boid4)))
            void8[boid4] = 1 + void8[boid4]
            iiii = iiii + 1
    #condicion if, solo para extraccion Panel Caving
    #wr: zona inactiva (de no movimiento)
    #num_extraction: guarda cantidad de extracciones por periodo definido por wr
    #si min(bmodel[void3, 0]) <= wr entonces termina la iteracion en flowmarkIII.py
            num_extraction += 1
            if (min(bmodel[void3, 0]) <= wr) and (wr != -99):
                #print("minX void3= " + str(min(bmodel[void3,0])))
                #print("maxY void3= " + str(max(bmodel[void3, 1])))
                print("Pasa a Wr= " + str(wr) + "!!!!!")
                break
        flowmodel = bmodel
        blocksmoved = len(void4)
        flowmodel[:,8] = leyex
        flowmodel[:,4] = frag
        iii = 0
        t2 = time()-t1
        #print("tiempo flowmarkIII = " + str(round(t2, 2)) + " s")
        return flowmodel,void4,blocksmoved,num_extraction,void3