#8_5.py
#Author Siddharth Srinivasan
import math
def main():
         try:
                  while True:
                           num = eval(input("Enter a number: "))
                           if num > 0 and type(num) == int:
                                    break
                           print("Enter a valid number")
                  if num == 1:
                           print("Your number is neither prime or composite")
                  elif num == 2:
                            print("Your number is prime")
                  else:    
                           numsqrt = int(math.sqrt(num))
                           n = 2
                           while n <= numsqrt and num % n != 0:
                                    n = n + 1
                           if num % n == 0:
                                    print(num, "is not a prime number")
                           else:
                                    print(num, "is a prime number")
         except:
                  print("something went wrong")
                  
         
         
                    
         
main()
