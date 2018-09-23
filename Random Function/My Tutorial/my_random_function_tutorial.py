# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:48:51 2018

@author: Heictor Costa
"""

import random
division = "---------------------------------------"

#Prints a random value between 0(inclusive) and 1(not-inclusive)
value = random.random()
print(value,"\n")
print(division)


#Prints a random integer value between x(inclusive) and y(also inclusive)
value_xy = random.randint(1,10)
print(value_xy,"\n")
print(division)


#Prints a random float value between x(inclusive) and y(also inclusive)
value_xy = random.uniform(1,10)
print(value_xy,"\n")
print(division)

#Picks a random value from a list of values
animes = ['Yu-Gi-Oh', 'DragonBall', 'Naruto'] #list of values
answear = random.choice(animes) #random function
print('o melhor anime de todos é o ' + answear)
print(division)

#Picks a random value "k" times from a list of values
chromosomes = ['X', 'Y']
pair = random.choices(chromosomes, k=10) #"k" is the quantity of results
print(pair + pair)
print(division)

#Picks a random value from a list of values with weights
colors = ['Black', 'Red', 'Green']
roulette_wheel = random.choices(colors,weights=[10, 10, 2], k=10)
print(roulette_wheel)
print(division)

#Picks a random value from a list of values with weights
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)
print(division)

#The difference between the choices method and the shuffle method is
#that the first one can pick up the same value mutiple times

#Picks a random sample of unique "k" itens from a list of values
deck = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)
print(division)