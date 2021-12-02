# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:15:37 2020

@author: Matt
"""

import math

class Polygon(object):
    
    def __init__(self,n,l):
        self.n = n
        self.l = l
    
    def perimeter(self):
        p = self.l * self.n
        return p
    
    def area(self):
        a = ((self.l ** 2)*self.n) / (4*math.tan(math.pi/self.n))
        return a
    
    
    
    