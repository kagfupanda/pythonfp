#9_12.py
#Author Siddharth Srinivasan
from random import random
 
def main():
    n = getInput()
    position = randomWalk(n)
    printSummary(n,position)
 
def getInput():
    n = eval(input("How many steps to be take: "))   
    return n
 
def randomWalk(n):   
    pos = 0
    for i in range(n):
        walk = direction()
        pos = move(pos,walk)
    return pos

def direction():
    if random() > 0.5:
        walk = 1
    else:
        walk = -1
    return walk

def move(pos,walk):
    pos = pos + walk
    return pos
 
def printSummary(n,position):
    if position > 0:
        direction = "forward"
    else:
        direction = "backward"
    print("\nRandom walk total {} steps make you move {} {} steps.".format(n,direction,abs(position)))


main()
