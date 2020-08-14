# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:41:10 2020

@author: sofia.russmann
"""


import matplotlib.pyplot as plt

Phase = [1,2,3,4]   
Month = [1,2,3,4,5,6,7,8,9,10,11,12,
         13,14,15,16,17,18,19,20,21,22,23,24,
         26,27,28,29,30,31,32,33,34,35,36,37]

Regular_vaccine = [1,1,1,1,1,1,1,1,1]
Oxford_vaccine =[]
  
plt.plot(Month, Phase, color='g')
plt.plot(Month, Oxford_vaccine, color="#6c3376", linewidth=3)
plt.plot(Month, Regular_vaccine, color="#f3e151", linewidth=3)

plt.title('Vaccine phase vs Time')
plt.xlabel('Time')
plt.ylabel('Vaccine phase')
plt.show() 