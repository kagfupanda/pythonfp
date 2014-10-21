#Rectangle.py
#Program allows user to draw a rectangle
#Author Siddharth Srinivasan
import graphics
from graphics import *
def main():
    win = GraphWin("Draw a rectangle", 400,400)
    per = Text(Point(50,300), "Perimeter:"); per.draw(win)
    area = Text(Point(250,300), "Area:"); area.draw(win)
    finalPer = Text(Point(100,300), "");finalPer.draw(win)
    finalarea = Text(Point(300,300), "");finalarea.draw(win)
    fp = win.getMouse()
    x = fp.getX()
    y = fp.getY()
    sp = win.getMouse()
    a = sp.getX()
    b = sp.getY()
    rect = Rectangle(Point(x,y), Point(a,b))
    rect.draw(win)
    length = abs(a-x)
    height = abs(y-b)
    perimeter = 2 * (length + height)
    area = length * height
    finalPer.setText(perimeter)
    finalarea.setText(area)
    win.getMouse()
    win.close()
    
    
    
main()
