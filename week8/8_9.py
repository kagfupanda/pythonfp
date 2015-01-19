#8_9.py
#Author Siddharth Srinivasan
def main():
         prevOd = input("Enter the starting odometer reading: ")
         prevOdometer = int(prevOd)
         totmiles = 0
         totgallons = 0
         v = input("Enter the current odometer reading and amount of gas used: (use a space to split) ")
         while v != "":
                  curOd, curGal = v.split()
                  curOdometer = int(curOd)
                  gallons = int(curGal)
                  miles = curOdometer - prevOdometer
                  totmiles = totmiles + miles
                  totgallons = totgallons + gallons
                  print("Your MPG for this leg is", miles/gallons)
                  v = input("Enter the current odometer reading and amount of gas used: ")
                  prevOdometer = curOdometer
         print("Your total MPG so far is", totmiles/totgallons)


main()
                  
                  
                  
