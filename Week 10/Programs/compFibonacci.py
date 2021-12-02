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

def timingCurve(fcn, start, inc, stop, trials):
    '''RETURNS a list representing the average time required to sort
         lists of sizes start, start+inc, start+2*inc, ..., stop.'''
    times = []
    for n in range(start, stop, inc):
        total = 0.0
        for i in range(trials):
            total += timing(fcn, n)
        avg = total / trials
        times.append(avg)
        print("Run time of the function on a problem of size {} was {:.10f}".format(n, avg))
    return times
