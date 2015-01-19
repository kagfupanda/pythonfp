#6_7.py
#Calculates nth fibonacci number
#Author Siddharth Srinivasan
position = eval(input("Enter the position of the number: "))
def fib(n):
    old = 0
    cur = 1
    i = 1
    yield cur
    while (i < n):
        cur, old, i = cur+old, cur, i+1
        yield cur

for f in fib(2):
    print(f)
