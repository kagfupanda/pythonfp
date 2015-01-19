#8_6.py
#Author Siddharth Srinivasan
import math
 
def main():
    try:              
        while True:                
            max = eval(input("Enter a number to display the prime numbers before it: "))
            if max > 0 and type(max) == int:
                     break
            print("Ther is no prime number less than", max)
         
        if max == 1:               
            print("There is no prime number less than 1.")
        else:                                  
            num = 2                  
            ans = [2]
            while num <= max:               
                numsqrt= int(math.sqrt(num))  
                n = 2
                while n <= numsqrt:        
                    if num%n == 0:
                        break              
                    else:
                        n = n+1       
                if num%n != 0:           
                    ans.append(num)        
                num = num+1                  
            print("The Prime Numbers up to",max,"are: ")
            print(ans)
    except:
        print("Something went wrong")
    

main()
