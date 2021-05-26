from polyominoGen import *
from pyglet import shapes
from random import seed
from random import random as rnd

from basePolyomino import *

def hsv_to_rgb(h, s, v):
	'''To convert HSV to RGB, 
	H should be between 0 <= H < 360
	S and V should be between 0 and 1

	Formula courtesy of https://www.rapidtables.com/convert/color/hsv-to-rgb.html'''
	c = s * v
	x = c * (1 - abs((h/60)%2 - 1))
	m = v - c

	rgb_ = (0, 0, 0)
	if h<60:
		rgb_ = (c, x, 0)
	elif h<120:
		rgb_ = (x, c, 0)
	elif h<180:
		rgb_ = (0, c, x)
	elif h<240:
		rgb_ = (0, x, c)
	elif h<300:
		rgb_ = (x, 0, c)
	elif h<360:
		rgb_ = (c, 0, x)

	return (int((rgb_[0]+m)*255), int((rgb_[1]+m)*255), int((rgb_[2]+m)*255))

rotationValues = {
	'c': [0,-1],
	'a': [0,1]
}
class Polyomino:
	def __init__(self,n,xPos,yPos,scale,wl,wr, vel, no_of_polyomino, polyomino_piece):
		self.n = n
		self.no_of_polyomino = no_of_polyomino
		self.type = polyomino_piece[0]
		self.shapeCoords = polyomino_piece[1].listOfCells.copy()
		self.color = hsv_to_rgb(self.type * 360/no_of_polyomino, 0.7, 1)
		self.xPos = xPos
		self.yPos = yPos
		self.x = xPos * scale
		self.y = yPos * scale
		self.vel = vel
		self.scale = scale
		self.xdir = 0
		for coord in self.shapeCoords:
			coord[0] += xPos
			coord[1] += yPos
		self.wallLeft = wl
		self.wallRight = wr

	def reset(self,xPos,yPos, polyomino_piece):
		self.__init__(self.n, xPos, yPos,self.scale,self.wallLeft,self.wallRight, \
			self.vel, self.no_of_polyomino, polyomino_piece)

	def update(self,ydir):
		self.y += self.vel*ydir		
		for coord in self.shapeCoords:
			coord[1] += self.yPos - int(self.y)//self.scale
		self.yPos = int(self.y)//self.scale

	def centreOfMass(self):
		x_centreOfMass = 0
		y_centreOfMass = 0

		for point in self.shapeCoords:
			x_centreOfMass += point[0]
			y_centreOfMass += point[1]

		x_centreOfMass = x_centreOfMass//self.n
		y_centreOfMass = y_centreOfMass//self.n
		
		return [x_centreOfMass,y_centreOfMass]

	def rotate(self,rdir):
		 pivot = self.centreOfMass()
		 minVal = self.findMinX_or_Y(rdir)

		 for point in self.shapeCoords:
		 	c,s = rotationValues[rdir][0],rotationValues[rdir][1]

		 	nx = point[0] - pivot[0]
		 	ny = point[1] - pivot[1]

		 	rx = nx*c - ny*s
		 	ry = nx*s + ny*c

		 	point[0] = rx + pivot[0]
		 	point[1] = ry + pivot[1]

		 newMinVal = self.findMinX_or_Y(rdir)
		 diff = minVal - newMinVal

		 if rdir == 'c':
		 	for point in self.shapeCoords:
		 		point[1] += diff
		 elif rdir == 'a':
		 	for point in self.shapeCoords:
		 		point[0] += diff

	def setxdir(self,xdir):
		self.xdir = xdir
		self.xPos += self.xdir
		self.x = self.xPos*self.scale
		for point in self.shapeCoords:
			point[0] += xdir
		self.wallConstraint()

	def findMinX_or_Y(self,rdir):
		if rdir == 'c':
			return min(point[1] for point in self.shapeCoords)
		if rdir == 'a':
			return max(point[0] for point in self.shapeCoords)

	def wallConstraint(self):
		maxX = max(point[0] for point in self.shapeCoords)
		minX = min(point[0] for point in self.shapeCoords)
		if maxX > self.wallRight - 1:
			diff = maxX - self.wallRight + 1
			for point in self.shapeCoords:
				point[0] -= diff
		if minX < self.wallLeft:
			diff = self.wallLeft - minX
			for point in self.shapeCoords:
				point[0] += diff
				
	def draw(self):
		for point in self.shapeCoords:
			i = point[0]
			j = point[1]
			shapes.BorderedRectangle(i*self.scale, j*self.scale,
									  self.scale, self.scale,1,
									  self.color,(0,0,0)).draw()