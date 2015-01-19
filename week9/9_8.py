#9_8.py
#Author Siddharth Srinivasan
from random import randrange
 
def main():
    n = getInput()
    win, lost, draw, bust = blackJack(n)
    printSummary(win, lost, draw, bust, n)     
     
def getInput():
    n = eval(input("\nHow many games to simulate: "))   
    return n
 
def blackJack(rounds):
    win = lose = draw = busted = 0
    for i in range(rounds):        
        status,pHand,pLucky = playerHand()
        if pHand <= 21:
            status = dealerHand(pHand,pLucky)
        win,lose,draw,busted = stat(status,win,lose,draw,busted)
    return win,lose,draw,busted
 
def playerHand():
    status = ""
    pHand = 0

    pHand, hasAce, pLucky = getStart()
 
    while pHand < 17:
        pHand,hasAce = playHit(pHand,hasAce)

    if pHand >21: status = "dealer"            
    return status, pHand, pLucky
  
def dealerHand(pHand,pLucky):
    dHand = 0
    status = ""
     
    dHand, hasAce, dLucky = getStart()
    status = vsJack(pLucky,dLucky)
 
    if status=="":
        if pHand == 21:
            while dHand < pHand:
                 
                dHand,hasAce = playHit(dHand,hasAce)
        else:
            while dHand <= pHand:
                 
                dHand,hasAce = playHit(dHand,hasAce)
        status = endGame(pHand,dHand)
         
    return status

def getStart():
    hand = 0
    lucky = ""
    hasAce = 0
    c1,hasAce = hit(hasAce)
    c2,hasAce = hit(hasAce)
    hand = c1+c2                             
    lucky = isJack(hand)
    return hand, hasAce, lucky

def hit(hasAce):
    c = randrange(1,11)
    if c == 1 and hasAce == 0:
 
        hasAce = 1
        return c+10, hasAce
 
    return c, hasAce
     

def isJack(hand):
    lucky = ""
 
    if hand == 21 : lucky = "yes"
    return lucky
 
def vsJack(pLucky,dLucky):
     
    
    status = ""
     
 
    if  dLucky == "yes" and pLucky == "yes": status = "draw"
     
    
    elif pLucky == "yes": status = "player"   
    elif dLucky == "yes": status = "dealer"
     
    return status
 
 
 

def playHit(hand,hasAce):
     
    c,hasAce = hit(hasAce)
    hand = hand + c
     

    if hasAce==1 and hand > 21:
        hand = hand - 10
         
              
        hasAce = ""
     
    return hand,hasAce

def endGame(pHand,dHand):
     

    if dHand == pHand: status = "draw" 
    elif dHand > pHand and dHand <= 21 : status = "dealer"
    elif dHand > 21 : status = "busted"
     
    return status

def stat(status,win,lose,draw,busted):
     
    if status == "dealer" :
         win = win+1
    elif status == "player" :
         lose = lose+1
    elif status == "draw" :
         draw = draw+1
    elif status == "busted" :
         busted = busted+1
     
    return win,lose,draw,busted
 
 
def printSummary(a,b,c,d,n):
    print("\n===============================")
    print("Games simulated:",n)
    print("\nDealer wins {0} games ({1:0.1%})".format(a, a/n))
    print("Dealer lose to BlackJack hand {0} games({1:0.1%})".format(b, b/n))
    print("Dealer busted {0} games({1:0.1%})".format(d, d/n))
    print("Games draw {0} times ({1:0.1%})".format(c, c/n))


main()
     
