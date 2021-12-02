# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:20:29 2020

@author: Matt
"""


#class MyClass(object):
#    
#    def __init__(self):
#        pass
#    
#    def setTo(self,value):
#        self.data = value
#    
#    def get(self):
#        return self.data
#    
#    def double(self):
#        self.data *=2
#    
#    def ntimes(self,n):
#        self.data = self.data * n
#        
#
#
#def sums(l):
#    
#    count = 0
#    for x in l:
#        count += x
#    print(count)
#        
#        
#
#sums([1,'f',3])
#        
#        
#        
#
#class Person:
#	def __init__(self, name, age):
#		self.name = name
#		self.age = age
#
#	def compare_age(self, other):
#		if self.age() < other.age():
#            return "{} is older than me".format(other.name())
#        
#       if self.age() 
#		
#        
        
#
#from tkinter import Label, Tk
#
#class HelloWorld(Tk):
#    def __init__(self,somedata='default value',parent=None):
#        Tk.__init__(self,parent)
#        self.title('Hello World!')
#        self.make_widgets()
#        
#        
#        
#    def make_widgets(self):        
#        Label(self,text='Hello World watching from home').pack()
#        Label(self,text='Another line of text').pack()
##        Label(self,text=somedata).pack()
#        
#
#HelloWorld().mainloop()
#
#
#
#
#
#
#cookiejar = ['chocolate chip','peanut butter','oatmeal','mint chocolate','raisin','vegan','oatmeal']
#
#
#
#
#def loadCookies():
#    'loads the cookies from a file as Cookie objects.  Clears exisiting cookies in memory before it loads. returns True if successful and False if not.'
#    jar = []
#    try:
#        infile = open('cookies.txt','r')
#        content = infile.readlines()
#        infile.close
#        for c in content:
#            newcookies = c.strip()
#            jar.append(newcookies)
#    except:
#        pass
#    print(jar)
#
#
#loadCookies()

#
#def extractStr2(lst):
#    'takes an arbitrarily nested list as a parameter and returns a string that consists of the concatenation of all strings found in the list'
#    ##base case
#    if lst==[]:
#        return ''
#    if type(lst[0])==str:
#        firstItem=str(lst[0])
#        restOfLst=str(extractStr2(lst[1::]))
#        return firstItem + restOfLst
#    else:
#        return extractStr2(lst[1::])
#
#
#
#lll = [['a'],'b','c',['d'],'e','f']
#print(extractStr([['a'],'b','c',['d'],'e','f']))
#
#
#import os
#
#def Indexer(root):
#    ss = ''
#    
#    for item in os.listdir(root):
#        n = os.path.join(root,item)
#        if os.path.isdir(n):
#            ss += Indexer(n)
#            
#            
#        else:
#            f=open(n,'r')
#            s=f.read()
#            f.close()
#            
#            newtxt = 'Path : '+n+'\n'+s+'\n'
#            ss += newtxt
#            
#    return ss
#            
#print(Indexer('Test9hw'))






x=0

for i in range(1,10):
    for j in range(1,i+1):
       x += 1
       
       
       
print(x)
































