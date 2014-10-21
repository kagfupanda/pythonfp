#face.py
#progroam draws a face
#Author Siddharth Srinivasan
import graphics
from graphics import*
def main():
    win = GraphWin()
    head = Circle(Point(100,100), 100)
    eye1 = Circle(Point(50,50), 20)
    eye2 = Circle(Point(150,50), 20)
    pupil1 = Point(50,50)
    pupil2 = Point(150,50)
    mouth = Line(Point(50,150), Point(150,150))
    head.draw(win)
    eye1.draw(win)
    eye2.draw(win)
    pupil1.draw(win)
    pupil2.draw(win)
    mouth.draw(win)
    head.setFill('green')
    eye1.setFill('white')
    eye2.setFill('white')
    win.getMouse()
    win.close()

main()
