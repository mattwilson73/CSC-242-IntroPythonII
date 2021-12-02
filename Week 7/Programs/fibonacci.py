def fibonacci(n):
    x, y = 1, 1
    i = 1
    while i < n:
        x, y = y, x+y
        i = i+1
    return y


