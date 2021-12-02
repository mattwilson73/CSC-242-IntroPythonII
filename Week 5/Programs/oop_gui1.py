from tkinter import Button, Frame
     
class HelloClass(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()
        
    def make_widgets(self):
        Button(self, text='Hello event world', command=self.hello).pack()

    def hello(self):
        print('Hello class method world')    # self.hello is a class method

HelloClass().mainloop()
