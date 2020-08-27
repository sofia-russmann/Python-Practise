# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:33:30 2020

@author: sofia.russmann
"""

camion = leer_camion('Data/camion.csv')
costo = sum([ s['cajones'] * s['precio'] for s in camion ])
costo

precios = leer_precios('Data/precios.csv')
valor = sum([ s['cajones'] * precios[s['nombre']] for s in camion ])
valor
