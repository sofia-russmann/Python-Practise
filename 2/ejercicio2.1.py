# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:39:02 2020

@author: sofia.russmann
"""

f = open('Data/camion.csv', 'rt')
headers = next(f).split(',')

for line in f: 
    row = line.split(',')
    print(row)
    
f.close()