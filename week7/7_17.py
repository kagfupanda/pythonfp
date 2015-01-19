#7_17.py
#Author Siddharth Srinivasan

from graphics import *
from time import sleep
MAX_X = 30
MAX_Y = 24 
MIN_X = 0
MIN_Y = 0

def main():
    win = GraphWin("My Chapter 7/17: Animation",500,350)
    win.setCoords(MIN_X,MIN_Y,MAX_X,MAX_Y)
    BallCenter = Point(MAX_X/2,MAX_Y/2)
    radius = 2
    dx,dy = 1,1
    speed = 0.05
    XborderMax = MAX_X-radius
    XborderMin = MIN_X+radius
    YborderMax = MAX_Y-radius
    YborderMin = MIN_Y+radius
    ball = Circle(BallCenter,radius)
    ball.setFill("green")
    ball.setOutline("blue")
    ball.draw(win)
    start = Text(BallCenter,"Click anywhere to Start!")
    start.setSize(36)
    start.draw(win)
    win.getMouse()
    start.undraw()
    for i in range(10000):
        now = ball.getCenter()
        if now.getX() >= XborderMax:
            dx = -1
        if now.getX() <= XborderMin:
            dx = 1
        if now.getY() >= YborderMax:
            dy = -1
        if now.getY() <= YborderMin:
            dy = 1
        ball.move(dx,dy)
        sleep(speed)
    win.close()

main() 
