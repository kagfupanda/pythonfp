#9_5.py
#Author Siddharth Srinivasan
from random import random
def main():
    probA, probB = getInputs()
    games = 1000
    winsAreg, winsBreg, winsAral, winsBral = simNGames(probA, probB, games)
    comment = getComment(winsAreg, winsBreg, winsAral,
                          winsBral, probA, probB, games)
    printSummary(winsAreg, winsBreg, winsAral, winsBral,
                 games, comment)
 
def getInputs():
    while True:
        a = eval(input("What is the probability team A wins a serve? "))
        b = eval(input("What is the probility team B wins a serve? "))
        if a == b:
                 print("Something went wrong")
        else:
                 break      
 
    return a,b
         
 
def simNGames(probA,probB,games):
    winsAreg = winsBreg = 0 
    winsAral = winsBral = 0 
     
    for i in range(games):
        if i%2 == 0: serving = "A"
        else: serving = "B"
        scoreA, scoreB = simOneGame(probA,probB,serving,"regular")
         
        if scoreA > scoreB:
            winsAreg = winsAreg + 1
        else:
            winsBreg = winsBreg + 1
             
        scoreA, scoreB = simOneGame(probA,probB,serving,"rally")
         
        if scoreA > scoreB:
            winsAral = winsAral + 1
        else:
            winsBral = winsBral + 1
             
    return winsAreg, winsBreg, winsAral, winsBral, 
 
 
def simOneGame(probA,probB,serving,type):
    scoreA = scoreB = 0
     
    if type == "regular":
         
        while not gameOver(scoreA,scoreB,type):
             
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

    if type == "rally":
           
        while not gameOver(scoreA,scoreB,type):
     
            if serving =="A":
                if  random() < probA:
                    scoreA = scoreA + 1
                else:
                    scoreB = scoreB + 1
                    serving = "B"
            else:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    scoreA = scoreA + 1
                    serving = "A"
     
    return scoreA, scoreB
 
 
def gameOver(a,b,type):
     
    if type == "regular":
        status = ((a >= 15) and (a-b >= 2)) or ((b >= 15) and (b-a >= 2))
     
    if type == "rally":
        
        status = ((a >= 25) and (a-b >= 2)) or ((b >= 25) and (b-a >= 2))
     
    return status
 
 
def getComment(winsAreg, winsBreg, winsAral, winsBral, probA, probB, games):
    if probA == max(probA,probB):
        betterteam = "A"
        diff = (winsAral-winsAreg)/games
    else: 
        betterteam = "B"
        diff = (winsBral-winsBreg)/games
                 
    return Comment(betterteam,diff)
 
 
def Comment(betterteam,diff):
     
    if diff > 0:
        c =":\nTeam {0} is better team and enjoy benefit {1:0.1%} from rally scoring system.".format(betterteam,diff)
     
    elif diff < 0:
        c =":\nEven Team {0} is a better but their advantage is reduce {1:0.1%} by rally scoring system.".format(betterteam,diff)
 
    else:
        c ="\nTeam {0} is better but does not gain benefit from rally scoring system.".format(betterteam)
         
    return c
 
 
def printSummary(winsAreg,winsBreg,winsAral,winsBral,games,comment):
 
    print("Games simulated:",games)
     
    print("Regular type games result:")
    print("Wins for A: {0} ({1:0.1%})".format(winsAreg, winsAreg/games))
    print("Wins for B: {0} ({1:0.1%})".format(winsBreg, winsBreg/games))
     
    print("Rally Scoring type games result:")
    print("Wins for A: {0} ({1:0.1%})".format(winsAral, winsAral/games))
    print("Wins for B: {0} ({1:0.1%})".format(winsBral, winsBral/games))
     
    print("\n====================================================")
    print(comment)



main()
