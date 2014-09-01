#futval.py
#a program to compute the value of an investment carried how ever many years you input ino the future

def main():
    print("This program calculates the future value")
    print("of how ever many years you invest")
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate: ")
    years = input("Enter how many years you would like to invest: ")
    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in the", years, "years is:", principal)
    

main()
