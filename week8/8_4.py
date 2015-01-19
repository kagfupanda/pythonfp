#8_4.py
#Author Siddharth Srinivasan

def main():
    mynum = int(input('Enter a number to calculate Syracuse sequence: '))
    print ('The Syracuse sequence for',mynum, ' is: ', mynum, end="")
    newNum = mynum
    while (newNum>1):
        if (newNum%2 == 0):
            newNum = int(newNum/2)
            print(',',newNum, end="")
        else:
            newNum = 3*newNum + 1
            print(',',newNum, end="")
    print("\n")

main()
