#futvalimp.py
#imporved version of the futval program
#Author Siddharth Srinivasan
import graphics
from graphics import*
def main():
    win = GraphWin("Futval", 300, 400)
    win.setCoords(0,0,3,6)
    Text(Point(1,5), "Initial Principal:").draw(win)
    Text(Point(1,4), "Annual Interest Rate:").draw(win)
    Text(Point(1,3), "Number of Years:").draw(win)
    Text(Point(1,1), "Final Amount:").draw(win)
    prinIn = Entry(Point(2,5), 10)
    prinIn.setText("0.0")
    prinIn.draw(win)
    annIn = Entry(Point(2,4), 10)
    annIn.setText("0.0");annIn.draw(win)
    yearIn = Entry(Point(2,3), 10)
    yearIn.setText("0.0");yearIn.draw(win)
    finalAmount = Text(Point(2,1), ""); finalAmount.draw(win)
    button = Text(Point(1.5,2.0),"Calculate"); button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    win.getMouse()
    p = eval(prinIn.getText())
    air = eval(annIn.getText())
    year = eval(yearIn.getText())
    for i in range(year):
        p = p * (1 + air)
    finalAmount.setText(p)
    button.setText("Quit")
    win.getMouse()
    win.close()
    


main()
