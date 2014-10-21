#sum.py
#Author Siddharth Srinivasan
def sumN(n):
    z = 0
    for i in range(3):
        z = z + (n + (n - 1))
        n = n - 2
    print(z)
sumN(5)
