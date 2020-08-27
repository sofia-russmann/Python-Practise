# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:53:23 2020

@author: sofia.russmann
"""

medidas = [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(medidas)
