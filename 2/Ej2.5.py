# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:02:12 2020

@author: sofia.russmann
"""

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    headers = next(f)
    headers
    total = 0
    for line in f:
        row = line.split(',')
        precio = round(float(row[1])*float(row[2]),2)
        total = total + precio
    return total
    
costo = costo_camion('../Data/camion.csv')
print('Costo total: ', costo)