#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import

def captura_dimension(ar):
    dimension = ar.readline().rstrip('\n').split(' ')
    dimension[0] = int(dimension[0])
    dimension[1] = int(dimension[1])   
    return dimension

def captura_centro(ar):
    centro = ar.readline().rstrip('\n').split(' ')
    centro[0] = int(centro[0])
    centro[1] = int(centro[1])   
    return centro

def de_str_int(lista, cantidad):
    j = 0
    while j < cantidad:
        lista[j] = int(lista[j])
        j = j + 1
    return lista

def lee_tablero(ar, dimension, centro):
    tablero = []
    i = 0
    while i < dimension[0]:
        lista = ar.readline().rstrip('\n').split(' ')
        lista = de_str_int(lista, dimension[1])
        tablero.append(lista)
        i = i + 1
    return tablero

def devuelve_fila(altura, columnas):
    lista = []
    i = 0
    while i < columnas + 2:
        lista.append(altura)
        i = i + 1
    return lista

def leer_datos(nombre):
    ar = open(nombre)
    dimension = captura_dimension(ar)
    centro = captura_centro(ar)
    tablero = lee_tablero(ar,dimension, centro)
    altura = tablero[dimension[0]-1][dimension[1]-1]
    ladera = []
    fila0 = devuelve_fila(altura, dimension[1])
    ladera.append(fila0)
    i = 0
    while i < dimension[0]:
        ladera.append([altura]+tablero[i]+[altura])
        i = i + 1
    ladera.append(fila0)    
    print(ladera)
    ar.close()

def estallo_volcan(ladera):
    pass

def genera_mapa(lava, nombre):
    pass

if __name__ == "__main__":
    ladera = leer_datos('VOLCAN.DAT')
    lava = estallo_volcan(ladera)
    genera_mapa(lava, 'VOLCAN.RES')

