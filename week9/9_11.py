#9_11.py
#Author Siddharth Srinivasan
from random import randrange
def main():
    times = getInput()
    foak = rollNtimes(times)
    printSummary(foak,times)
 

def getInput():     
    times = eval(input("How many times you want to roll the dices: "))
    return times
 
def rollNtimes(times):
    foak = 0
    for i in range(times):
        result = rollOneTime()    
      
        foak = diceCheck(result,foak)
    return foak
 
 

def rollOneTime():
    result = "no"
    i = 0
    x = diceRandom()
    while diceRandom() == x:
        i = i+1
     
    if i == 4:
        result = "yes"
    return result
 

def diceCheck(result,foak):
     
    if result == "yes":
        foak = foak+1
    return foak
 
def diceRandom():   
    x = randrange(1,7)
    return x
 
 
def printSummary(foak,times):
    print("\nFor {} times we get FOAK {} times which is {:0.2%}".format(times,foak,foak/times))

main()
