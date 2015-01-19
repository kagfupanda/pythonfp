#5_6.py
#Finds the numeric value of your name
#Author Siddharth Srinivasan
def main():
    name = input("Enter your name: ")
     
    name = name.replace(' ','')
    newname = name.lower()

    finalamount = 0
    for i in newname:
        finalamount = finalamount + ord(i)-96
    
    print("Numeric value of your name is", finalamount)
main()
