def printLst(lst):
    if len(lst) == 0:
        return
    else:
        print(lst[0])
        printLst(lst[1:])
