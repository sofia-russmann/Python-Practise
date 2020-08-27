# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:31:39 2020

@author: sofia.russmann
"""

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

preguntar_edad('Sofia')