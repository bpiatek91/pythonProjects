from graphics import *
win = GraphWin("Trees", 800, 600)
x = 150
y = 375
height = 150 #height of my tree
def drawTree (x,y,height):
	trunkWidth = height/3
	trunkHeight = height
	#Trunk

	p1 = Point(x,y)
	p2 = Point(x+trunkWidth, y+trunkHeight)
	trunk = Rectangle(p1,p2)
	trunk.setFill("brown")
	trunk.draw(win)
	
	#Branch
	
	p3 = Point(x+(trunkWidth/2), y-trunkHeight)
	p4 = Point(x-trunkWidth, y)
	p5 = Point(x+(trunkWidth*2), y)
	branch = Polygon(p3,p4,p5)
	branch.setFill("green")
	branch.draw(win)
	
	
	
def drawScene(x,y,height):
	for i in range (6): 
		drawTree(x,y,height)
		x+=100
		y-=25
		height -= 18
	
drawScene(x,y,height)
win.getMouse()