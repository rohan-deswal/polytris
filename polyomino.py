from polyominoGen import *
from pyglet import shapes
class Polyomino:
	def __init__(self,n,xPos,yPos,scale):
		self.n = n
		self.shape_coords,self.shape_matrix = getPolyomino_Backtracking(n)
		self.xPos = xPos
		self.yPos = yPos
		self.x = xPos * scale
		self.y = yPos * scale
		self.vel = -0.5
		self.scale = scale

	def update(self,xdir):
		self.y += self.vel
		self.xPos += xdir
		self.x = self.xPos * self.scale
		self.yPos = int(self.y)//self.scale

	def draw(self):
		for i in range(self.n):
			for j in range(self.n):
				if self.shape_matrix[i][j] == 1:
					shapes.Rectangle(self.x + i*self.scale, self.yPos*self.scale + j*self.scale , self.scale, self.scale, (0,0,0)).draw()
					shapes.Rectangle(self.x + i*self.scale + self.scale//4, self.yPos*self.scale + j*self.scale + self.scale//4, self.scale*3/4, self.scale*3/4, (217,17,74)).draw()