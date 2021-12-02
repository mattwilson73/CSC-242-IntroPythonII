def a(x):
    print(x)
    ret = b(x+1)
    print(x)
    return ret+1

def b(x):
    print(x)
    ret = c(x+1)
    print(x)
    return ret+1
    

def c(x):
    print(x)
    return 1

print('Final output:', a(10))
    

