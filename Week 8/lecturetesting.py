# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:27:45 2020

@author: Matt
"""

#1234
#1
#2   print
#3
#4


#return [1,2,3,4]


def printLineWithList(num):
    
    lst=[]
    if num < 10:
        print(num)
        lst.append(num)
        return lst
    
    else:
        retVal = printLineWithList(num//10)
        localVal = num%10
        print(localVal)
        lst.append(localVal)
        return retVal + lst 
    
    
    
lst = printLineWithList(1234)
        
print(lst)       
#num = 12

#print(num%10)