
import random

chromosomes = ['X', 'Y']#list
#Picks a random value "k" times from a list
allele = random.choices(chromosomes, k=10) #"k" is the quantity of results
print(allele + allele)
