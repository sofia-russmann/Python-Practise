# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:47:06 2020

@author: sofia.russmann
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
d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345

#for k in d:
#    print('k =', k)


#for k in d:
#        print(k, '=', d[k])

items = d.items()

print(items)


for k, v in d.items():
        print(k, '=', v)

