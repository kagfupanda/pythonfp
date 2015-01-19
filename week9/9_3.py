#9_3.py
#Author Siddharth Srinivasan
from random import random
def main():
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
 
def getInputs():
    a = eval(input("What is the probability team A wins a serve: "))
    b = eval(input("What is the probability team B wins a serve: "))
    c = eval(input("How many games: "))
    return a,b,c
 
def simNGames(n,probA,probB):
    winsA = winsB = 0
     
    for i in range(n):
        if i%2 == 0: serving = "A"
        else:
                 serving = "B"
                 scoreA, scoreB = simOneGame(probA,probB,serving) 
                 if scoreA > scoreB:
                     winsA = winsA + 1
                 else:
                     winsB = winsB + 1
             
    return winsA, winsB
 
 
def simOneGame(probA,probB,serving):
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA,scoreB):
        if serving =="A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
         
    return scoreA, scoreB
         
def gameOver(a,b):
    return ((a >= 15) and (a-b >= 2)) or ((b >= 15) and (b-a >= 2))
 
def printSummary(winsA,winsB):
    n = winsA + winsB
    print("Games simulated:",n)
    print("Wins for team A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for team B: {0} ({1:0.1%})".format(winsB, winsB/n))


main()
