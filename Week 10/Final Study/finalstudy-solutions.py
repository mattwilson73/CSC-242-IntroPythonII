from tkinter import Button, Entry, Label,Tk
from tkinter.messagebox import showinfo
import random

class Die(object):
    'a class representing a Die'
    def __init__(self, sides=6):
        'initialize a die, default 6 sides'
        self.sides=sides
        self.roll()

    def roll(self):
        'roll the dice'
        self.currentSide = random.randint(1,self.sides)

    def get(self):
        'get the current value of the die'
        return self.currentSide

    def numSides(self):
        'get the number of sides of the die'
        return self.sides

    def __str__(self):
        'get the string representation of the die'
        return str(self.sides)

    def __repr__(self):
        'get the python representation of the die'
        return 'Die({})'.format(self.sides)

class DiceShaker(object):
    'DiceShaker class'
    def __init__(self,dieCount=1, dieSides=6):
        'initialize a dice shaker'
        self.dice = []
        for i in range(dieCount):
            self.dice.append(Die(dieSides))

    def shake(self):
        'shake all the dice in the shaker'
        for die in self.dice:
            die.roll()

    def getTotalRoll(self):
        'get the total face value of all the dice'
        total=0
        for die in self.dice:
            total = total + die.get()
        return total
                
    def getIndividualRolls(self):
        'get a lsit of integers of all the individual die rolls'
        rolls=[]
        for die in self.dice:
            rolls.append(die.get())
        return rolls

    def __str__(self):
        'get a string with all the die rolls seperated by a space'
        s=''
        for die in self.dice:
            s=s+str(die.get())+ ' '
        return s
    
from tkinter import Label, Tk, Entry, Button, END, LEFT
from random import randrange
class Craps(Tk):
    'Craps app'
    def __init__(self,parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title('Craps')
        self.ds=DiceShaker(2,6)
        Craps.make_widgets(self)
        
    def make_widgets(self):
        'defines Craps widgets'
        Label(self, text="Your roll:").pack()
        self.ent = Entry(self,width=26)
        self.ent.pack()
        Button(self, text="New game", command=self.new_game).pack(side=LEFT)
        Button(self, text="Roll for point", command=self.for_point).pack(side=LEFT)

    def new_game(self):
        'handler for "New game" button, starts new game by rolling a pair of dice'
        self.ds.shake()
        self.initial = self.ds.getTotalRoll()
        self.ent.delete(0,END)
        if self.initial in [7,11]:
            self.ent.insert(END, "Thow total: {}... you won!".format(self.initial))
        elif self.initial in [2,3,12]:
            self.ent.insert(END, "Thow total: {}... you lost.".format(self.initial))
        else:
            self.ent.insert(END, "Thow total: {}... Throw for point.".format(self.initial))

    def for_point(self):
        'rolls a pair of dice for point'
        self.ds.shake()
        tmp = self.ds.getTotalRoll()
        self.ent.delete(0, END)
        if tmp == self.initial:
            self.ent.insert(END, "Thow total: {}... you won!".format(tmp))
        elif tmp == 7:
            self.ent.insert(END, "Thow total: {}... you lost.".format(tmp))
        else:
            self.ent.insert(END, "Thow total: {}... Throw for point.".format(tmp))




    


import os


def frequency(folder):
    words=dict()
    for item in os.listdir(folder):
        n = os.path.join(folder, item)
        if os.path.isdir(n):
            subwords = frequency(n)
            for word in subwords:
                if word in words:
                    words[word] = words[word] + subwords[word]
                else:
                    words[word] = subwords[word]
        else: 
            f = open(n, 'r')
            s = f.read()
            items = s.split()
            for item in items:
                if item in words:
                    words[item]=words[item]+1
                else:
                    words[item]=1

            f.close()
    return words


def fileNameCount(folder,name):
    count=0
    for item in os.listdir(folder):
        n = os.path.join(folder, item)
        if os.path.isdir(n):
            count = count + fileNameCount(n,name)
        else: 
            if item == name:
                count=count+1
    return count
    

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import Request, urlopen

#https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-BS-In-Computer-Science-Software-Development.aspx
#https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-BS-In-Computer-Science-Game-Systems.aspx
def testParser(url):
    req = Request(url)
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4056.0 Safari/537.36 Edg/82.0.432.3')
    content = urlopen(req).read().decode()
    parser = CourseParser()
    parser.feed(content)
    return parser.getData()

class CourseParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.courses=[]
        self.allowed=False
        
    def handle_starttag(self, tag, attrs):
        self.allowed=False
        for attr in attrs:
            if attr[0]=='class':
                if attr[1]=='CDMExtendedCourseInfo':
                    self.allowed=True

    def handle_data(self, data):
        data = data.strip()
        if self.allowed==True and data !='':
            self.courses.append(data)
        
    def getData(self):
        return self.courses
