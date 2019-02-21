# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:09:49 2018

@author: heict
"""

x = 6 #Not a global variable

#Defining example function
def example():
    z = 5
    print(z)
    print(x)
    x += 5
    print(x)

#The previsou commands will cause the following message, that's why we're not running it
#UnboundLocalError: local variable 'x' referenced before assignment

#If you try to print z's value outside the "def" block you will receive the message saying "z" was no defined

#To make a variable become global variable:
def example2():
    global y #Define as global
    y = 7 #Atributing a value
    print(y) #Printing the variable
    y += 3 #Executing a operantion with the variable
    print(y) #Printing its new value
example2() #Calling the function

print(y) #Printing "y" again, but this time outside the "def" block

V = 5
def example3():
    anotherV = V #We can acess the local variable, but not modify it
    print(anotherV) #Print the "new variable"
    anotherV += 4 #Execute a operation with it
    #print(anotherV) #Print its new value
    #anotherV it's also a local variable
    return anotherV

example3()
print(V)
