# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:27:28 2020

@author: Matt Wilson

CSC 242
Midterm GUI Problem
"""

from tkinter import Tk, Label, Button, Entry, END, Scale, HORIZONTAL
from tkinter.messagebox import showinfo


class FeedbackGUI(Tk):
    'Feedback GUI Class'
    def __init__(self,parent=None):
        'constructor'
        Tk.__init__(self,parent)
        self.title('Feedback GUI')
        self.make_widgets()
        
    def saveFeedback(self):
        'Writes to feeback file after Save Feedback button is pressed'
        try:
            
        
            if self.nameentry.get() == '':
                showinfo(title='Feedback Error',message='You must specify a name.')
                return
            
            if self.dateentry.get() == '':
                showinfo(title='Feedback Error',message='You must specify a date.')
                return
            
            name = self.nameentry.get()
            date = self.dateentry.get()
            rate = self.slider.get()
            
            
            
            outfile = open('feedback.txt','a+')
            print('{},{},{}'.format(name,date,rate),file=outfile)
            outfile.close()
            showinfo(title='Feedback',message='Feedback Saved.')
            
            self.nameentry.delete(0,END)
            self.dateentry.delete(0,END)
            
        except:
            showinfo(title='Feedback Error',message='Error saving feedback to file')
            
        
        
    def make_widgets(self):
        
        Label(self,text='Customer Service Survey').grid(row=0,column=0,columnspan=2)
        
        Label(self,text='Your Name:').grid(row=1,column=0)
        self.nameentry = Entry(self)
        self.nameentry.grid(row=1,column=1)
        
        Label(self,text='Date of Visit').grid(row=2,column=0)
        self.dateentry = Entry(self)
        self.dateentry.grid(row=2,column=1)
        
        Label(self,text='Would you come back again?').grid(row=3,column=0)
        self.slider = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider.grid(row=3,column=1)
        
        Button(self,text='Save Feedback',command=lambda:self.saveFeedback()).grid(row=4,column=0)
        

        
FeedbackGUI().mainloop()