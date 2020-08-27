# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:38:40 2020

@author: sofia.russmann
"""

mas100 = [ s for s in camion if s['cajones'] > 100 ]

myn = [ s for s in camion if s['nombre'] in {'Mandarina','Naranja'} ]

costo10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]



#corchetes ([,]) por llaves ({, }),
#comprensión de conjuntos. Vas a obtener valores únicos.
#listado de las frutas en el camión pordías usar:
nombres = { s['nombre'] for s in camion }
#nombres
#{'Caqui', 'Durazno', 'Lima', 'Mandarina', 'Naranja'}



camion_precios = { nombre: precios[nombre] for nombre in nombres }