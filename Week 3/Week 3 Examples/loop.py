def loopf():
    'A loop that forces the user to enter an integer'
    while True:
        try:
            num = int(input("Please enter a whole number: "))
            break
        except:
            print("Oops!  That was not a valid number.  Try again ...")
    return num
