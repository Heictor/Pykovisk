# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 19:40:51 2018

@author: heict
"""
d=float(input('insira distância: '))
t=float(input('insira tempo: '))

def velocidade(distância,tempo):
    v = distância/tempo
    print('velocidade média é',v)

velocidade(d,t)