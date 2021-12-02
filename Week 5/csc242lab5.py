#Completed by myself


from tkinter import Label, Tk, Entry, Button, END
from tkinter.messagebox import showinfo

class BankAccount(object):
    'bank account class'
    def __init__(self, balance=0):
        self.balance = balance
        

    def withdraw(self,amount):
        'withdraw funds'
        self.balance -= amount

    def deposit(self, amount):
        'add funds'
        self.balance += amount

    def balance(self):
        'get balance '
        return self.balance

    
        
class ATM(Tk):
    def __init__(self,account=BankAccount(),parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.account = account
        self.title('ATM')
        self.make_widgets()

    def withdraw(self):
        'withdraw funds from BankAccount and update GUI'
        print('withdraw')
        
        wamount = float(self.input.get())
        self.account.withdraw(wamount)
        
        
        

    def deposit(self):
        'add funds to BankAccount and update GUI'
        damount = float(self.input.get())
        print(damount)

    def updateBalance(self):
        'Update account balance label in GUI'
        bal = self.account.balance()
        
        self.balance.configure(text=str(bal))
        
#        self.balance.configure(text=str(self.account.balance))

    def make_widgets(self):
        'Create widgets'
#        self.updateBalance()
        Label(self,text='Balance:').grid(row=0,column=0)
        
        Label(self,text='Amount:').grid(row=1,column=0)
        
        self.bal = Label(self)
        self.bal.grid(row=0,column=1)
        
        
        self.input = Entry(self)
        self.input.grid(row=1,column=1)
        
        Button(self,text='Withdraw',command=lambda:self.withdraw()).grid(row=2,column=0)
        
        Button(self,text='Deposit',command=lambda:self.deposit()).grid(row=2,column=1)
        




ATM().mainloop()
