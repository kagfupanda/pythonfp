#8_11.py
#Author Siddharth Srinivasan
def main():
    print("Enter daily average temperature below. Leave empty when finish.\n")    
    hdd, cdd, hot, cool = 0, 0, 0, 0
    date = 1
    try:
        temp = input("Day#{} :".format(date))
        while temp != "":
            temp = int(temp)
            if temp > 80:
                cdd = (temp-80)+cdd
            if temp < 60:
                hdd = (60-temp)+hdd
            date = date+1
            temp = input("Day#{} :".format(date))   
        print("In {} days, there\"r total of {} Hot Degree Days and {} Cool Degree Days.".format(date-1,hdd,cdd))
    except:
        print("Unknow error.")

main()
