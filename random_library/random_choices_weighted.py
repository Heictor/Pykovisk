# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 03:50:00 2019

@author: heict
"""


import random

#Picks a random item from a list with weighted intems
colors = ['Black', 'Red', 'Green']
roulette_wheel = random.choices(colors,weights=[10, 10, 2], k=10)
print(roulette_wheel)


'''
Run the code mutiple times to notice the "green" item is the one less picked 
'''