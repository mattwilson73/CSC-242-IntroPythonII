# Prints instructions on moving n disks from source post to dest post using
# temp resting post

def moveTower(n, source, dest, temp):
    #print(n,source,dest,temp)
    if n==1:
        print("Move disk from", source, "to", dest)
    else:
        moveTower(n-1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n-1, temp, dest, source)

def hanoi(n):
    moveTower(n,1,3,2)
