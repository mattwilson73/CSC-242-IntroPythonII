#Worked on this homework assignment by myself


#PROBLEM 1
class Order(object):

    def __init__(self,name='',date='',costPerPerson=0,guests=0,taxRate=0):
        '''Initialize  the order object.  Note: only way to set values on the object
        is by using the constructor'''
        self.name = name
        self.date = date
        self.costPerPerson = costPerPerson
        self.guests = guests
        self.taxRate = taxRate
        

    def getName(self):
        'get the event name'
        return self.name

    def getDate(self):
        'get the event date'
        return self.date

    def getTotalGuests(self):
        'get the total guests'
        return self.guests

    def getCostPerPerson(self):
        'get the cost per person'
        return self.costPerPerson

    def getTax(self):
        'get the tax'
        return self.taxRate

    def calculateTotal(self):
        'calculcate the event total including tax'
        tcost = self.costPerPerson * self.guests
        taxcost = tcost * self.taxRate
        return tcost + taxcost

    def __str__(self):
        'str representation.'
        return "{}:{}:{}:{}:{}".format(self.name,self.date,self.costPerPerson,
                self.guests,self.taxRate)
    
    def __repr__(self):
        'python representation'
        return "Order('{}','{}',{},{},{})".format(self.name,self.date,self.costPerPerson,
                     self.guests,self.taxRate)
    
#PROBLEM 2 and 3:
class OrderManager(object):

    #START OF PROBLEM 2
    def __init__(self, filename='inventory.txt'):
        'Initialize the Order Manager class'
        self.filename = filename
        self.orders = []
        

    def addOrder(self,order):
        'adds an order to the manager'
        self.orders.append(order)
        return True
    
    def getOrdersTotal(self):
        'returns the total cost of all the orders managed.'
        
        total = 0
        for order in self.orders:
            total += order.calculateTotal()
        
        return total

    def getCountOfOrders(self):
        'returns a count of how many orders there are'
        return len(self.orders)

    def getAverageCost(self):
        'returns the average cost of the orders. Returns 0 if there are no orders'
        if len(self.orders) == 0:
            return 0
        else:
            return (self.getOrdersTotal() / len(self.orders))

    def getAllEventNames(self):
        'gets a list of the names of all the orders. if there are no orders the list should be empty'
        l = []
        for order in self.orders:
            l.append(order.getName())
        return l

    def getMostExpensiveOrder(self):
        'gets the order with the highest total. Returns None if there are no orders.'
        
        highcost = 0
        for order in self.orders:
            if order.calculateTotal() >= highcost:
                highcost = order.calculateTotal()
        
        for order in self.orders:
            if order.calculateTotal() == highcost:
                return order

    def __iter__(self):
        'iterator'
        return iter(self.orders)

    #START OF PROBLEM 3

    def loadOrders(self):
        'Read the order information from the file. You should clear out any orders that are in the manager before you load.Returns True if successful and False if there is an error'
        try:
            infile = open(self.filename,'r')
            content = infile.readlines()
            infile.close()
            self.orders.clear()
            for o in content:
                oinfo = o.strip().split(':')
                self.addOrder(Order(oinfo[0],oinfo[1],float(oinfo[2]),
                                    int(oinfo[3]),float(oinfo[4])))
            return True
        except:
            return False
    
        
    def writeOrdersToFile(self):
        'write all orders to the file overwriting the existing file. Returns True if successful and False if there is an error'
        
        try:
            
            outfile = open(self.filename,'w')
    
            for order in self.orders:
                print(order,file = outfile)
            outfile.close()
            
            return True
        
        except:
            return False
        

        
        
        




