#9_7.py
#Author Siddharth Srinivasan
from random import randrange
 
def main():
    n = getInput()
    x = crapsCasino(n)
    printSummary(x,n)

  
def getInput():
    n = eval(input("How many games to simulate: "))
    return n

def crapsCasino(rounds):        
    win = 0
    for i in range(rounds):
        init = firstRoll()
         
        if init == "win": win = win+1
        elif (type(init)) == int:
             
            final = pointRoll(init)
                 
            if final == "win": win = win+1            
    return win 
     
def firstRoll():
     
    x = dice()
    if x == 7 or x == 11:
        status = "win"
         
    elif x ==2 or x ==3 or x ==12:
        status = "lose"
         
    else:
        status = x
    return status
 
 

def pointRoll(point):
    x = 0
    while not pointCheck(x,point):         
        x = dice()
        if x == point:
            status = "win"
        elif x == 7:
            status = "lose"
     
    return status
     
 

def pointCheck(x,point):
    return x == 7 or x == point
 
def dice():
    return randrange(1,7)+randrange(1,7)
 
def printSummary(win,rounds):
    print("==========================================")
    print("Games simulated:",rounds)
    print("Total winning:",win)
     
    print("\nProbability of winning Craps is: {:0.2}".format(win/rounds))

main()
 
