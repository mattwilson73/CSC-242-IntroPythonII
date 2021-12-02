from tkinter import Frame, Button, LEFT
     
class Hello(Frame):                            # An extended Frame
    def __init__(self, parent=None):
        Frame.__init__(self, parent)           # Call the superclass constructor
        self.pack()
        self.data = 0
        Hello.make_widgets(self)                # Attach widgets to self
        #self.make_widgets()
        
    def make_widgets(self):
        Button(self, text='Hello frame world!', command=self.message).pack(side=LEFT)

    def message(self):
        self.data += 1
        print('Hello frame world {}!'.format(self.data))

Hello().mainloop()
