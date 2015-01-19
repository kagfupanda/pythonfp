#7_12.py
#Author Siddharth Srinivasan
from dateutil.parser import *

def main():
    for i in range(1,2):
        date = input('Enter a date in the form of month/day/year?\n')
        try:
            parse(date)
            print('Date is:',  date)
        except :    
            print('Wrong date',date)

main()
