# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:30:24 2020

@author: sofia.russmann
"""

a = [1, 2, 3, 4, 5]
#devuelve una nueva lista b con los elementos de a pero duplicados
b = [2*x for x in a]
# imprime [2, 4, 6, 8, 10]
print(b)

nombres = ['Edmundo', 'Juana']
#devuelve a pero con cada nombre de nombres en minusculas
a = [nombre.lower() for nombre in nombres]
print(a)

#'modificacion en cada item' 'for' 'item' ¿in' en 'lista'
#[<expresión> for <variable> in <secuencia>]

c = [1, -5, 4, 2, -2, 10]
d = [2*x for x in c if x > 0]
print(d)

#[<expresión> for <variable> in <secuencia>]

#[<expresión> for <variable> in <secuencia> if <condición>]
#ejemplo
#a = [s for s in camion if s['precio'] > 100 and s['cajones'] > 50 ]

#resultado = []
#for variable in secuencia:
    #if condición:
       #resultado.append(expresión)
       
       
       
       
       