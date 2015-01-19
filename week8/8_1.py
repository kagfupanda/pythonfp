#8_1.py
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

for f in fib(position):
    print(f)
