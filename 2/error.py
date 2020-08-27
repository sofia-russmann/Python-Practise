# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:33:27 2020

@author: sofia.russmann
"""

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')