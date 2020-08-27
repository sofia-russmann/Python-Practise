# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:44:38 2020

@author: sofia.russmann
"""
n=int(9)
for row in range(1, n + 1):
    print(*(f"{row*col:3}" for col in range(1, n + 1)))