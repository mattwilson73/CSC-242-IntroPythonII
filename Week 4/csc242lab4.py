#Completed by myself outside of lab time.

from tkinter import Label,Tk
class Sign(Tk):
    
    def __init__(self,textl=[],parent=None):
        Tk.__init__(self, parent)
        defulttxt = ['GREAT DEAL!','Android 1.0 Phones for $10!','Security vulnerabilities included!']
        
        if len(textl) == 0:
            self.textl = defulttxt
            self.title('Warning')
        else:
            self.textl = textl
            self.title('Digital Sign')
            
        self.make_widgets()

    def make_widgets(self):
       Label(self,text=self.textl[0]).pack()
       Label(self,text=self.textl[1]).pack() 
       Label(self,text=self.textl[2]).pack()


