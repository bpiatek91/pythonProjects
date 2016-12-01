#artHouse.py
#Brett Piatek
#Lab 5 Art House
#6/26/2016
#CS 1336

from graphics import *

win = GraphWin("Cool Graphics Demo", 600, 400)	

def main(): 


#Background
	
	pt1 = Point(0,0)
	pt2 = Point(600,200)
	rec = Rectangle(pt1, pt2)
	rec.setFill("blue")
	rec.draw(win)
	
	h1 = Point(80, 275)
	hill1 = Circle(h1, 120)
	hill1.setFill("green3")
	hill1.draw(win)
	
	h = Point(180, 250)
	hill = Circle(h, 120)
	hill.setFill("green1")
	hill.draw(win)
	
	h2 = Point(350, 275)
	hill2 = Circle(h2, 120)
	hill2.setFill("green3")
	hill2.draw(win)

	pt3 = Point(0,200)
	pt4 = Point(600,400)
	rec = Rectangle(pt3, pt4)
	rec.setFill("green")
	rec.draw(win)

#Sun

	pt = Point(575,25)
	cir = Circle(pt, 80) 
	cir.setFill("yellow")
	cir.setOutline("red")
	cir.setWidth(5)
	cir.draw(win)

#Bush

	st1 = Point(135, 325)
	st2 = Point(145, 355)
	stem = Rectangle(st1, st2)
	stem.setFill("brown")
	stem.draw(win)

	b1 = Point(150, 325)
	bush = Circle(b1, 25)
	bush.setFill("green1")
	bush.draw(win)
	
	b2 = Point(140, 305)
	bush1 = Circle(b2, 25)
	bush1.setFill("green2")
	bush1.draw(win)
	
	b3 = Point(120, 325)
	bush2 = Circle(b3, 25)
	bush2.setFill("green3")
	bush2.draw(win)
	
	b4 = Point(160, 280)
	bush3 = Circle(b4, 25)
	bush3.setFill("forestgreen")
	bush3.draw(win)
	
	b5 = Point(130, 290)
	bush4 = Circle(b5, 25)
	bush4.setFill("green1")
	bush4.draw(win)
	
	

#House
	
	house1 = Point(200,150)
	house2 = Point(400,350)
	house = Rectangle(house1, house2)
	house.setFill("white")
	house.draw(win)
	
#Chimney
	c1 = Point(260, 20)
	c2 = Point(275, 100)
	chim = Rectangle(c1, c2)
	chim.setFill("grey")
	chim.draw(win)

#Roof
	roof1 = Point(175, 150)
	roof2 = Point(425, 150) 
	roof3 = Point(300, 35) 
	roof = Polygon(roof1, roof2, roof3) 
	roof.setFill("brown4")
	roof.draw(win)
	

#Door

	door1 = Point(265, 245)
	door2 = Point(335, 350) 
	door = Rectangle(door1, door2) 
	door.setFill("red")
	door.draw(win)
	
	walk1 = Point(265, 350)
	walk2 = Point(335, 600)
	walk = Rectangle(walk1, walk2)
	walk.setFill("tan")
	walk.draw(win)
	
#Window

	window1 = Point(300,195)
	cir1 = Circle(window1, 30)
	cir1.setFill("turquoise")
	cir1.setOutline("black")
	cir1.setWidth(1)
	cir1.draw(win)
	
#WindowPane1
	
	pane1 = Point(297,167)
	pane2 = Point(303, 227)
	wpane1 = Rectangle(pane1, pane2)
	wpane1.setFill("white")
	wpane1.setOutline("white")
	wpane1.draw(win)
	
#WindowPane2
	
	pane3 = Point(267,193)
	pane4 = Point(330, 197)
	wpane2 = Rectangle(pane3, pane4)
	wpane2.setFill("white")
	wpane2.setOutline("white")
	wpane2.draw(win)
	
#Tree	
	
	t1 = Point(480,200)
	t2 = Point(500, 350)
	trunk = Rectangle(t1, t2)
	trunk.setFill("brown")
	trunk.draw(win)
	
	l1 = Point(490, 200)
	leaf = Circle(l1, 50)
	leaf.setFill("forestgreen")
	leaf.draw(win)
	
	
	win.getMouse()
	

main()