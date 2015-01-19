#8_13.py
#Author Siddharth Srinivasan

from graphics import *
 
def myWindow():
    win = GraphWin('Plotting a Regression Line',400,300)
    win.setCoords(0,0,40,30)
    win.setBackground('pink')
    color1 = color_rgb(60,77,68)
    color2 = color_rgb(147,237,159)
    color3 = color_rgb(61,64,102)
    greenBox = Rectangle(Point(0,4),Point(40,4.5))
    greenBox.setFill(color1)
    greenBox.setWidth(0)
    greenBox.draw(win)
    box2 = Rectangle(Point(0,0),Point(40,4))
    box2.setFill(color2)
    box2.setWidth(0)
    box2.draw(win)
    boxText = Text(Point(16.5,2.75),'My Regression Line')
    boxText.setFace('times roman')
    boxText.setSize(12)
    boxText.setTextColor('blue')
    boxText.draw(win)
    boxText2 = Text(Point(23.20,1),'Click to enter data point and click DONE when finished.')
    boxText2.setSize(7)
    boxText2.setTextColor('black')
    boxText2.draw(win)
    buttonBorder = Rectangle(Point(0.5,0.4),Point(9.5,3.7))
    buttonBorder.setFill('purple')
    buttonBorder.draw(win)
    mybutton = Rectangle(Point(0.75,0.65),Point(9.25,3.5))
    mybutton.setFill(color3)
    mybutton.draw(win)
    buttonText = Text(Point(5,2),'Done')
    buttonText.setFace('times roman')
    buttonText.setSize(12)
    buttonText.setTextColor('black')
    buttonText.draw(win)
    Line(Point(2,6.5),Point(2,28)).draw(win)
    Line(Point(2,6.5),Point(38,6.5)).draw(win)
    for i in range(36):
        Line(Point(i+3,6.25),Point(i+3,6.75)).draw(win)
    for i in range(0,36,5): 
        Line(Point(i+8,6.05),Point(i+8,6.95)).draw(win)
    for i in range(21):       
        Line(Point(1.75,i+7.5),Point(2.25,i+7.5)).draw(win)
    for i in range(0,21,5):   
        Line(Point(1.55,i+11.5),Point(2.45,i+11.5)).draw(win)   
    warn = Text(Point(20,18),'click inside field to input data.')
    warn.setSize(10)
    warn.setTextColor('yellow')
    return win,warn,buttonText
 
def processData(pX,pY,num,xTotal,yTotal,xy,x2):
    pX = pX-2
    pY = pY-6.5            
    num = num+1
    xTotal = xTotal+pX             
    yTotal = yTotal+pY             
    xy = xy + (pX*pY)    
    x2 = x2+pX**2  
    return num,xTotal,yTotal,xy,x2
 
def drawregressLine(num,xTotal,yTotal,xy,x2,win):
    xMean = xTotal/num             
    yMean = yTotal/num             
    m = (xy - (num*xMean*yMean)) / (x2 - (num*(xMean**2)))
    Ymin = yMean + m*(0-xMean)
    Ymax = yMean + m*(36-xMean)
    Rline = Line(Point(2,Ymin+6.5),Point(38,Ymax+6.5))
    Rline.draw(win)
     
def main():
    win,warn,buttonText = myWindow()  
    num,xTotal,yTotal,xy,x2 = 0,0,0,0,0
    while True:
        p = win.getMouse()
        pX = p.getX()
        pY = p.getY()
        if 38 >= pX >= 2 and 28 >= pY >= 6.5:
            warn.undraw()          
            p.draw(win)
            num,xTotal,yTotal,xy,x2 = processData(pX,pY,num,xTotal,yTotal,xy,x2)
        elif num >= 2 and 9.5 >= pX >= 0.5 and 3.7 >= pY >= 0.4:
            warn.undraw()          
            drawregressLine(num,xTotal,yTotal,xy,x2,win)
            break
        else:
            warn.undraw()          
            warn.draw(win)
    buttonText.setText('Close')
    win.getMouse()

main()
