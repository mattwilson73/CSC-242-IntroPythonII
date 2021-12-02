from tkinter import Tk, Frame, Button, LEFT, RIGHT  # Get Tk widget classes
from oop_gui2 import Hello                   # Get the subframe class

class HelloPlus(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        HelloPlus.make_widgets(self)
        
    def make_widgets(self):
        Button(self, text='Exit', command=self.parent.destroy).pack(side=LEFT)
        Hello(self).pack(side=RIGHT)     # Attach Hello instead of running it

root = Tk()
HelloPlus(root).mainloop()
