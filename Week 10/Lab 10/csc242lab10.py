#Completed by myself during the lab
#Matt Wilson


import os

def nestingCount(pathname):
    largest=0
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        if os.path.isdir(n):
            depth = nestingCount(n)
            if depth > largest:
                largest = depth
    return 1+largest

from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import urlopen

class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.foundTitle = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            print('there was a title!!!')
            self.foundTitle == True
        print('tag:   '+tag)
#        print('attrs',attrs)
        
        
    def handle_endtag(self, tag):
#        print('tag2'+tag)
        if tag == 'title':
            self.foundTitle == True

    def handle_data(self, data):
        #only run if title tag is found
        if self.foundTitle == True:
            self.title= data
            print(data)
            print('working')
            print(tag)
            print(attrs)
    def getTitle(self):
        return self.title

from random import randrange
class Magic8Ball(object):

    def __init__(self, q=[]):
        'the constructor'
        if len(q)==0:
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
        self.current=randrange(0,len(self.q))

    def shake(self):
        'get the next answer'
        self.current=randrange(0,len(self.q))

    def get(self):
        'get the current answer'
        return self.q[self.current]

    def numAnswers(self):
        'get the number of answers in the ball'
        return len(self.q)

    def __iter__(self):
        'get the iterator'
        return iter(self.q)

    def __str__(self):
        'string representation'
        return 'I am a Magic 8 Ball with {} answers'.format(len(self.q))

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END
from tkinter.messagebox import showinfo


class BizzaroGUI(Tk):
    'Number guessing app'
    def __init__(self,ball=Magic8Ball(),parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title('Bizzaro GUI')
        
        self.ball = ball
        
        self.myParser = TitleParser()
        
        self.make_widgets()
        
        
    def getTitle(self):
        #I left the following line as hint.
        #
        url = self.urlentry.get()
        content =urlopen(url).read().decode()
        self.myParser.feed(content)

        
        showinfo(title='The answer...',message=self.myParser.getTitle())

    def getFolderDepth(self):
        pathname = self.folderentry.get()
        depth = nestingCount(pathname)
        showinfo(title='The answer...',message=depth)

    def getAnswer(self):
        self.ball.shake()
        showinfo(title='The answer...',message='The answer to your question {} is {}.'.format(self.qentry.get(),self.ball.get()))
        self.qentry.delete(0,END)

    def make_widgets(self):
        
        Label(self,text='Enter URL:').grid(row=0,column=1)
        self.urlentry = Entry(self)
        self.urlentry.grid(row=0,column=2)
        Button(self,text='Get Title', command=lambda:self.getTitle()).grid(row=0,column=3)
        
        
        Label(self,text='Enter Folder:').grid(row=1,column=1)
        self.folderentry = Entry(self)
        self.folderentry.grid(row=1,column=2)
        Button(self,text='Get Depth Count', command=lambda:self.getFolderDepth()).grid(row=1,column=3)
    
    
        Label(self,text='Ask Question:').grid(row=2,column=1)
        self.qentry = Entry(self)
        self.qentry.grid(row=2,column=2)
        Button(self,text='Get Magic Answer', command=lambda:self.getAnswer()).grid(row=2,column=3)






BizzaroGUI().mainloop()


testurl = 'http://zoko.cdm.depaul.edu'

