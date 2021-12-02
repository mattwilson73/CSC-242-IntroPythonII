class GroceryListManager (object):
    'The constructor'
    def __init__(self, filename='grocery.txt'):
        pass

    def getCount(self):
        'sets a count of items from the grocery list'
        pass

    def addItem(self,text):
        'adds an item to the grocery list'
        pass

    def getItem(self, index):
        'gets a specific item from the grocery list'
        pass

    def removeItem(self, number):
        'removes an item from the grocery list'
        pass

    def __iter__(self):
        'iterates through items in the grocery list.'
        pass
    
    def saveToFile(self):
        'saves the items to a file.  The file is completely over written'
        pass

    def __str__(self):
        pass

    def loadFile(self):
        'loads Grocery list items from a file.  Existing items in the list are removed'
        pass
