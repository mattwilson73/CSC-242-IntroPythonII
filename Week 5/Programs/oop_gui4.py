from tkinter import Tk, Button, RIGHT
from oop_gui2 import Hello
     
class HelloExtender(Hello):
    def __init__(self, parent=None):
        Hello.__init__(self, parent)
        self.parent = parent
        HelloExtender.make_widgets(self)
        #self.make_widgets()
        
    def make_widgets(self):                       # extend method here
        Button(self, text='Exit', command=self.parent.destroy).pack(side=RIGHT)

root = Tk()
HelloExtender(root).mainloop()
