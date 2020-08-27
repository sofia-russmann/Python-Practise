# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:34:41 2020

@author: sofia.russmann
Diccionarios
"""
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
next(filas)
fila = next(filas)

d = {
     'nombre' : fila[0],
     'cajones' : int(fila[1]),
     'precio'  : float(fila[2])
    }



cost = d['cajones'] * d['precio']

print(cost)