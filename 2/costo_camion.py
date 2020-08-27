# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:58:19 2020

@author: sofia.russmann
"""

f = open('../Data/camion.csv', 'rt')
headers = next(f)
headers
total = 0

for line in f:
    row = line.split(',')
    precio = round(float(row[1])*float(row[2]),2)
    total = total + precio
    
print(total)

f.close()