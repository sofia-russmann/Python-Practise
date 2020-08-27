# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:57:37 2020

@author: sofia.russmann
"""

import csv

def leer_parque (nombre_archivo,parque):
   lista = []    
   with open (nombre_archivo,"rt",encoding = "utf8") as f:
             
       filas = csv.reader(f)
       encabezados = next(filas)
       
       for  fila in filas:
           
           diccionario = dict(zip(encabezados,fila))
           altura = float(diccionario["altura_tot"])
           if diccionario["espacio_ve"] ==parque:
               lista.append(diccionario)
               
       return lista

parque = 'GENERAL PAZ'

informe = leer_parque("../Data/arbolado-en-espacios-verdes.csv", parque)

