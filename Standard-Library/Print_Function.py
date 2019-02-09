# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 10:16:30 2018

@author: Heictor Costa
"""
#On this class you will learn some things about Print Function and Strings

#Important: The sharp symbol is used on lines that are just comments, so they're not executed
#Outputs to console whatever you put in there
print()

#print function is mostly used with a string, "mostly" i said
print('Example of printing a string')

#Using single quotes ('') X Using double quotes ("")
#print('I'm feeling nice')
#The string above won't work out - sorry for the spoiler -, but it's not your fault...not yet

#So, instead of using single quotes, you can use double quotes arround the sentence
print("I'm feeling nice")
#Yes, i know what's in yout mind, and the answear is "YES, CHANGING THE ORDER WILL DO WELL"
print('I"m feeling nice')
#The last example is quite useful to direct speech examples
print('Jane says, "I am done with Sergio."')
#By the way, this is a song from a band called "Jane's Addiction", you should hear it. Link Below
#https://www.youtube.com/watch?v=Z0hFQdEUQKM

#But now, if you want to use the last example using "I'm" instead of "I am" here's how you gonna do it
print('I\'m done with Sergio.')
#Noticed the difference? You just have to use backslash before the single quote

#CONCATENATION
#Well, let's try printing two different sentences and make them get together
print('What\'s up '+'people') #But you have to enter space after "up" so it doesn't get straight before the next sentence
#or you can use comma (",")
print('What\'s up','people') #See what i did there? And this will print out the same result

#You don't always have to use strings on print function
print('MP',3)
#In this example, you won't be able to use "+" instead of ",". That's beacause strings and int numbers are two differente types of variables

#You really wanna use the plus symbol, don't you? Okay Okay, i feel the same. So let's try this
print('MP '+str(5)) #OMG, HEICTOR. WWHAT JUST HAPPENED?
#Easy, my lil Padawan.
#What i did here? I just converted the number five into a string, so now "MP" and "5" can stay together, it's basically a love story.

#Now it's the time you ask yourself: "Can i do the opposite action?"
#And just like Obama said, "YES, YOU CAN"
print(int('34')+12)
#Yeah, it worked

#Try running this out
#print(int('34.7')+12)
#I know, it didn't worked, that's because 34.7 is a float number, not a int (integer one. So now you know what you have to do
print(float('34.7')+12)

#Okay, all of this was BORING, i know, i slept twice while making all of this.
#But it'll be useful - i think so, but maybe not -, so try to make this rules run in your mind quite naturally.

#Shihemi se shpejti, mirupafshim