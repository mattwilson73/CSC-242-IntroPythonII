from random import randint

def game(n):
    'a program to teach simple arithmetic'
    count = 0
    for i in range(n):
        x, y = randint(0,9), randint(0,9)
        while True:
            try:
                print(x, ' + ', y, ' = ')
                #ans = eval(input("Enter answer: " ))
                ans = float(input("Enter answer: " ))
                break
            except (ValueError):
                print("Please enter your answer using digits (0-9).")
        if ans == x+y:
            print("Correct")
            count += 1
        else:
            print("Incorrect")
    print("You got {} correct answers out of {}.".format(count, n))
