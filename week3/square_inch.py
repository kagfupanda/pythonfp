#square_inch.py
#program that computes square inch
#author Siddharth Srinivasan
import math
def main():
    diameter = input("Enter your diameter for your pizza: ")
    price = input("Enter your price for your pizza: ")
    A = math.pi * (diameter/2) **2
    finalPrice = A * price
    print("your final price is", finalPrice)

main()
