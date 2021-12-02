#Completed this homework assignment by myself.
#Matt Wilson

def recLessThan(n):
    if n > 0:    
        print(' '*(n-1) + '*')
        recLessThan(n-1)
    
    if n >= 1:
        print(' '*(n-1)+'*')
        
 
def recHourGlassShape(c,n,i):
    'c is the character to display, n is number of characters on each line and i is indentation'

    if n > 0:
        print(' '*i + c*(n))
        recHourGlassShape(c,n-2,i+1)

    if n > 0:
        print(' '*(i)+c*n)
    
 
def recAdder(lst):
    'return the sum of all numbers in a list.'
    
    if len(lst) == 0:
        return 0
    
    else:
        
        if type(lst[-1]) == int or type(lst[-1]) == float:
            return( lst[-1]) + recAdder(lst[:-1])
    
        else:
            return recAdder(lst[:-1])


def recEvenNumberCounter(lst):
    'return a count of all the even numeric values (ints and floats) in the list'
    
    if len(lst) == 0:
        return 0
    
    else:
        
        if type(lst[-1]) == int or type(lst[-1]) == float:
            if lst[-1] % 2 == 0:
                return 1 + recEvenNumberCounter(lst[:-1])
            
        return recEvenNumberCounter(lst[:-1])


def recStringMerge(a,b):
    'Merge two string together recursivly'
    
    if len(a) == 0 and len(b) == 0:
        return ''
    
    if len(a) == 0 and len(b) != 0:
        return b[0] + recStringMerge([],b[1:])
    
    if len(a) != 0 and len(b) == 0:
        return a[0] + recStringMerge(a[1:],[])
    
    if len(a) != 0 and len(b) != 0:
        return a[0] + b[0] + recStringMerge(a[1:],b[1:])


    


