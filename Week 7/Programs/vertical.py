def vertical(n):           #1
    'print the digits of n from most significant to least, one per line'
    print("Entering vertical({})".format(n)) #2
    if n < 10:             #3
        print(n)           #4
        print("Leaving vertical({})".format(n)) #5
    else:                  #6
        vertical(n // 10)  #7
        print(n % 10)      #8
        print("Leaving vertical({})".format(n)) #9




vertical(1234)