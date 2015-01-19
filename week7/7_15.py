#7_15
#Author Siddharth

import math
from graphics import *
 
def main():
    win = GraphWin('Line Segment Information',300,420)
    win.setCoords(-10, -14, 10, 14)
    win.setBackground('grey')
     
    FirstBox = Rectangle(Point(-10,14),Point(10,10))
    FirstBox.setFill(color_rgb(157,154,145))
    FirstBox.setWidth(0)
    FirstBox.draw(win)
     
    FinalBox = Rectangle(Point(-10,-10),Point(10,-14))
    FinalBox.setFill(color_rgb(157,154,145))
    FinalBox.setWidth(0)
    FinalBox.draw(win)
     
    for i in range(1,20): 
        myLayout = Line(Point(i-10,-10),Point(i-10,10))
        myLayout.setFill('grey')
        myLayout.draw(win)
         
        myLayout = Line(Point(-10,i-10),Point(10,i-10))
        myLayout.setFill('grey')
        myLayout.draw(win)
           
    armX = Line(Point(0,-10),Point(0,10))
    armX.setWidth(2)
    armX.draw(win)
     
    armY = Line(Point(-10,0),Point(10,0))
    armY.setWidth(2)
    armY.draw(win)
     
    for i in range(0,21):
        showline = Line(Point(i-10,-0.25),Point(i-10,0.25))
        showline.setWidth(2)
        showline.draw(win)
         
        showline = Line(Point(-0.25,i-10),Point(0.25,i-10))
        showline.setWidth(2)
        showline.draw(win)
         
    z = -10
     
    for i in range(1,10):
        num = Text(Point(i,-0.6),i)
        num.setSize(6)
        num.draw(win)
         
        num = Text(Point(i-10,-0.6),z+i)
        num.setSize(6)
        num.draw(win)
         
        num = Text(Point(-0.7,i),i)
        num.setSize(6)
        num.draw(win)
         
        num = Text(Point(-0.7,i-10),z+i)
        num.setSize(6)
        num.draw(win)
     
    introductionText = Text(Point(0,13),'Click two points on map to draw line')
    introductionText2 = Text(Point(0,11.75),'and get length and slope info')
    introductionText.draw(win)
    introductionText2.draw(win)
     
    Text(Point(-7.5,-12),'Slope: ').draw(win)
    Text(Point(3,-12),'Length: ').draw(win)
     
    slopeBox = Entry(Point(-3.5,-12),6)
    slopeBox.setText('?')
    slopeBox.draw(win)
      
    lengthBox = Entry(Point(7,-12),6)
    lengthBox.setText('?')
    lengthBox.draw(win)
         
    p1 = win.getMouse()
    p1.draw(win)
    print(p1)
     
    p2 = win.getMouse()
    p2.draw(win)
    print(p2)
    print()
     
    drawLine = Line(p1,p2)
    drawLine.setWidth(2)
    drawLine.draw(win)
     
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
     
    dx = x2-x1
    dy = y2-y1
     
    print('dx =',dx)
    print('dy =',dy)
    print()
     
    Xmiddle = x2-(dx/2)
    Ymiddle = y2-(dy/2)
     
    midPoint = Circle(Point(Xmiddle,Ymiddle),0.2)
    midPoint.setWidth(0)
    midPoint.setFill('cyan')
    midPoint.draw(win)
     
    length = math.sqrt(dx**2+dy**2)
    length = round(length,3)
    lengthBox.setText(length)
     
    introductionText.undraw()
    introductionText2.setText('Done! Click anywhere to quit!')
    introductionText2.setFill('yellow')
    introductionText2.move(0,0.5)
    
    # Checking for vertical line condition here.
    if dx == 0:
      slopeBox.setFill('red') 
      slopeBox.setText('NONE!!') 
    else:
      slope = dy/dx
      slope = round(slope,3)
      slopeBox.setText(slope)

    win.getMouse()
    win.close()
     
main()
