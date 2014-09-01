#File: chaos6a.py
#Author: Siddharth Srinivasan 95016469
#homework 1 exercise 6a
# A simple program illustrating chaotic behavior
def main():
    print("This program is for 6a")
    x = eval(raw_input("Enter a number between 0 and 1: "))
    for i in range(100): #loop 100 times
        x = 3.9 * x * (1 - x)
        print(x)

main()



