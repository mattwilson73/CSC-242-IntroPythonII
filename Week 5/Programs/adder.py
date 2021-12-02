from tkinter import Button, Entry, Label,Tk,W
from tkinter.messagebox import showinfo

class Adder(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Simple Adder')
        self.make_widgets()
        
    def add(self):
        left=self.leftEntry.get()
        right=self.rightEntry.get()

        try:
            l = float(left)
        except ValueError:
            showinfo(title='Calculation', message="Error. The left side of the equation cant convert to float.")
            return
        try:
            r = float(right)
        except ValueError:
            showinfo(title='Calculation', message="Error. The right side of the equation cant convert to float.")
            return
        self.answerLabel.config(text=str(l+r))

    def make_widgets(self):
        self.leftEntry = Entry(self)
        self.leftEntry.grid(row=0,column=0)
        Label(self,text='+').grid(row=0,column=1)
        self.rightEntry = Entry(self)
        self.rightEntry.grid(row=0,column=2)
        Label(self,text='=').grid(row=0,column=3)
        self.answerLabel = Label(self,text='  ')
        self.answerLabel.grid(row=0,column=4)
        Button(self,text="Add", command=lambda:self.add()).grid(row=1,column=1)
        
