#Worked on this homework assignment by myself.

import random

from tkinter import Label, Tk, Entry, Button
from tkinter.messagebox import showinfo

class Cookie(object):

    #built in cookies, other cookies are allowed
    cookieTypes=['chocolate chip','peanut butter','oatmeal','mint chocolate','raisin','vegan']
    
    def __init__(self,cookieType=None):
        'constructor. Assigns a cookie name or randomly picks one from the built in cookie types'
        if cookieType==None:
            self.cookie = self.cookieTypes[random.randint(0,len(self.cookieTypes)-1)]
        else:
            self.cookie = cookieType

    def getCookieType(self):
        'return the cookie type'
        return self.cookie

    def __str__(self):
        'string representation of cookie'
        return self.cookie 

    def __repr__(self):
        'pythin representation of cookie'
        return "Cookie('{}')".format(self.cookie)

class CookieJar(object):

    def __init__(self):
        'cookie jar constructor.  sets up the jar to hold cookies'
        self.jar = []
        

    def getCount(self):
        'returns a count of all cookies'
        return len(self.jar)

    def addCookie(self,cookie):
        'adds a cookie object to the jar'
        self.jar.append(cookie)

    def getCookies(self):
        'returns a list of all the cookies in the jar'
        return self.jar

    def getCookieCount(self,cookieTypeName):
        'return the count of a specific type of cookie.  cookieTypeName is a string'
        count=0
        for c in self.jar:
            if c.getCookieType() == cookieTypeName:
                count += 1
        return count
            
    
        
    def getAllCookieCount(self):
        'returns a dictionary of all the types of cookies in the jar and their count'
        cd = {}
        for c in self.jar:
            if c.getCookieType() not in cd:
                cd[c.getCookieType()] = 0
            if c.getCookieType() in cd:
                cd[c.getCookieType()] += 1
                 
        return cd


    def __iter__(self):
        'returns an iterator'
        return iter(self.jar)

    def __contains__(self,cookieTypeName):
        'checks if a cookie is in the jar based on its name. cookieTypeName is a string'
        
        for c in self.jar:
            if c.getCookieType() == cookieTypeName:
                return True
        return False

    def loadCookies(self):
        'loads the cookies from a file as Cookie objects.  Clears exisiting cookies in memory before it loads. returns True if successful and False if not.'
        try:
            infile = open('cookies.txt','r')
            content = infile.readlines()
            infile.close
            self.jar.clear()
            for c in content:
                newcookie = c.strip()
                self.jar.append(newcookie)
            return True
         
        except:
            return False
                
    def saveCookies(self):
        'writes (does not append) the cookies to a file. returns True if successful and False if not.'
        try:
            outfile = open('cookies.txt','w')
            for c in self.jar:
                print(c.getCookieType(),file=outfile)
            outfile.close()
            return True
        except:
            return False


class AverageCalculator(object):
    def __init__(self,fileName='grades.txt'):
        self.fileName = fileName

    def loadGrades(self):
        'loads grades from a file, grades.txt used as defult'
        try:
            
            self.gradelist = []
            infile = open(self.fileName,'r')
            for line in infile:
                studentgrades = line.strip().split(',')
                for x in range(len(studentgrades)):
                    studentgrades[x] = float(studentgrades[x])
                self.gradelist.append(studentgrades)
            infile.close()
            return True
        except:
            return False


    def writeLetterGrades(self):
        'Determines letter grade for each student and writes numerical average and letter to file'
        outfile = open('avg-'+self.fileName+'.txt','w')
        
        for num in self.getStudentAverages():
            if num >= 90:
                letter = 'A'
            if num <90 and num >= 80:
                letter = 'B'
            if num <80 and num >= 70:
                letter = 'C'
            if num <70 and num >= 60:
                letter = 'D'
            if num < 60:
                letter = 'F'
            print(num,':',letter,file=outfile)
        outfile.close()
            
                

    def getStudentAverages(self):
        'returns a list of the averages for all students'
        avglist = []
        for studentgrades in self.gradelist:
            avglist.append((sum(studentgrades)/len(studentgrades)))
        return avglist
    
    def getCourseAverage(self):
        'returns overall class average grade'
        avglist = []
        for studentgrades in self.gradelist:
            avglist.append((sum(studentgrades)/len(studentgrades)))
        return(sum(avglist)/len(avglist))
        



class MortgageCalculator(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Mortgage calculator')
        self.make_widgets()
                

    def calculateMortgage(self):
        'calculates monthly mortgage payments and displays in new window'
        
        try:    
            p = float(self.principal.get())
        except ValueError:
            showinfo(title='Monthly Payment',message='Error. Incorrect value entered for principal.')
        
        try:
            n = float(self.term.get())
        except ValueError:
            showinfo(title='Monthly Payment',message='Error. Incorrect value entered for term.')
                
        try:
            r = float(self.interest.get())
        except ValueError:
            showinfo(title='Monthly Payment',message='Error. Incorrect value entered for interest.')
        
        try:
            m = (p*r/1200)/(1-(1+r/1200)**(-12*n))
        except ZeroDivisionError:
            showinfo(title='Monthly Payment',message='Error. Unable to calculate payment.')
            
        
        showinfo(title='Monthly Payment',message='Your monthly payment is ${:.2f}.'.format(m))



    def make_widgets(self):
        
        
        Label(self,text='Principal').grid(row=0,column=0)
        self.principal = Entry(self)
        self.principal.grid(row=0,column=1)
        
        Label(self,text='Interest Rate').grid(row=1,column=0)
        self.interest = Entry(self)
        self.interest.grid(row=1,column=1)
        
        Label(self,text='Term in Years').grid(row=2,column=0)
        self.term = Entry(self)
        self.term.grid(row=2,column=1)
        
        Button(self,text='Calculate Payment',command=lambda:self.calculateMortgage()).grid(row=3,column=1)



MortgageCalculator().mainloop()
