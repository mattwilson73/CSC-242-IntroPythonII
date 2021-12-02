# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:03:39 2020

@author: Matt
"""

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END,filedialog,Scale, HORIZONTAL
from tkinter.messagebox import showinfo


class BrokenBoneWard(Tk):
    'Hospital Patient Intake Class'
    
    def __init__(self,parent=None):
        '''
        Constructor
        '''
        Tk.__init__(self,parent)
        self.title('Broken Bone Ward Intake')
        self.make_widgets()
        
    def saveinfo(self):
        '''
        Saves patient info in a "Name,Age,Time Waited,Pain,Severity" format to
        "PatientLogs.txt"
        '''
        
        try:
            outfile = open('PatientLogs.txt','a+')
            print('{},{},{},{},{}'.format(self.nameentry.get(),self.ageentry.get()
            ,self.timeentry.get(),self.pain.get(),self.sev),file=outfile)
    
            outfile.close()
            
            
        except:
            showinfo(title='File Save Error',message='Error saving information to file')
        
        
        
    def runinfo(self):
        '''
        Checks for entry errors and then determines the severity of the patient.
        Severity is based off of age and pain of patient.
        Calls saveinfo to log information to file.
        '''
        
        if self.nameentry.get() == '':
            showinfo(title='Entry Error',message='Missing Name')
            return
        
        if self.ageentry.get() == '':
            showinfo(title='Entry Error',message='Missing Age')
            return
        
        
        if self.timeentry.get() == '':
            showinfo(title='Entry Error',message='Missing Time Waited')
            return        
    
        try:
            name = self.nameentry.get()
            age = int(self.ageentry.get())
            time = int(self.timeentry.get())
            pain = int(self.pain.get())
                
        except ValueError:
            showinfo(title='Entry Error', message='Invalid Age or Time Entry')
            return
        
        else:    
            self.sev = 'Low'
            
        if pain >= 5 and pain < 8:
            self.sev = 'Medium'
            
        if (age <= 10 or age >= 70) or pain >= 8:
            self.sev = 'High'
            
            
        showinfo(title='Severity',message='Patient Determined to be {} Severity'.format(self.sev))
        
        self.saveinfo()

        self.nameentry.delete(0,END)
        self.ageentry.delete(0,END)
        self.timeentry.delete(0,END)
        
        
        
        
    def make_widgets(self):
        '''
        Creates widgets for the GUI
        '''
        
        Label(self,text='Name:').grid(row=0,column=1)
        self.nameentry = Entry(self)
        self.nameentry.grid(row=0,column=2)
        
        Label(self,text='Age:').grid(row=1,column=1)
        self.ageentry = Entry(self)
        self.ageentry.grid(row=1,column=2)
        
        Label(self,text='Time Waited:').grid(row=2,column=1)
        self.timeentry = Entry(self)
        self.timeentry.grid(row=2,column=2)
        
        Label(self,text='Level of Pain:').grid(row=3,column=1)
        self.pain = Scale(self,from_=0,to=10, orient=HORIZONTAL)
        self.pain.grid(row=3,column=2)
        
        Button(self,text='Intake Patient',command=lambda:self.runinfo()).grid(row=4,column=1,columnspan=2)
        
        
        
        
        
BrokenBoneWard().mainloop()