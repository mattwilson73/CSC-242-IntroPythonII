#Completed during the lab session by myself.
#Matt Wilson


def recProd(k,n):
    
    if k == n:
        return n
    if k > n:
        return 1
    
    else:
        return k * recProd(k+1,n)



def printTriangle(m,i):
    
    if m <= 0:
        return
    
    else:    
        print(' '*i + '*'*m)
        printTriangle(m-2,i+1)






printTriangle(5,5)
        