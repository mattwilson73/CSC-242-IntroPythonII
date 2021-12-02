# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:48:13 2020

@author: Matt
"""

from tkinter import Label, Tk, Entry, Button
from tkinter.messagebox import showinfo

class Adder(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.title('Simple Adder!')
        self.make_widgets()
        
        
    def add(self):
        top = int(self.top.get())
        bottom = int(self.bottom.get())
        self.answer.configure(text=str(top+bottom))
        
    def make_widgets(self):
        self.top = Entry(self)
        self.top.grid(row=0,column=1)
        
        self.bottom = Entry(self)
        self.bottom.grid(row=1,column=1)
        
        Label(text='+').grid(row=1,column=0)
        self.answer=Label(self)
        self.answer.grid(row=2,column=1)
        
        
        Button(self,text='Add',command=lambda:self.add()).grid(row=3,column=1)
        
    
Adder().mainloop()