# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:41:48 2020

@author: sofia.russmann
"""

#lista de tuplas (nombre, cajones) que indiquen 
#la cantidad de cajones de cada fruta tomando los datos de camion

nombre_cajones =[ (s['nombre'], s['cajones']) for s in camion ]