# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:39:25 2020

@author: sofia.russmann
"""

camion = leer_camion('../Data/camion.csv')
costo = sum([ s['cajones'] * s['precio'] for s in camion ])
print(costo)
