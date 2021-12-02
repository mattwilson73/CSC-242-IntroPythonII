# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:58:02 2020

@author: Matt
"""

import random #Imports the random library 

def getValue(maxVal): 
    a = maxVal *2 #variable a is defined with the n
    return random.randrange(0,a)


def func(val):
    output = set()
    for i in val:
        print(i)
        num = int(i)
        if num > 0:
            rndnum = getValue(num)
            output.add(rndnum)
        return output
    

val = input('Pleasee enter you 7 digit student id:')
print(func(val))
