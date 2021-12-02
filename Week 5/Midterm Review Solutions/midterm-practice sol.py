# Problem 8.21
import math
class Polygon(object):
    'regular polygon class'

    def __init__(self, n, s):
        'constructs an n-sided polygon with side length s'
        self.n = n
        self.s = s

    def perimeter(self):
        'returns polygon perimeter'
        return self.n*self.s

    def area(self):
        'returns polygon area'
        return (self.n*self.s**2)/(4*math.tan(math.pi/self.n))


# Problem 8.22
class Worker(object):
    'worker class'
    def __init__(self, name, rate):
        'constructs worker object with associated name and pay rate'
        self.name = name
        self.rate = rate

    def changeRate(self, newRate):
        'changes worker rate'
        self.rate = newRate

    def pay(self,hours):
        'returns worker pay'
        print('Not implemented')
        

class HourlyWorker(Worker):
    'hourly worker class'

    def pay(self, hours):
        'returns hourly worker pay'
        if hours > 40:
            return 40*self.rate + (hours-40)*2*self.rate
        else:
            return hours*self.rate

class SalariedWorker(Worker):
    'salaried work class'

    def pay(self, hours=None):
        'returns salaried worker pay'
        return 40*self.rate

# Problem 8.35
class Stack(object):
    'classic stack class'

    def __init__(self):
        'constructor initializes empty stack'
        self.s = []

    def pop(self):
        'removes and returns top item in stack'
        return self.s.pop()

    def push (self, item):
        'pushes item into stack'
        return self.s.append(item)

    def isEmpty(self):
        'checks whether stack is empty'
        return (len(self) == 0)

    def __len__(self):
        'returns length of stack'
        return len(self.s)

    def __repr__(self):
        'returns a string representation of stack object'
        return repr(self.s)

# Problem 8.37
class Square(Polygon):
    'square class'

    def __init__(self, s):
        'constructor that initializes the side length of a square'
        Polygon.__init__(self, 4, s)

    def area(self):
        'returns square area'
        return self.s**2

from math import sqrt
class Triangle(Polygon):
    def __init__(self, s):
        'constructor that initializes the side length of an equilateral triangle'
        Polygon.__init__(self, 3, s)

    def area(self):
        'returns triangle area'
        return sqrt(3)*self.s**2/4

# Problem 8.40
class BankAccount2(object):
    'a second bank account class'

    def __init__(self, initial=0):
        'constructor; raises ValueError exception if initial balance is negative'
        if initial < 0:
            raise ValueError('Negative balance')
        self.b = initial

    def withdraw(self, amount):
        'withdraws amount; raises ValueError exception if resulting balance is negative'
        if self.b - amount<0:
            raise ValueError('Overdraft')
        self.b -= amount

    def deposit(self, amount):
        'deposits amount; raises ValueError exception if amount is negative'
        if amount < 0:
            raise ValueError('Negative deposit')
        self.b += amount

    def balance(self):
        'returns balance'
        return self.b

# Problem 9.16
from tkinter import Label, Frame, Entry, Button, END
from tkinter.messagebox import showinfo
class BMI(Frame):
    'Body Mass Index app'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.pack()
        BMI.make_widgets(self)

    def make_widgets(self):
        'defines BMI widgets'
        Label(self, text="Enter your height:").grid(row=0,column=0)
        Label(self, text="Enter your weight:").grid(row=1,column=0)
        self.height = Entry(self)
        self.height.grid(row=0,column=1)
        self.weight = Entry(self)
        self.weight.grid(row=1,column=1)
        Button(self, text="Compute BMI", command=self.compute).grid(row=2, column=0, columnspan=2)

    def compute(self):
        'handler for button "Compute BMI"'
        h = eval(self.height.get())
        w = eval(self.weight.get())
        bmi = w*703/h**2
        showinfo(message='Your bmi is {}'.format(bmi))
        self.height.delete(0,END)
        self.weight.delete(0,END)

#Problem 9.19

from tkinter import Tk, Button,Entry,Frame,END

class Phone(Tk):
    def  __init__(self, parent = None):
        Tk.__init__(self, parent)
        self.make_widgets()
        
    def click(self, key):
        if len(self.entry.get())==3 or len(self.entry.get())==7 :
            self.entry.insert(END, '-')
        if len(self.entry.get())<12:
            self.entry.insert(END, key)

    def make_widgets(self):
        labels = [['1', '2', '3'],     # phone dial label texts
          ['4', '5', '6'],     # organized in a grid
          ['7', '8', '9'],
          ['*', '0', '#']]

        f = Frame(self)
        f.pack()

        for r in range(4):      # for every row r = 0, 1, 2, 3
            for c in range(3):      # for every row c = 0, 1, 2
                # create label for row r and column c
                cmd= lambda x=labels[r][c]: self.click(x)
                btn = Button(f,
                               padx=10,
                              text=labels[r][c], command=cmd)  # label text
                # place label in row r and column c
                
                btn.grid(row=r, column=c)  
        self.entry=Entry(self)
        self.entry.pack()

# Problem 9.25, 9.26
from tkinter import Label, Frame, Entry, Button, LEFT, RIGHT, END
from random import randrange
class Ed(Frame):
    'Simple arithmetic education app'
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)
        self.pack()
        Ed.make_widgets(self)
        Ed.new_problem(self)

    def make_widgets(self):
        'defines Ed widgets'
        self.ent1 = Entry(self)
        self.ent1.pack(side=LEFT)
        self.ent2 = Entry(self)
        self.ent2.pack(side=LEFT)
        Button(self, text="Enter", command=self.evaluate).pack(side=RIGHT)

    def new_problem(self):
        'creates new arithmetic problem'
        self.ent1.delete(0,END)
        numA = randrange(0,10)
        numB = randrange(0,10)
        oper = randrange(0,2)
        if oper == 0:                    # addition problem
            self.res = numA + numB
            self.ent1.insert(END, numA)
            self.ent1.insert(END, '+')
            self.ent1.insert(END, numB)
        else:                            # subtraction problem               
            if numA < numB:
                numA, numB = numB, numA  # insure result is not negative
            self.res = numA - numB
            self.ent1.insert(END, numA)
            self.ent1.insert(END, '-')
            self.ent1.insert(END, numB)
