#7_14.py
#Author Siddharth Srinivasan

from graphics import *
import math
 
def main():
        win = GraphWin('Circle intersection',600,300)
        win.setCoords(0,0,24,12)
        win.setBackground('White')
        cBgr = Rectangle(Point(1,11),Point(11,1))
        cBgr.setFill('grey')
        cBgr.draw(win)
        Line(Point(6,1),Point(6,11)).draw(win)
        Line(Point(1,6),Point(11,6)).draw(win)
        for i in range(2,23):
            i = i/2
            Line(Point(0.75,i),Point(1.25,i)).draw(win)
            Line(Point(i,10.75),Point(i,11.25)).draw(win)
        z = q = 6
        for i in range(0,11):
            num = Text(Point(0.5,z),i)
            num.setSize(6)
            num.draw(win)
            num2 = Text(Point(z,11.5),i)
            num2.setSize(6)
            num2.draw(win)
            num3 = Text(Point(q,11.5),i*-1)
            num3.setSize(6)
            num3.draw(win)
            num3 = Text(Point(0.5,q),i*-1)
            num3.setSize(6)
            num3.draw(win)
            z = z+0.5  
            q = q-0.5
        introText1 = Text(Point(17.40,10.75),'Program to calculate X value where')
        introText1.setStyle('bold')
        introText1.draw(win)
        introText2 = Text(Point(15.8,10),'Y intersection with circle.')
        introText2.setStyle('bold')
        introText2.draw(win)
        Text(Point(15.75,8.5),'Circle radius (value 1-10): ').draw(win)
        rightInput = Entry(Point(14,7.5),10)
        rightInput.setText('0')
        rightInput.draw(win)
        Text(Point(18,6),'Horizon line intersection (value 10 to -10): ').draw(win)
        yIn = Entry(Point(14,5),10)
        yIn.setText('0')
        yIn.draw(win)
        Text(Point(14.5,3.5),'X intersection at: ').draw(win)
        Text(Point(12.2,2.70),'+').draw(win)
        Text(Point(12.2,2.25),'-').draw(win)
        xResponse = Entry(Point(14.5,2.5),10)
        xResponse.setText('?')
        xResponse.draw(win)
        myButton = Rectangle(Point(19,2),Point(23.5,0.5))
        myButton.setFill('green')
        myButton.draw(win)
        myButton =  Text(Point(21.25,1.25),'Find Answer!')
        myButton.draw(win)
        win.getMouse()
        R = eval(rightInput.getText())
        Y = eval(yIn.getText())
        result = R**2-Y**2
        if (result < 0):
          X=0
          xResponse.setFill('red')
          xResponse.setText('None')
        else:
          X = math.sqrt(R**2-Y**2)
          X = round(X,2)
          xResponse.setText(X)
        R = R/2
        resultC = Circle(Point(6,6),R)
        resultC.setFill('yellow')
        resultC.draw(win)
        Line(Point(6,1),Point(6,11)).draw(win)
        Line(Point(1,6),Point(11,6)).draw(win)
        Y = Y/2+6
        lineY = Line(Point(1,Y),Point(11,Y))
        lineY.setFill('green')
        lineY.draw(win)
        X = X/2
        Xa = X+6
        Xb = 6-X
        resultPa = Circle(Point(Xa,Y),0.1)
        resultPa.setFill('red')
        resultPa.draw(win)
        resultPb = Circle(Point(Xb,Y),0.1)
        resultPb.setFill('red')
        resultPb.draw(win)
        myButton.setText('Quit')
        win.getMouse()
        win.close()
     
main()
