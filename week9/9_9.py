#9_9.py
#Author Siddharth Srinivasan
from random import randrange
 
def main():
    n = getInput()
    bustProb,totalCardDraw = blackJack(n)
    printSummary(bustProb,totalCardDraw,n)
     
     
def getInput():
    n = eval(input('How many games to simulate [suggest 1000+]:'))   
    return n
     
     
 
def blackJack(rounds):
    bustProb = [0]*10
    totalCardDraw = [0]*10
     
    for i in range(rounds):
     
        card,hand,hasAce,lucky = getStart()
        if lucky == '':
             
            while hand < 17:
                hand,hasAce = playHit(hand,hasAce)

        stat(card,hand,bustProb,totalCardDraw)
       
    return bustProb,totalCardDraw
 
 
 
def stat(card,hand,bustProb,totalCardDraw):
    card = card-2
     
    if hand > 21:
        bustProb[card] = bustProb[card]+1
     
    totalCardDraw[card] = totalCardDraw[card]+1
     
def getStart():
     
    hand = 0
    lucky = ''
    hasAce = 0
  
    c1,hasAce = hit(hasAce)
    c2,hasAce = hit(hasAce)
     
    hand = c1+c2                             
                                             
    lucky = isJack(hand)
     
    return c1, hand, hasAce, lucky
     
     
 
def hit(hasAce):
     
    c = randrange(1,11)
     
    if c == 1 and hasAce == 0:
        hasAce = 1
        return c+10, hasAce
 
    return c, hasAce
 
 
 
def isJack(hand):
     
    lucky = ''
 
    if hand == 21 : lucky = 'yes'
    else: lucky = ''
 
    return lucky
 
 
 
def playHit(hand,hasAce):
     
    c,hasAce = hit(hasAce)
    hand = hand + c
     
    if hasAce==1 and hand > 21:
        hand = hand - 10     
        hasAce = ''
     
    return hand,hasAce
 
 
 
def printSummary(a,b,n):
    print('\n===============================')
    print('Games simulated:',n)
    print()
     
    for i in range(10):
         
        #turn report from Card 11 to Ace card
        if i == 9:
            print('Ace card has {0:0.1%} bust probability'.format(a[i]/b[i]))
         
        else:
            print('Card#{0} has {1:0.1%} bust probability'.format(i+2,a[i]/b[i]))

main()
