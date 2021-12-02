#Completed during the lab session.
#Worked with Matthew Theodoropoulos on problem 1.


def extractStr(lst):
    #Base case
    if len(lst) == 0:
        return ''

    #If item lst[0] is a string
    if type(lst[0]) == str:
        return lst[0] + extractStr(lst[1:])
    
    #If item lst[0] is a list
    if type(lst[0]) == list:
        lst = lst[0] + lst[1:]
        return extractStr(lst)

    else:
        return extractStr(lst[1:])
    


def totalNumericValue(lst):
    
    #Base Case
    if len(lst) == 0:
        return 0
    
    if type(lst[0]) == int:
        return lst[0] + totalNumericValue(lst[1:])
    
    if type(lst[0]) == list:
        lst = lst[0] + lst[1:]
        return totalNumericValue(lst)
    
    else:
        return totalNumericValue(lst[1:])
    
    