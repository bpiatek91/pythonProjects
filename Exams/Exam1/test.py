#Brett Piatek
#6/29/16
#ACC CS 1336
#Exam 1 Lab

from graphics import *
win = GraphWin("Exam 1 Lab",300,300)
count = 0
while True: #Forever while loop that repeats the circle
	count = count +1 #sequences the forever loop
	radius = 60 #the original radius
	color1 = "red"
	color2 = "white"
	for ring in range (0,6): #for loop that draws the 6 circles
		radius = radius - 10 #calculates the difference in the circle radius'
		pt1 = Point(150,150)
		cir1 = Circle(pt1, radius) #the outer circle with the adjusting radius
		if (ring % 2 == 0):
			cir1.setFill(color1)
		else: 
			cir1.setFill(color2)
		if (count % 2 == 0):
			cir1.setFill(color2)
		else: 
			cir1.setFill(color1)
		cir1.draw(win)
	if win.checkMouse(): break #breaks the forever loop when the window is clicked