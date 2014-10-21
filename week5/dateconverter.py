#dateconverter.py
#converts dates
#Author Siddharth Srinivasan
def main():
    day, month, year, = eval(input("Enter day, month, and year numbers: "))
    date1 = str(month) + "/" + str(day) + "/" + str(year)
    months = ["january", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthStr = months[month - 1]
    date2 = monthStr + " " + str(day) + ", " + str(year)
    print("The date is", date1.center(50), "or", date2.center(50) + ".")


main()
