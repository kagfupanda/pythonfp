#9_15.py
#Author Siddharth Srinivasan
from random import random
import math
def main():
    n,s = getInput()
    r = getWallAngle(s)
    x = seeingNtimes(n,r)
    printSummary(n,x)
    print()
 

def getInput():
    n = eval(input("How many times to simulate random seeing:"))
    s = eval(input("How large this diameter of this cube:"))
    return n,s
 
def getWallAngle(s):
    a = s/4
    o = s/2
    c = o/a
    r = math.atan(c)
    r = r*2
    return r
def seeingNtimes(n,r):
    times = 0
    for i in range(n):
        seeing = "no"
        h = random()*6.28
        v = random()*3.14
        if h < r:
            if v < r:
                times = times+1
     
    return times
 
 
def printSummary(n,x):
    print("\nFor {} random seeing.\nIt has seen a wall {} times which is {:.2%}".format(n,x,x/n))
main()
