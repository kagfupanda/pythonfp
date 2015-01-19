#8_7.py
#Author Siddharth Srinivasan

import math
 
def primeCheck(pPossible):
    mycondition = 2
    half = math.sqrt(pPossible)
    pCheck = 1
    while mycondition <= half:
        if pPossible%mycondition == 0:
            pCheck = 0
            break
        else:
            mycondition = mycondition+1
    if pPossible%mycondition != 0:
        pCheck = 1
    return pCheck

def ListofPrimes(max):
    pPossible = 2
    pList = []
    while pPossible < max:                
        pCheck = primeCheck(pPossible)
        if pCheck == 1:
            print('Found a prime ',pPossible)
            pList.append(pPossible)
        pPossible = pPossible+1
    return pList    

def main():
    try:
        while True:
            num = eval(input('Please provide positive even number greater than 2:'))
            if num%2 == 0 and num > 2:
              break
            print('That\'s not correct. Try again!')
             
        pList = ListofPrimes(num)
        for i in pList:
            remain = num - i
            pCheck = primeCheck(remain)
            if pCheck == 1:
              break         
        print('The numbers are ',i,' and ' , remain)
     
    except:
        print('Something went wrong')

main()
