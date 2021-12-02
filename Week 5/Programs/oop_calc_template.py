from tkinter import Frame, Button, Entry, END

class Calculator(Frame):
    """
      The calculator has a layout like this:
      < display >
      7 8 9 *
      4 5 6 /
      1 2 3 -
      0 = + C
    """
    
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.make_widgets()
        self.grid()

    def make_widgets(self):
        pass

    def click(self, key):
        pass

Calculator().mainloop()
