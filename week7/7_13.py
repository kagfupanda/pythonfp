#7_13.py
#Author Siddharth Srinivasan
from dateutil.parser import *

def main():
    for i in range(1,2):
        date = input('Enter a date in the form of month/day/year to find its number?\n')
        try:
            parse(date)
            smonth,sday,syear = date.split('/')
            month = int(smonth)
            day = int(sday)
            year = int(syear)
            add = 0
            sub = 0
            if (month >= 3):
                sub = (4*month + 23)//10
            if ((year%4) == 0 and (month >=3 or (month ==2 and day >=29))):
                add = 1
            dayNum = 31 * (month - 1) + day + add - sub
            print('Input Date is valid, ', date)
        except :    
            print('Wrong date: ',date)

main()
