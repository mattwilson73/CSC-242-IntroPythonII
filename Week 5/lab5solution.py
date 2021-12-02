# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:13:10 2020

@author: Matt
"""

from tkinter import Label, Tk, Entry, Button, END
from tkinter.messagebox import showinfo

class BankAccount(object):
    'bank account class'
    def __init__(self, balance=0):
        self.total=balance
    
    def withdraw(self,amount):
        'withdraw funds'
        if(amount>self.total):
            return False
        else:
            self.total=self.total-amount
        return True
    
    def deposit(self, amount):
        'add funds'
        self.total=self.total+amount
        return True
    
    def balance(self):
        'get balance'
        return self.total



class ATM(Tk):
    def __init__(self,account=BankAccount(),parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title('ATM')
        self.make_widgets()
        self.account=account
        self.updateBalance()
    
    def withdraw(self):
        'withdraw funds from BankAccount and update GUI'
        try:
            amount = float(self.aEntry.get())
            if self.account.withdraw(amount)==True:
                showinfo(title='Transaction', message='Success. Funds withdrawn')
            else:
                showinfo(title='Transaction', message='Error. Error. Unable to withdraw funds.')
                self.aEntry.delete(0,END)
            self.updateBalance()
        except ValueError:
            showinfo(title='Transaction', message='Amount entered is not a number.')
    
    def deposit(self):
        'add funds to BankAccount and update GUI'
        try:
            amount = float(self.aEntry.get())
            if self.account.deposit(amount)==True:
                showinfo(title='Transaction', message='Sucessful deposit')
                self.aEntry.delete(0,END)
                self.updateBalance()
        except ValueError:
            showinfo(title='Transaction', message='Amount entered is not a number.')
    
    def updateBalance(self):
        'Update account balance label in GUI'
        self.bLabel.config(text=self.account.balance())
    
    def make_widgets(self):
        'Create widgets'
        Label(self,text='Balance:').grid(row=0,column=0)
        self.bLabel = Label(self)
        self.bLabel.grid(row=0,column=1)
        
        Label(self,text='Amount:').grid(row=1,column=0)
        self.aEntry = Entry(self)
        self.aEntry.grid(row=1,column=1)
        
        Button(self, text="Withdraw", command=lambda:self.withdraw()).grid(row=3,column=0)
        Button(self, text="Deposit", command=lambda:self.deposit()).grid(row=3,column=1)
        
        
ATM().mainloop()