"""
      The calculator has a layout like this:
      < display >
      7 8 9 *
      4 5 6 /
      1 2 3 -
      0 = + C
"""
       
from tkinter import Tk, Button, Entry, END
       
def click(key):
    if key == '=':
        try:
            result = eval(entry.get())
            entry.insert(END, " = " + str(result))
        except:
            entry.insert(END, "--> Error!")
    elif key == 'C':
        entry.delete(0, END) # clear entry
    else:
        # The previous calculation has been done, so clear entry
        if '=' in entry.get() or 'Error' in entry.get():
            entry.delete(0, END)
        entry.insert(END, key)

root = Tk()
root.title("Calculator")

btn_list = [
'7', '8', '9', '*',
'4', '5', '6', '/',
'1', '2', '3', '-',
'0', '=', '+', 'C']
       
# create all buttons with a loop
r = 1
c = 0
for b in btn_list:
    rel = 'ridge'
    cmd = lambda x=b: click(x)
    Button(root,text=b,width=7, relief = rel,command=cmd).grid(row=r,column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

# use Entry widget for an editable display
entry = Entry(root, width=33)
entry.grid(row=0, column=0, columnspan=4)

root.mainloop()
