#futval2.py
#This program Calculates the interest per year
#Author Siddharth Srinivasan

def main():
    print("This program calculates the future value")
    print("of an investment.")
    principal = eval(input("Enter the amount invested each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for the investment: "))
    print("Year".ljust(10) + "Value".rjust(5))
    print("-" * 17)
    for i in range(years):
        tempval = principal
        principal = principal * (1 + apr)
        currentval = years * i + principal
        print(str(years).ljust(10) + str(currentval).rjust(5))

main()

