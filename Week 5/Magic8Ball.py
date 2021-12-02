import random

class Magic8Ball(object):

    def __init__(self, answers=[]):
        'the constructor'
        '''
            answers.append('It is certain')
            answers.append('It is decidedly so')
            answers.append('Without a doubt')
            answers.append('Yes definitely')
            answers.append('You may rely on it')
            answers.append('As I see it, yes')
            answers.append('Most likely')
            answers.append('Outlook good')
            answers.append('Yes')
            answers.append('Signs point to yes')
            answers.append('Reply hazy try again')
            answers.append('Ask again later')
            answers.append('Better not tell you now')
            answers.append('Cannot predict now')
            answers.append('Concentrate and ask again')
            answers.append("Don't count on it")
            answers.append('My reply is no')
            answers.append('My sources say no')
            answers.append('Outlook not so good')
            answers.append('Very doubtful')
        '''

    def shake(self):
        'get the next answer'
        pass

    def get(self):
        'get the current answer'
        pass

    def numAnswers(self):
        'get the number of answers in the ball'
        pass

    def __iter__(self):
        'get the iterator'
        pass

    def __str__(self):
        'string representation'
        pass

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END
from tkinter.messagebox import showinfo

class Magic8BallGame(Tk):

    def __init__(self,ball=Magic8Ball(),parent=None):
        Tk.__init__(self, parent)
        pass

    def shake(self):
        pass
    
    def askQuestion(self):
        pass

    def make_widgets(self):
        pass

snarkyAnswers=['I dont care','leave me alone','buzz off','what do you want again?']
    
Magic8BallGame().mainloop()
