#9_13.py
#Author Siddharth Srinivasan
from random import random
def main():
    n = getInput()
    y,x = randomWalk(n)
    printSummary(n,y,x)

def getInput():
    n = eval(input("\nHow many steps to be take: "))   
    return n
 
def randomWalk(n):
    y=x=0
     
    for i in range(n):
        v,h = direction()
         
        y,x = move(y,x,v,h)
 
    return y,x
 
def direction():
    v=h=0
    z = random()
    if z < 0.25:
        v = 1
    elif z < 0.5:
        v = -1
    elif z < 0.75:
        h = 1
    else:
        h = -1
    return v,h
 
def move(y,x,v,h):
    y = y+v
    x = x+h
     
    return y,x
def printSummary(n,y,x):
    vertical,horizon = wordingAxis(y,x)
    if vertical == 0 and horizon == 0:
        print("\nFor all {} steps You stay at the starting point!".format(n))

    elif vertical == 0:
        print("\nFor all {} steps You move to the {} {} blocks.".format(n,horizon,abs(x)))

    elif horizon ==0:
        print("\nFor all {} steps You move {} {} blocks.".format(n,vertical,abs(y)))
     
    else:
        print("\nFor all {} steps You move {} {} blocks and to the {} {} blocks.".format(n,vertical,abs(y),horizon,abs(x)))
 
def wordingAxis(y,x):
    vertical = horizon = 0
    if y > 0:
         vertical = "forward"
    elif y < 0:
        vertical = "backward"
         
    if x > 0:
        horizon = "right"
    elif x < 0:
        horizon = "left"
    return vertical,horizon

main()
