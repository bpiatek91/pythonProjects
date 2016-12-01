#Brett Piatek
#CS 1336
#7/10/16

from graphics import *
import time
width = 600
height = 400
radius = 25
dx = 3
dy = 3
speed = 1/20

def main(): 
	global dx, dy
	
#Pool Table

	win = GraphWin('Pool Table', 600, 400)
	win.setBackground("green")
	win.getMouse()
	
#Pool Ball
	ball = Circle(Point(width/2, height/2), radius)
	ball.setFill('purple')
	ball.draw(win)
	
	while 1 == 1: 
		ball.move(dx, dy)
		time.sleep(speed)
		center = ball.getCenter()
		current_x = center.getX()
		current_y = center.getY()	
		if (current_x >= width - radius): 	
			dx = -dx
		if (current_x <= (width-600) + radius): 	
			dx = -dx
		if (current_y >= height-radius):
			dy = -dy
		if (current_y <= (height-400) + radius):
			dy = -dy
		if win.checkMouse(): break
main()

