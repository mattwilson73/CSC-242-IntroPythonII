import random

class Magic8Ball(object):

    def __init__(self, q=[]):
        'the constructor'
        
        if len(q) == 0:      
            q.append('It is certain')
            q.append('It is decidedly so')
            q.append('Without a doubt')
            q.append('Yes definitely')
            q.append('You may rely on it')
            q.append('As I see it, yes')
            q.append('Most likely')
            q.append('Outlook good')
            q.append('Yes')
            q.append('Signs point to yes')
            q.append('Reply hazy try again')
            q.append('Ask again later')
            q.append('Better not tell you now')
            q.append('Cannot predict now')
            q.append('Concentrate and ask again')
            q.append("Don't count on it")
            q.append('My reply is no')
            q.append('My sources say no')
            q.append('Outlook not so good')
            q.append('Very doubtful')
        
        self.q = q
        self.shake()

    def shake(self):
        'get the next answer'
        num = random.randrange(0,self.numAnswers())
        self.currentans = num
        

    def get(self):
        'get the current answer'
        return self.q[self.currentans]

    def numAnswers(self):
        'get the number of answers in the ball'
        return len(self.q)

    def __iter__(self):
        'get the iterator'
        return iter(self.q)

    def __str__(self):
        'string representation'
        return 'I am a Magic 8 Ball with {} answers'.format(self.numAnswers())






from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END
from tkinter.messagebox import showinfo

class Magic8BallGame(Tk):

    def __init__(self,ball=Magic8Ball(),parent=None):
        Tk.__init__(self, parent)
        self.ball = ball
        self.title('Magic 8 Ball')
        
        self.make_widgets()

    def shake(self):
        self.ball.shake()
        showinfo(title="I'm shaking!",message='I am searching into the mystic realms (RAM) for an answer.')

        
        
    def askQuestion(self):
        
        showinfo(title='The answer',message = 'The answer to your question {} is {}.'.format(self.entry.get(),self.ball.get()))
        self.entry.delete(0,END)
        
    def make_widgets(self):
        
        Label(self,text='Please ask a question:').pack(side=TOP)
        
        self.entry = Entry(self)
        self.entry.pack()
        
        Button(self,text='Shake', command=self.shake).pack(side=LEFT)
        
        Button(self,text='Ask', command=self.askQuestion).pack(side=RIGHT)
        
        
        
        
        
        
        
        
        
        
        
        
    
Magic8BallGame().mainloop()
