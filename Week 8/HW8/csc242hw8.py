#Completed by myself
#Matt Wilson


def recNestedListSumOfNumbers(lst):
    '''
    recursively loops through a nested list and returns the sum of all
    int and float items
    '''
    
    if len(lst) == 0:
        return 0
    
    if type(lst[0]) == int or type(lst[0]) == float:
        return lst[0] + recNestedListSumOfNumbers(lst[1:])


    if type(lst[0]) == list:
        lst = lst[0] + lst[1:]
        return recNestedListSumOfNumbers(lst)
    
    else:
        return recNestedListSumOfNumbers(lst[1:])
    
    
    
import os


#FIXME Need to print parent file dir.
#!!! FIX BEFORE SUBMITING !!!
def dirPrint(pathname, indent):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''


    for item in os.listdir(pathname):
        
        n = os.path.join(pathname, item)

        if os.path.isdir(n):
            print(' '*indent + n)
            dirPrint(n,indent+1)
        
        else:
            pass
        
        
dirPrint('count')


import os





def fileCountWithLetter(pathname, letter):
    localCount=0
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname. Returns a count of files with the letter in the name'''
    
    for item in os.listdir(pathname):
        
        n = os.path.join(pathname,item)
        
        if os.path.isdir(n):
            fileCountWithLetter(n,letter)
            
            
        else: #n is a file
            f = open(n,'r')
            s = f.read()
            if s.find(letter):
                retVal = fileCountWithLetter(n,letter)
                localCount += 1
                return retVal + localCount



#fileCountWithLetter('Test','a')



    
from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END,filedialog
from tkinter.messagebox import showinfo

###EXAMPLE############

class FileDialogExample(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('FileDialog Example')
        self.make_widgets()
    def getPath(self):
        path = filedialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        print(path)
        
    def make_widgets(self):
        Button(self, text="Print Path", command=lambda:self.getPath()).grid(column=0,row=0)

#FileDialogExample().mainloop()
####END EXAMPLE########


class FileCountWithLetterExplorer(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('File Count with Letter Explorer')
        self.make_widgets()

    def getPath(self):
        path = filedialog.askdirectory(parent=self,initialdir="/",title='Please select a directory')
        self.dirPath.delete(0,END)
        self.dirPath.insert(END, path)
 
    def fileCountWithLetter(self,pathname, letter):
        pass

    def make_widgets(self):
        pass


def fileContentsCount(folder,content):
    'return a count of files that have the specific content'
    localCount = 0
    for item in os.listdir(folder):
        
        n = os.path.join(folder,item)
        
        if os.path.isdir(n):
            fileCountWithLetter(n,content)
            
            
        else: #n is a file
            f = open(n,'r')
            s = f.read()
            if s.find(content) > 0:
                
                
                localCount += 1
                return localCount
            





# DONT FORGET TO PUT PROBLEM 5 HERE

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END,filedialog,Scale, HORIZONTAL
from tkinter.messagebox import showinfo


class BrokenBoneWard(Tk):
    'Hospital Patient Intake Class'
    
    def __init__(self,parent=None):
        '''
        Constructor
        '''
        Tk.__init__(self,parent)
        self.title('Broken Bone Ward Intake')
        self.make_widgets()
        
    def saveinfo(self):
        '''
        Saves patient info in a "Name,Age,Time Waited,Pain,Severity" format to
        "PatientLogs.txt"
        '''
        
        try:
            outfile = open('PatientLogs.txt','a+')
            print('{},{},{},{},{}'.format(self.nameentry.get(),self.ageentry.get()
            ,self.timeentry.get(),self.pain.get(),self.sev),file=outfile)
    
            outfile.close()
            
            
        except:
            showinfo(title='File Save Error',message='Error saving information to file')
        
        
        
    def runinfo(self):
        '''
        Checks for entry errors and then determines the severity of the patient.
        Severity is based off of age and pain of patient.
        Calls saveinfo to log information to file.
        '''
        
        if self.nameentry.get() == '':
            showinfo(title='Entry Error',message='Missing Name')
            return
        
        if self.ageentry.get() == '':
            showinfo(title='Entry Error',message='Missing Age')
            return
        
        
        if self.timeentry.get() == '':
            showinfo(title='Entry Error',message='Missing Time Waited')
            return        
    
        try:
            name = self.nameentry.get()
            age = int(self.ageentry.get())
            time = int(self.timeentry.get())
            pain = int(self.pain.get())
                
        except ValueError:
            showinfo(title='Entry Error', message='Invalid Age or Time Entry')
            return
        
        else:    
            self.sev = 'Low'
            
        if pain >= 5 and pain < 8:
            self.sev = 'Medium'
            
        if (age <= 10 or age >= 70) or pain >= 8:
            self.sev = 'High'
            
            
        showinfo(title='Severity',message='Patient Determined to be {} Severity'.format(self.sev))
        
        self.saveinfo()

        self.nameentry.delete(0,END)
        self.ageentry.delete(0,END)
        self.timeentry.delete(0,END)
        
        
        
        
    def make_widgets(self):
        '''
        Creates widgets for the GUI
        '''
        
        Label(self,text='Name:').grid(row=0,column=1)
        self.nameentry = Entry(self)
        self.nameentry.grid(row=0,column=2)
        
        Label(self,text='Age:').grid(row=1,column=1)
        self.ageentry = Entry(self)
        self.ageentry.grid(row=1,column=2)
        
        Label(self,text='Time Waited:').grid(row=2,column=1)
        self.timeentry = Entry(self)
        self.timeentry.grid(row=2,column=2)
        
        Label(self,text='Level of Pain:').grid(row=3,column=1)
        self.pain = Scale(self,from_=0,to=10, orient=HORIZONTAL)
        self.pain.grid(row=3,column=2)
        
        Button(self,text='Intake Patient',command=lambda:self.runinfo()).grid(row=4,column=1,columnspan=2)

























#print(fileContentsCount('Test-2','April'))
#print(fileContentsCount('Test-2','like'))
#print(fileContentsCount('Test-2','e'))   



#print(recNestedListSumOfNumbers([]))                               
#print(recNestedListSumOfNumbers([[1,2,3,4,5,6,7,8,9,10]]))
#print(recNestedListSumOfNumbers([[[[[[[[[5]]]]]]]]]))
#print(recNestedListSumOfNumbers([[1,2,3],[4,[[[5,[[[6]]]]]]]]))
#print(recNestedListSumOfNumbers([[[[[[[[[10,20]]]]]]]]]))


#dirPrint('Test',2)
#dirPrint('count',5)

#print('FILE COUNT WITH LETTER: ', fileCountWithLetter('Test','a'))
#print('FILE COUNT WITH LETTER: ', fileCountWithLetter('Test','i'))
#print('FILE COUNT WITH LETTER: ', fileCountWithLetter('Test','e'))

#FileCountWithLetterExplorer().mainloop()


#print("FILE CONTENTS COUNT" , fileContentsCount('Test-2','April'))
#print("FILE CONTENTS COUNT" , fileContentsCount('Test-2','like'))
#print(f"FILE CONTENTS COUNT" ,ileContentsCount('Test-2','e'))   


