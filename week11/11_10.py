#11_10.py
#Author Siddharth Srinivasan
def factorial(n):
    nshriek = 1       # n factorial is sometimes called 
    while n > 1:      # 'n shriek' because of the 'n!' notation
        nshriek *= n
        n -= 1
    return nshriek
