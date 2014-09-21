#futval3.py
#a program to compute the value of an investment carried how ever many years you input ino the future
#Author Siddharth Srinivasan

def main():
    print("This program calculates the future value")
    print("of how ever many years you invest")
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate: ")
    years = input("Enter how many years you would like to invest: ")
    periods = input("Enter how many times interest is compounded each year: ")
    interest = 0
    for i in range(years*periods):
          interest = interest + apr*principal/(periods*100)

    print("The value in ", years, " years on a principal of", principal," is: ", interest)
                                                

main()

