"""Was completed during the lab session by myself"""

import random
class Die(object):
    'a class representing a Die'
    def __init__(self, sides=6):
        'initialize a die, default 6 sides'
        
        self.sides = sides

    def roll(self):
        'roll the dice'
        self.value = random.randint(0,self.sides)
 

    def get(self):
        'get the current value of the die'
        return self.value


    def numSides(self):
        'get the number of sides of the die'
        return self.sides


    def __str__(self):
        'get the string representation of the die'
        return "{}".format(self.sides)

    def __repr__(self):
        'get the python representation of the die'
        return "Die({})".format(self.sides)
    


def rollDice(rolls, sides):
    ''' rolls 2 dice of a given size and amount and prints the results'''
    d1 = Die(sides)
    d2 = Die(sides)
    
    for i in range(rolls):
        d1.roll()
        d2.roll()
        print("Roll {} : {} - {}".format(i,d1.get(),d2.get()))
    
    
    

        
   
        
