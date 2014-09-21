#futval2.py
#This program Calculates the interest per year
#Author Siddharth Srinivasan

def main():
    print("This program calculates the future value")
    print("of an investment.")
    principal = input("Enter the amount invested each year: ")
    apr = input("Enter the annual interest rate: ")
    years = input("Enter the number of years for the investment: ")
    for i in range(years):
        tempval = principal
        principal = principal * (1 + apr)
        currentval = years * i + principal
    print("The value in", years, "years is: ", currentval)


main()
