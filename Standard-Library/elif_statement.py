# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:38:13 2019

@author: heict
"""

x = (float(input('Insira o valor de x: \n')))
y = (float(input('Insira o valor de y: \n')))

if x>y:
    print('x é maior que y')
elif x<y:
    print('x é menor que y')
elif x>=y:
    print('x é maior ou igual que y')
elif x<=y:
    print('x é menor ou igual que y')
elif x!=y:
    print('x é diferente de y')
elif x==y:
    print('x é igual a y')
else:
    print('nenhuma condição foi satisfeita')
