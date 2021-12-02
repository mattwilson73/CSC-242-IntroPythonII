from tkinter import Label, Tk
#import tkinter

# Create a GUI window
root = Tk()

# Create a Label widget in the master window
widget = Label(master = root, text = 'Hello GUI world!')

# Place the Label widget into the master window
widget.pack()

# Invoke the main loop on the master window
root.mainloop()
