# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:47:30 2020

@author: sofia.russmann
"""

nums = [1,2,3,4]
cuadrados = [ x * x for x in nums ]
print(cuadrados)
[1, 4, 9, 16]
dobles = [ 2 * x for x in nums if x > 2 ]
print(dobles)
