#8_10.py
#Author Siddharth Srinivasan
def main():
         filename = input("Enter file name: ")
         infile = open(filename, 'r')
         result = infile.readline()
         prevOd = result
         prevOdometer = int(prevOd)
         totmiles = 0
         totgallons = 0
         result = infile.readline()
         while result != ' ':
                  curOd, curGal = result.split()
                  curOdometer = int(curOd)
                  gallons = int(curGal)
                  miles = curOdometer - prevOdometer
                  totmiles = totmiles + miles
                  totgallons = totgallons + gallons
                  print("Your MPG for this leg is", miles/gallons)
                  result = infile.readline()
                  print("hello", result)
                  prevOdometer = curOdometer
         print("Your total MPG so far is", totmiles/totgallons)


main()
                  
                  
                  
