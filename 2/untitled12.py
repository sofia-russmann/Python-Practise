# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:02:04 2020

@author: sofia.russmann
"""
      
import csv

precios = {}  

with open('precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])

