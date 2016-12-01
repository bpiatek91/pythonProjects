#Brett Piatek
#7/17/16
#COSC 1336
#Lab 7

from graphics import *

win = GraphWin("Lab 7", 500,500)

def drawCircle(x,y,radius,color):
    c = Circle(Point(x,y),radius)
    c.setFill(color)
    c.draw(win)
def drawTriangle(p1,p2,p3,p4,p5,p6,color):
	triangle = Polygon(Point(p1,p2), Point(p3,p4), Point(p5,p6))
	triangle.setFill(color)
	triangle.draw(win)
def drawRectangle(x1,y1,x2,y2,color):
	rec = Rectangle(Point(x1,y1),Point(x2,y2))
	rec.setFill(color)
	rec.draw(win)

def main():
    fin = open("drawing.dat","r")
    code = fin.readline().strip()
    while code != '':
        if code == "circle":
            color = fin.readline().strip()
            x = int(fin.readline())
            y = int(fin.readline())
            radius = int(fin.readline())
            drawCircle(x,y,radius,color)
        if code == "triangle":
            color = fin.readline().strip()
            p1 = int(fin.readline())
            p2 = int(fin.readline())
            p3 = int(fin.readline())
            p4 = int(fin.readline())
            p5 = int(fin.readline())
            p6 = int(fin.readline())
            drawTriangle(p1,p2,p3,p4,p5,p6,color)
        if code == "rectangle": 
            color = fin.readline().strip()
            x1 = int(fin.readline())#Error begins here. It says: "X1 is not defined"
            y1 = int(fin.readline())
            x2 = int(fin.readline())
            y2 = int(fin.readline())
            drawRectangle(x1,y1,x2,y2,color)
			
        code = fin.readline().strip()

main()
win.getMouse()
win.close()