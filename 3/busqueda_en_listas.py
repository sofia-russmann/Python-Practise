# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:53:47 2020

@author: sofia.russmann
"""

def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0
    print(i)
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si entontramos a e
            pos = i  # guardamos su posición
            if z==e:
                pos = i
            break    # y salimos del ciclo
        i += 1       
    return pos


#resta que devuelva el ultimo

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
        ...
    return m

#resta resolver 0

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el minimo de los elementos a medida que recorro la lista. 
    m = 9999999999 # Lo inicializo en 999999999
    for e in lista: # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
        ...
    return m




