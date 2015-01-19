#8_12.py
#Author Siddharth Srinivasan
#Create a .txt file for this exercise
#Ex.
#13
#242
#80
def main():
    filename = input("Please enter a file name: ")
    infile = open(filename, 'r')
    temp = infile.readline()
    hdd, cdd, hot, cool = 0, 0, 0, 0
    date = 1
    try:
        while temp != '':
            if temp == '':
                break
            temp = int(temp)
            if temp > 80:
                cdd = (temp-80)+cdd
            if temp < 60:
                hdd = (60-temp)+hdd
            date = date+1
            temp = infile.readline()
        print("In {} days, there\"r total of {} Hot Degree Days and {} Cool Degree Days.".format(date-1,hdd,cdd))
         
    except:
        print("Something went wrong")

main()
