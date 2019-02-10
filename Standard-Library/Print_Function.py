# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:16:30 2018

@author: Heictor Costa
"""
#On this class you will learn some things about Print Function and Strings

#Important: The sharp symbol is used on lines that are just comments, so they're not executed
#Outputs to console whatever you put in there
print()

#print function can be used to display a string
print('Example of printing a string')

"""
Using single quotes ('') X Using double quotes ("")
Have the following line as example
print('I'm feeling nice')
The string above won't work, so instead of using single quotes you can use double quotes arround the sentence
"""
print("I'm feeling nice")

#You can also change de single by the double and get like this:
print('I"m feeling nice')
#And will work just fine

#The last example is quite useful to direct speech examples
print('Jane says, "I am done with Sergio."')
#If you want to use the last example using "I'm" instead of "I am" here's how you gonna do it
print('I\'m done with Sergio.')
#You just have to use backslash before the single quote

#CONCATENATION
#Well, let's try printing two different sentences and make them get together
print('What\'s up '+'people') #But you have to press space button after "up" so it doesn't get straight before the next sentence
#instead of "+" you can use comma (",")
print('What\'s up','people') #And this will print out the same result

#You don't always have to use strings on print function
print('MP',3)
#In this example, you won't be able to use "+" instead of ",". That's beacause strings and int numbers are two differente types of data

#To use the plus symbol with a string and a number, you have to convert the number into a string
print('MP '+str(5))
#And the opposite operation is also possible
print(int('34')+12)#I first declared 34 as a string using single quotes, and after that it turns into a int

#You can't convert a float number into a int number
#print(int('34.7')+12) <== This won't work
#That's because 34.7 is a float number, not a int
print(float('34.7')+12)#This one will work just fine
