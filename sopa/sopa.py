#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import

def ejes(linea):
    lista = linea.rstrip('\n').split(' ')
    x = int(lista[0])
    y = int(lista[1])
    return x, y

def lee_datos(nombre):
    ar = open(nombre)
    tablero = []
    palabras = []
    x, y = ejes(ar.readline())
    i = 0
    while i < x:
        linea = ar.readline().rstrip('\n')
        tablero.append(linea)
        i = i + 1
    cantidad =int( ar.readline().rstrip('\n'))
    i = 0
    while i < cantidad:
        linea = ar.readline().rstrip('\n')
        palabras.append(linea)
        i = i + 1
    return tablero, palabras   

def izq_der(tablero, palabra):
    for linea in tablero:
        if palabra in linea:
            return 'SI'
    return 'NO'

def proceso(tablero, palabras):
    for palabra in palabras:
        esta = izq_der(tablero, palabra)
        print(palabra, esta)

def genera_solucion(solucion, nombre):
    pass

if __name__ == "__main__":
    tablero, palabras = lee_datos('SOP.DAT')
    solucion = proceso(tablero, palabras)
    genera_solucion(solucion, 'SOP.RES')
