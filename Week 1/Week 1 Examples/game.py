# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:30:57 2020

@author: Matt
"""




import random




def game(n):
    
    correct_total = 0
    for l in range(n):
        
    
        int1 = random.randrange(0,9)
        int2 = random.randrange(0,9)
        correctans = int1+int2
    
        print("what is {} + {}".format(int1,int2))
        
        
        

        while True:
    
            try:
                
                userans = int(input("inputhere"))
                break
            except ValueError:
                
                print("You didnt enter a int, try again")
    
    
        if correctans == userans:
            print("Correct")
            correct_total += 1
            
        else:
            print("incorrect")
            
            
    
    print("you got {} questions correct!".format(correct_total))

    





game(5)