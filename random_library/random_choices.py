# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 03:49:03 2019

@author: heict
"""

import random

chromosomes = ['X', 'Y']#list
#Picks a random value "k" times from a list
allele = random.choices(chromosomes, k=10) #"k" is the quantity of results
print(allele + allele)
