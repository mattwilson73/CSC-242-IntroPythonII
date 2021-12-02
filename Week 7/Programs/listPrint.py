def printLst(lst):
    'print a list lst, one element per line, non-destructively'
    if len(lst) > 0:
        print(lst[0])
        printLst(lst[1:])
            
def listPrint(lst):
    'print elements of a multi-dimensional list, one per line'
    if len(lst) > 0:
        if type(lst[0]) == list:
            listPrint(lst[0])
        else:
            print(lst[0])
        listPrint(lst[1:])

