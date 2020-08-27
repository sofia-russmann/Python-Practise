# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:13:04 2020

@author: sofia.russmann
Tuplas

"""
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
next(filas)
fila = next(filas)

t = (fila[0], int(fila[1]), float(fila[2]))
print(t)

cost = t[1] * t[2]
print(t[1], t[2])
print(cost)