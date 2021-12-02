# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:27:24 2020

@author: Matt Wilson

CSC 242
Midterm Class Problem
"""

class GroceryListManager(object):
    
    def __init__(self,filename='groceries.txt'):
        'constructor'
        self.filename = filename
        self.gl = []
        
        
    def getCount(self):
        'sets a count of items from the grocery list'
        return len(self.gl)
    
    
    def addItem(self,text):
        'adds an item to the grocery list'
        self.gl.append(text)
        return True
    
    def getItem(self,index):
        'gets a specific item from the grocery list'
        return self.gl[index]
    
    def removeItem(self,number):
        'removes an item from the grocery list'
        del self.gl[number]
    
    def __iter__(self):
        'iterates through items in the grocery list.'
        return iter(self.gl)
    
    def saveToFile(self):
        'saves the items to a file.  The file is completely over written'
        try:
            outfile = open(self.filename,'w')
            for item in self.gl:
                print(item,file=outfile)
            outfile.close()
            return True
        except:
            return False
    
    def loadFile(self):
        'loads Grocery list items from a file.  Existing items in the list are removed'
        try:
            infile = open(self.filename,'r')
            self.gl.clear()
            for line in infile:
                item = line.strip()
                self.gl.append(item)
                
            infile.close()
            return True
        except:
            return False

    def __str__(self):
        return 'The Grocery List has {} items'.format(self.getCount())
    
    
    

