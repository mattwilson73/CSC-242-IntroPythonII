# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:29:45 2020

@author: Matt
"""


class Animal(object):
    
    def __init__(self,s='default',l='default'):
        self.species=s
        self.lang=l
        
    def setSpecies(self,name):
        self.species = name
        
    def getSpecies(self):
        return self.species
    
    def setLanguage(self,lang):
        self.lang = lang
        
    def speak(self):
        return 'I am a {} and I {}'.format(self.species,self.lang)
    
    def __repr__(self):
        return "Animal('{}','{}')".format(self.species,self.lang)
    
    
    
    
    