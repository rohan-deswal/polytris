from polyominoGen import *
from pyglet import shapes

rotationValues = {
	'c': [0,-1],
	'a': [0,1]
}
class Polyomino:
	def __init__(self,n,xPos,yPos,scale):
		self.n = n
		self.shapeCoords,self.shapeMatrix = getPolyomino_Backtracking(n)
		self.xPos = xPos
		self.yPos = yPos
		self.x = xPos * scale
		self.y = yPos * scale
		self.vel = -0.5
		self.scale = scale
		for coord in self.shapeCoords:
			coord[0] += xPos
			coord[1] += yPos

	def update(self,xdir,ydir):
		self.y += self.vel*ydir
		self.xPos += xdir
		self.x = self.xPos * self.scale
		for coord in self.shapeCoords:
			coord[0] += xdir
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
		 print(minVal)
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

	def findMinX_or_Y(self,rdir):
		if rdir == 'c':
			return min(point[1] for point in self.shapeCoords)
		if rdir == 'a':
			return min(point[0] for point in self.shapeCoords)

	def draw(self):
		for point in self.shapeCoords:
			i = point[0]
			j = point[1]
			shapes.Rectangle(i*self.scale, j*self.scale, self.scale, self.scale, (255,179,71)).draw()

