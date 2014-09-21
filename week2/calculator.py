#calculator.py
#program to calculate the expressions that are inputed
#Author Siddharth Srinivasan

def main():
    print("This program will calculate the expression you input")
    for i in range(100):
        x = input("Enter an expression you want evaluated: ")
        eval(str(x))
        print(x)

main()
