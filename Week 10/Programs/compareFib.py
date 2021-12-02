# Implementations of fibonacci

import random, time

def iterFib(n):
    x, y = 1, 1
    i = 1
    while i < n:
        x, y = y, x+y
        i = i+1
    return y

def recFib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recFib(n-1) + recFib(n-2)

def timing(fcn, n):
    '''RETURNS the time it takes to run fcn on a problem n'''
    t1 = time.time()
    fcn(n)
    t2 = time.time()
    return t2 - t1

# Write this so that it runs fcn on problems of
# size start, start + inc, start + 2 * inc, ..., stop
# with trials number of trials, printing the average for
# each problem size
def timingCurve(fcn, start, inc, stop, trials):
    pass
