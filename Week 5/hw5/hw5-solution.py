
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

class UpsidedownAnimal(Animal):
    def speak(self):
        return 'I am a {} and I {}'.format(self.species[::-1], self.language[::-1])

    def __repr__(self):
        return "UpsidedownAnimal('{}', '{}')".format(self.species, self.language)
    
from tkinter import Button, Entry, Label,Tk, HORIZONTAL, END
from tkinter.messagebox import showinfo

class RoadTripCalculator(Tk):
    'Trip Calculator Class'
    
    def __init__(self,parent=None):
        'the constructor'
        Tk.__init__(self, parent)
        self.title('Road Trip Cost Calculator')
        self.minsize(width=200,height=100)
        self.make_widgets()
        self.cost=0
        self.trips=0

    def clear(self):
        'clear all the labels and entry boxes'
        self.cost=0
        self.trips=0
        self.costLabel.config(text='${:.2f}'.format(self.cost))
        self.totalTripsLabel.config(text='{}'.format(self.trips))
        self.answerLabel.config(text='')
        self.mEntry.delete(0,END)
        self.mpgEntry.delete(0,END)
        self.cpgEntry.delete(0,END)
        
    def calculate(self):
        'Calculate (distance/mpg)*cost per gallon and update the total trips and total cost. Check if input is valid.'
        distance=self.mEntry.get()
        mpg=self.mpgEntry.get()
        cpg=self.cpgEntry.get()

        try:
            d = float(distance)
        except ValueError:
            showinfo(title='Calculation', message="Error. Distance cant convert to float.")
            return
        try:
            m = float(mpg)
        except ValueError:
            showinfo(title='Calculation', message="Error. MPG cant convert to float.")
            return

        try:
            c = float(cpg)
        except ValueError:
            showinfo(title='Calculation', message="Error. Cost per gallon cant convert to float.")
            return

        try:
            total=(d/m)*c
            self.answerLabel.config(text='${:.2f}'.format(total))
            self.cost=self.cost + total
            self.costLabel.config(text='${:.2f}'.format(self.cost))
            self.trips+=1
            self.totalTripsLabel.config(text='{}'.format(self.trips))
            
        except:
            self.answerLabel.config(text='Unable to calculate value.')
            

    def make_widgets(self):
        'add widgets to UI'

        Label(self,text='Total Trips:').grid(row=0,column=1)
        self.totalTripsLabel = Label(self,text='0')
        self.totalTripsLabel.grid(row=0,column=2)
        
        Label(self,text='Total Cost').grid(row=0,column=3)
        self.costLabel = Label(self,text='$0.00')
        self.costLabel.grid(row=0,column=4)
        
        Label(self,text='Mile Traveled').grid(row=1,column=1)
        self.mEntry = Entry(self)
        self.mEntry.grid(row=2,column=1)

        Label(self,text='MPG').grid(row=1,column=2)
        self.mpgEntry = Entry(self)
        self.mpgEntry.grid(row=2,column=2)

        Label(self,text='Cost Per Gallon').grid(row=1,column=3)
        self.cpgEntry = Entry(self)
        self.cpgEntry.grid(row=2,column=3)
        
        Label(self,text='=').grid(row=2,column=4)
        self.answerLabel = Label(self,text='  ')
        self.answerLabel.grid(row=2,column=5)
        Button(self,text="Add Trip", command=lambda:self.calculate()).grid(row=3,column=1)
        Button(self,text="Clear Trips", command=lambda:self.clear()).grid(row=3,column=2)

RoadTripCalculator().mainloop()

class WierdStringIter(object):
    def __init__(self,string):
        self.string=string
        self.index=0
        self.vowels=('a','e','i','o','u','A','E','I','O','U')

    def __next__(self):
        while(True):
            if self.index >= len(self.string):
                raise StopIteration()
            else:
                if self.string[self.index] in self.vowels:
                    self.index+=1
                    continue
                else:
                    val = self.string[self.index]
                    self.index+=1
                    return val
                
    
class WierdString(str):
    def __iter__(self):
        return WierdStringIter(self)
        
