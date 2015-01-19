#sum.py
#Author Siddharth Srinivasan
def sumN(n):
    z = 0
    for i in range(1, (n + 1)):
        z = z + i
    return z
9
def sumNCubes(n):
         p = 0
         for i in range(1, (n+1)):
                  p = p + (i**3)
         return p
a = sumN(5)
print(a)
b = sumNCubes(5)
print(b)

