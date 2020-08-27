# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:16:09 2020

@author: sofia.russmann
"""
#El error se resuelve imprimiendo el resultado

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

print(tiene_a('UNSAM 2020'))

print(tiene_a('abracadabra'))

print(tiene_a('La novela 1984 de George Orwell'))
