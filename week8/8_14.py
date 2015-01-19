#8_14.py
#Author Siddharth Srinivasan
from graphics import *

def getImage():
    win_input = GraphWin('Grayscale Converter',400,450)
    win_input.setCoords(0, 0, 10, 10)
    win_input.setBackground('white')
    purple1 = color_rgb(62,158,71)
    purple2 = color_rgb(82,19,53)
    purple3 = color_rgb(117,57,90)
    bckgr = Polygon(Point(0,0),Point(0,10),Point(9.7,10),Point(4.7,0))
    bckgr.setOutline(purple3)
    bckgr.setFill(purple3)
    bckgr.draw(win_input)
    bckgr = Polygon(Point(0,0),Point(0,10),Point(8,10),Point(3.5,0))
    bckgr.setOutline(purple2)
    bckgr.setFill(purple2)
    bckgr.draw(win_input)
    bckgr = Polygon(Point(1,0),Point(2,10),Point(6,10),Point(2.6,0))
    bckgr.setOutline(purple1)
    bckgr.setFill(purple1)
    bckgr.draw(win_input)
    imgName = Entry(Point(3,2),20)
    imgName.draw(win_input)
    okButton = Rectangle(Point(7,3),Point(9,1))
    okButton.setFill('gray')
    okButton.setWidth(0)
    okButton.draw(win_input)
    okText = Text(Point(8,2),'OK')
    okText.draw(win_input)
    introText = Text(Point(5,8), 'Enter file name into the text box below and press OK button to start convertion.')
    introText.setFace('times roman')
    introText.draw(win_input)
     
    introText1 = Text(Point(5,5),'Image supported: .gif and .ppm. Don\'t use too large image!')
    introText1.setSize(8)
    introText1.setFace('times roman')
    introText1.draw(win_input)
    while True:
        where = win_input.getMouse()
        if 9 > where.getX() > 7 and  3 > where.getY() > 1:
            if imgName.getText() != '':
                fileName = imgName.getText()
                photo = Image(Point(5,7),fileName)
                photo.draw(win_input)
                break
            imgName.setText('No file supported found.')
    win_input.close()
    return photo

def displayImage(photo):
    x = photo.getWidth()
    y = int(photo.getHeight())
    if x < 400 and y < 300:
        win_output = GraphWin('Grayscale Converter',400,360)
    elif x < 400 :
        win_output = GraphWin('Grayscale Converter',400,y*1.2)
    elif y < 300:
        win_output = GraphWin('Grayscale Converter',x,360)
    else:
        win_output = GraphWin('Grayscale Converter',x,y*1.2)
    win_output.setCoords(0, 0, 10, 12)
    win_output.setBackground('white')
    purple1 = color_rgb(62,158,71)
    purple2 = color_rgb(82,19,53)
    purple3 = color_rgb(117,57,90)
    bckgr = Rectangle(Point(0,2),Point(10,0))
    bckgr.setOutline(purple3)
    bckgr.setFill(purple3)
    bckgr.draw(win_output)
    bckgr = Polygon(Point(3,0),Point(7,0),Point(9.2,2),Point(0.8,2))
    bckgr.setOutline(purple2)
    bckgr.setFill(purple2)
    bckgr.draw(win_output)
    bckgr = Polygon(Point(4,0),Point(6,0),Point(7.5,2),Point(2.5,2))
    bckgr.setOutline(purple1)
    bckgr.setFill(purple1)
    bckgr.draw(win_output)
    photo.draw(win_output)
    return win_output,x,y

def convertImage(photo,win_output,x,y):
    introText = Text(Point(5,1),'Press anywhere to start.')
    introText.setFace('times roman')
    introText.draw(win_output)
    win_output.getMouse()
    introText.setText('converting... ')
    for pX in range(x):
        for pY in range(y):
            r,g,b = photo.getPixel(pX,pY)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            gray = color_rgb(brightness,brightness,brightness)
            photo.setPixel(pX,pY,gray)
    update()
    introText.undraw()
def saveImage(photo,win_output):   
    entry_image_save = Entry(Point(5.5,1),13)
    entry_image_save.setText('sample.gif')
    entry_image_save.draw(win_output)
    button_save = Rectangle(Point(7.5,1.5),Point(9.5,0.5))
    button_save.setFill('gray')
    button_save.setWidth(0)
    button_save.draw(win_output)
    text_save = Text(Point(8.5,1),'Save')
    text_save.draw(win_output)
    introText = Text(Point(2,1),'Enter new filename:')
    introText.draw(win_output)
    while True:
        where = win_output.getMouse()
        if 9.5 > where.getX() > 7.5 and  1.5 > where.getY() > 0.5:           
            if entry_image_save.getText() != '':
                save_file = entry_image_save.getText()
                try:                   
                    photo.save(save_file)
                    break
                except:
                    entry_image_save.setText('sample.gif')
    button_save.undraw()
    text_save.undraw()
    entry_image_save.undraw()
    introText.undraw()
    introText = Text(Point(5,1),'Thank you! Press anywhere to close.')
    introText.draw(win_output)
    win_output.getMouse()
    win_output.close() 
 
def main():
    photo = getImage()
    win_output,x,y = displayImage(photo)
    convertImage(photo,win_output,x,y)
    saveImage(photo,win_output)
    
main() 
