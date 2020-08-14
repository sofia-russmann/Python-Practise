# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:38:36 2020

@author: sofia.russmann
"""

import gzip
with gzip.open('Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')