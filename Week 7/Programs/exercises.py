def vertical(n):         #1
    if n < 10:           #2
        print(n)         #3
    else:                #4
        print(n % 10)    #5
        vertical (n//10) #6

def printLst(lst):
    if len(lst) == 0:
        return
    else:
        print(lst[0])
        printLst(lst[1:])
        
def cheer(n):
    if n <= 1:
        print ("Hurrah")
    else:
        print("Hip")
        cheer(n-1)

def pattern(n):
    if n <= 1:
        print (1, end = " ")
    else:
        pattern(n-1)
        print(n, end = " ")
        pattern(n-1)

def recLenLst(lst):
    'return the length of lst recursively'
    if lst == []:
        return 0
    else:
        return 1 + recLenLst(lst[1:])



printLst([1,2,3,4,5])