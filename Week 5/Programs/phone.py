from tkinter import Tk, Button,Entry,Frame,END

class Phone(Tk):
    def  __init__(self, parent = None):
        Tk.__init__(self, parent)
        self.make_widgets()
        
    


    def click(self, key):
        if len(self.entry.get())==3 or len(self.entry.get())==7 :
            self.entry.insert(END, '-')
        if len(self.entry.get())<12:
            self.entry.insert(END, key)

    def make_widgets(self):
        labels = [['1', '2', '3'],     # phone dial label texts
          ['4', '5', '6'],     # organized in a grid
          ['7', '8', '9'],
          ['*', '0', '#']]

        f = Frame(self)
        f.pack()

        for r in range(4):      # for every row r = 0, 1, 2, 3
            for c in range(3):      # for every row c = 0, 1, 2
                # create label for row r and column c
                cmd= lambda x=labels[r][c]: self.click(x)
                btn = Button(f,
                               padx=10,
                              text=labels[r][c], command=cmd)  # label text
                # place label in row r and column c
                
                btn.grid(row=r, column=c)  
        self.entry=Entry(self)
        self.entry.pack()

Phone().mainloop()
