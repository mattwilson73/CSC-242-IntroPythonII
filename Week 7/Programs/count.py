def countdown(n):
    'count from n down to 1'
    if n <= 0:
        print('Blast off!')
    else:
        print(n)
        countdown(n-1)
