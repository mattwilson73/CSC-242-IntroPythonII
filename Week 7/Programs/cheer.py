def cheer(n):
    if n <= 1:
        print ("Hurrah")
    else:
        print("Hip")
        cheer(n-1)
