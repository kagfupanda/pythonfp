#File: chaos4.py
# A simple program illustrating chaotic behavior
#Author: Siddharth Srinivasan 95016469
#chapter 1 problem 3
def main():
    print("This program illustrates a chaotic function")
    #use raw_input() in python2 instead of input() in python3
    x = eval(raw_input("Enter a number between 0 and 1: "))
    for i in range(20):   #loop 20 times
        x = 2.0 * x * (1 - x)
        print(x)

main()



