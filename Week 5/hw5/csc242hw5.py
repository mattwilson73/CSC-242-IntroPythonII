#Worked on this homework assignment by myself.

class Animal(object):
    'a class that abstracts an animal'
    def __init__(self, s = 'default', l = 'default'):
        self.species = s
        self.language = l
        
    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        return 'I am a {} and I {}'.format(self.species, self.language)
    
    def __repr__(self):
        return "Animal('{}', '{}')".format(self.species, self.language)

    def __str__(self):
        return self.speak()

#implement Upsidedown animal here

class UpsidedownAnimal(Animal):
    
    def __init__(self,s = 'default',l = 'default',animal = Animal()):
        animal = Animal(s,l)
        self.animal = animal
    
    def speak(self):
        
        return 'I am a {} and I {}'.format(self.animal.species[::-1], self.animal.language[::-1])
    
    
    def __repr__(self):
        return "UpsidedownAnimal('{}','{}')".format(self.animal.species,self.animal.language)
    
    
    
    
    
    
    
    
    
from tkinter import Button, Entry, Label,Tk, HORIZONTAL, END
from tkinter.messagebox import showinfo

class RoadTripCalculator(Tk):
    'Trip Calculator Class'
    
    def __init__(self,parent=None):
        'the constructor'
        Tk.__init__(self,parent)
        self.title('Road Trip Cost Calculator')
        self.tripcount = 0
        self.costsum = 0
        self.make_widgets()


    def clear(self):
        'clear all the labels and entry boxes'
        
        self.tripcount = 0
        self.costsum = 0
        currentcost = 0
        
        self.currentcost.config(text = '${:.2f}'.format(currentcost))
        self.totalcost.config(text = '${:.2f}'.format(self.costsum))
        self.totaltrips.config(text = self.tripcount)
        
        
        
    def calculate(self):
        'Calculate (distance/mpg)*cost per gallon and update the total trips and total cost. Check if input is valid.'
        try:
            distance = float(self.mileentry.get())
        except ValueError:
            showinfo(title = 'Calculation',message = 'Error. Distance cant convert to float.')
            return
            
        try:
            mpg = float(self.mpgentry.get())
        except ValueError:
            showinfo(title = 'Calculation',message = 'Error. MPG cant convert to float.')
            return
            
        try:
            cost = float(self.costentry.get())
        except ValueError:
            showinfo(title = 'Calculation',message = 'Error. Cost per gallon cant convert to float.')
            return
        
        self.tripcount += 1
        currentcost = (distance / mpg) * cost
        self.costsum += currentcost
        
        
        self.currentcost.config(text = '${:.2f}'.format(currentcost))
        self.totalcost.config(text = '${:.2f}'.format(self.costsum))
        self.totaltrips.config(text = self.tripcount)
        
        
        
            

    def make_widgets(self):
        'add widgets to UI'
        
        Label(self,text='Total Trips:').grid(row=0,column=0)
        Label(self,text='Mile Traveled').grid(row=1,column=0)
        Label(self,text='MPG').grid(row=1,column=1)
        Label(self,text='Total Cost').grid(row=0,column=2)
        Label(self,text='Cost Per Gallon').grid(row=1,column=2)
        Label(self,text='=').grid(row=2,column=3)
        
        
        self.mileentry = Entry(self)
        self.mileentry.grid(row=2,column=0)
        self.mpgentry = Entry(self)
        self.mpgentry.grid(row=2,column=1)
        self.costentry = Entry(self)
        self.costentry.grid(row=2,column=2)
        
        Button(self, text='Add Trip',command=lambda:self.calculate()).grid(row=3,column=0)
        Button(self, text='Clear Trips',command=lambda:self.clear()).grid(row=3,column=1)
        
        
        self.totaltrips = Label(self,text=self.tripcount)
        self.totaltrips.grid(row=0,column=1)
        
        self.totalcost = Label(self,text='${:.2f}'.format(0))
        self.totalcost.grid(row=0,column=3)
        
        self.currentcost = Label(self)
        self.currentcost.grid(row=2,column=4)
        
        
        

RoadTripCalculator().mainloop()

class WierdStringIter(object):
    
    def __init__(self,st):
        self.s = st
        self.index = 0
    
    def __next__(self):
        v = 'aeiouAEIOU'
        if self.index >= len(self.s):
            raise StopIteration()
        if self.s[self.index] in v:
            self.s = self.s.replace(self.s[self.index],'')

        try:
            
            char = self.s[self.index]
            self.index += 1
            return char
        except IndexError:
            pass
        
    
class WierdString(str):
    
    
    def __iter__(self):
        return WierdStringIter(self)
    
 

        
    
    
