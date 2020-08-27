# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:37:06 2020

@author: sofia.russmann
"""
# falta


def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while i<n:
    #while i<n and not tiene:
        if expresion[i] == 'a':
            return(tiene)
            #tiene = True
        i += 1
    #return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))