# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:28:03 2020

@author: sofia.russmann
"""

#devuelve la información como una lista de tuplas.


import csv

def costo_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
            
            
    return camion

costo = costo_camion('../Data/camion.csv')
print('Costo total: ', costo)