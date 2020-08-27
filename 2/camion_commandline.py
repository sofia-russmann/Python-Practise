# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:39:00 2020

@author: sofia.russmann
"""
# camion_commandline.py
import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
costo = costo_camion(nombre_archivo)
print('Costo total: ', costo)