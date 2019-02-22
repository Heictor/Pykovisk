# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:50:20 2019

@author: heict
"""

import random

#Shuffles values inside a choosen range
deck = list(range(1, 53))
print(deck)
print("------")



for x in deck:
    print(random.choice(deck))
