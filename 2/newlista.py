# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:28:35 2020

@author: sofia.russmann
"""

registros = []  # Empezamos con una lista vacía

with open('../Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
        
        
        
    print(registros)