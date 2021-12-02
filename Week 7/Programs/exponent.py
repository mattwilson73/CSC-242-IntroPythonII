i = 0

def iterExponent(a, n):
    product = 1
    for num in range(n):
        product *= a
    return product

def exponent (a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    temp = exponent (a, n//2)
    global i
    if n % 2 == 0:
        i=i+1
        return temp * temp
    else:
        i=i+2
        return temp * temp * a

def main():
    a = int(input("Enter a: "))
    n = int(input("Enter n: "))

    global i
    i=0
    print(exponent (a, n))
    print(i, "multiplications were done.")

main()
