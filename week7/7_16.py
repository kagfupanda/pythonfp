#7_16
#Author Siddharth Srinivasan
from graphics import *
import math
def scoreChecker(radius,scores):
    if radius<1:
        scores = scores+9
    elif radius<2:
        scores = scores+7
    elif radius<3:
        scores = scores+5
    elif radius<4:
        scores = scores+3
    else:
        scores = scores+1
    return scores
def main():
    win = GraphWin(,500,300)
    win.setCoords(-6, -6, 14, 6)
    colorBands = ["white","black","blue","red","yellow"]
    colorsIndex = 0
    for i in range(5):
        archersTarget = Circle(Point(0,0),(5-i))
        archersTarget.setFill(colorBands[colorsIndex])
        archersTarget.setOutline(colorBands[colorsIndex])
        archersTarget.draw(win)
        colorsIndex = colorsIndex+1       
         
    
     
    InfoText = Text(Point(7.7,5.2),"Click inside target to get scores.")
    InfoText.draw(win)
      
    scoreBoard = Rectangle(Point(6,4),Point(13.5,-2))
    scoreBoard.setFill("white")
    scoreBoard.draw(win)
     
    scoreBoardText = Text(Point(7.2,3.5),"Score:")
    scoreBoardText.draw(win)
     
    ScoreGraphics = Text(Point(9.75,1),"0")
    ScoreGraphics.setFace("times roman")
    ScoreGraphics.setSize(36)
    ScoreGraphics.draw(win)
     
    QuitButton = Rectangle(Point(10,-3),Point(13,-5))
    QuitButton.setFill("green")
    QuitButton.draw(win)
     
    QuitText = Text(Point(11.5,-4),"Quit")
    QuitText.draw(win)
     
    missText= Text(Point(9.75,-1),"Miss!")
    missText.setFill("red")
    missText.setSize(12)
    
 
    scores = 0
    missNotice = 0
    exit = 0
     
    for i in range(5):
         
        
        click = win.getMouse()
         

        x = click.getX()
        y = click.getY()
         
         

        if x<13 and x>10 and y>-5 and y<-3:
            exit = 1        
            break           
        else:
             
            Aim = Text(click,"x")
            Aim.setFill("purple")
            Aim.draw(win)
            radius = math.sqrt((x**2)+(y**2))                                    
            if radius<5:
                MissText.undraw()
                scores = scoreChecker(radius,scores)
                ScoreGraphics.setText(scores)                      
                MissNotice = 0 
            else:
                if MissNotice == 0:
                    MissText.draw(win)
                    MissNotice = 1
    if exit == 1:        
       win.close()
    else:
        InfoText.setText("Click anywhere to close.")
        win.getMouse()
        win.close()
         
     
main()
