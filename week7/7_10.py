#7_10.py
#Author Siddharth Srinivasan

MAX_YEAR = 2099
MIN_YEAR = 1900
def main():
    for i in range(1,2):
        name = input('Enter a year?\n')
        year = int(name)
        if (year <= MAX_YEAR and year >= MIN_YEAR):
            a = year%19
            b = year%4
            c = year%7
            d = (19*a + 24)%30
            e = (2*b + 4*c + 6*d +5)%7
            easter_date = 22 + d + e
            if (year == 1954 or year == 1981 or year == 2049 or year == 2076):
                easter_date = easter_date - 7
            if (easter_date > 31):
                print('Easter date for year,',name,' is: April ', easter_date - 9 - 22)
            else:
                print('Easter date for year, ',name,' is: March ', easter_date)
        else:
            print('Out of range year, ',name,'.')

main()
