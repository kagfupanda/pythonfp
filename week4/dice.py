#dice.py
#program draws 5 dice
#Author Siddharth Srinivasan
from graphics import*
win = GraphWin()
win.setCoords(0,300,200,0)
def dice1():
    ux = 10
    uy = 10
    lx = 70
    ly = 70
    dice1 = Rectangle(Point(ux,uy), Point(lx,ly))
    dice1number = Point((ux + lx) /2, (uy + ly) / 2)
    dice1.draw(win)
    dice1number.draw(win)
    
dice1()

def dice2():
    ux = 90
    uy = 10
    lx = 150
    ly = 70
    dice2 = Rectangle(Point(ux,uy), Point(lx,ly))
    dice2number1 = Point((2*ux + lx)/3, (uy + ly)/2)
    dice2number2 = Point((ux + 2 *lx)/3, (uy + ly)/2)
    dice2number2.draw(win)
    dice2number1.draw(win)
    dice2.draw(win)

dice2()

def dice3():
    ux = 10
    uy = 90
    lx = 70
    ly = 150
    mpy1 = (uy + ly)/2 
    dice3 = Rectangle(Point(ux,uy), Point(lx,ly))
    dice3number2 = Point((ux + lx)/2, (uy + ly)/2)
    dice3number1 = Point((ux + lx)/2, (mpy1 + uy)/2)
    dice3number3 = Point((ux + lx)/2, (mpy1 + ly)/2)
    dice3number2.draw(win)
    dice3number1.draw(win)
    dice3number3.draw(win)
    dice3.draw(win)

dice3()

def dice4():
    ux = 90
    uy = 90
    lx = 150
    ly = 150
    dice4 = Rectangle(Point(ux,uy), Point(lx,ly))
    dice4number1 = Point((2*ux + lx)/3, (2 * uy + ly)/3)
    dice4number2 = Point((ux + 2 * lx)/3, (2 * uy + ly)/3)
    dice4number3 = Point((2*ux + lx)/3, (uy + 2 * ly)/3)
    dice4number4 = Point((ux + 2 * lx)/3, (uy + 2 * ly)/3)
    dice4.draw(win)
    dice4number1.draw(win)
    dice4number3.draw(win)
    dice4number2.draw(win)
    dice4number4.draw(win)

dice4()

def dice5():
    ux = 10
    uy = 170
    lx = 70
    ly = 230
    dice5 = Rectangle(Point(ux,uy), Point(lx,ly))
    dice5number1 = Point((2 * ux + lx) / 3, (2 * uy + ly) / 3)
    dice5number2 = Point((ux + 2 * lx)/3, (2 * uy + ly)/3)
    dice5number3 = Point((ux + lx)/2, (uy + ly)/2)
    dice5number4 = Point((2*ux + lx)/3, (uy + 2 * ly)/3)
    dice5number5 = Point((ux + 2 * lx)/3, (uy + 2 * ly)/3)
    dice5.draw(win)
    dice5number1.draw(win)
    dice5number2.draw(win)
    dice5number3.draw(win)
    dice5number4.draw(win)
    dice5number5.draw(win)

dice5()
