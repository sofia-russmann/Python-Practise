# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:58:31 2020

@author: sofia.russmann
"""

import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
