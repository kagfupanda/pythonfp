#4.6.py
#calculates apr
#Author Siddharth Srinivasan
import graphics
from graphics import *
def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")


    win = GraphWin("Investment Growth Chart", 320, 280)
    win.setBackground("white")


    text1 = Text(Point(150, 80), "Enter the initial principal: ")
    text1.draw(win) 
    input = Entry(Point(150, 110), 20)
    input.setText("0.0")
    input.draw(win)
    button = Text(Point(150, 140), "Continue")
    button.draw(win)
    rect1 = Rectangle(Point(120, 130), Point(180, 150))
    rect1.draw(win)
    win.getMouse()
    principal = eval(input.getText())
    text1.undraw()
    button.undraw()
    input.undraw()
    rect1.undraw()

    text2 = Text(Point(150, 80), "Enter the interest rate: ")
    text2.draw(win)
    input = Entry(Point(150, 110), 20)
    input.setText("0.0")
    input.draw(win)
    button = Text(Point(150, 140), "Continue")
    button.draw(win)
    rect2 = Rectangle(Point(120, 130), Point(180, 150))
    rect2.draw(win)
    win.getMouse()
    apr = eval(input.getText())
    text2.undraw()
    button.undraw()
    input.undraw()
    rect2.undraw()

   
    Text(Point(20, 230), " 0.0K").draw(win)
    Text(Point(20, 180), " 2.5K").draw(win)
    Text(Point(20, 130), " 5.0K").draw(win)
    Text(Point(20, 80), " 7.5K").draw(win)
    Text(Point(20, 30), " 10.0K").draw(win)

 
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("blue")
    bar.setWidth(2)
    bar.draw(win)

    
    for year in range(1, 11):
        principal = principal * (1 + apr)
        y = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(y, 230), Point(y + 25, 230 - height))
        bar.setFill("blue")
        bar.setWidth(2)
        bar.draw(win)

    
    lrect = Rectangle(Point(260, 220), Point(320, 240))
    lrect.setFill("grey")
    lrect.draw(win)
    button = Text(Point(290, 230), "Done")
    button.draw(win)
    win.getMouse()
    win.close()

main()
