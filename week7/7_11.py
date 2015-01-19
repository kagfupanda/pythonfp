#7_11.py
#Author Siddharth Srinivasan
def main():
    try:
        year = eval(input("Enter the year"))
        if year % 4== 0 and year % 400==0:
            print("It is a leap year")
        elif year % 100==0:
            print("It's not a leap year")
        elif year % 4==0:
            print("It is a leap year")
        else:
            print("It's not a leap year")
    except:
        print("Something went wrong")
        
        
main()

