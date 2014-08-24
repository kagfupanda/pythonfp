#File: chaos5.py
#Author: Siddharth Srinivasan 95016469
#homework 1 exercise 5
# A simple program illustrating chaotic behavior
def main():
    print("This program illustrates a chaotic function")
    x = eval(raw_input("Enter a number between 0 and 1: "))
    n = eval(raw_input("How many numbers should I print? "))
    for i in range(n): #loop n times
        x = 2.0 * x * (1-x)
        print(x)

main()



