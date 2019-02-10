# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:35:24 2019

@author: heict
"""

import random

#Picks a random "k" quantity of itens contained in a choosen range
itens = list(range(1, 53))
k_itens = random.sample(itens, k=5)
print(k_itens)