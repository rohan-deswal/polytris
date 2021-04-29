from pyglet import shapes
class Pile:
	def __init__(self,scale,wl,wr,bottom = -1):
		self.scale = scale
		self.cellCoords = []
		for xPos in range(wl,wr):
			self.cellCoords.append([xPos,bottom])
		self.bottom = bottom
		self.maxY = bottom + 1
		self.wallLeft = wl
		self.wallRight = wr

	def addToPile(self,shapeCoords):
		for point in shapeCoords:
			self.cellCoords.append([point[0],point[1]])
			if point[1] > self.maxY:
				self.maxY = point[1]

	def collidePolyomino(self,shapeCoords):
		for piece in shapeCoords:
			if self.findList([piece[0],piece[1]-1]):
				return True
		return False
	def addPolyomino(self,shapeCoords):
		for piece in shapeCoords:
			self.addToPile(shapeCoords)
	def findList(self,coord):
		for point in self.cellCoords:
			if point[0] == coord[0] and point[1] == coord[1]:
				return True
		return False

	def update(self):
		count = 0
		for y in range(self.bottom + 1,self.maxY+1):
			for x in range(self.wallLeft,self.wallRight):
				if self.findList([x,y]):
					count += 1
					
			if count == self.wallRight - self.wallLeft + 1:
				for x in range(self.wallLeft,self.wallRight):
					self.cellCoords.remove([x,y])
				for ny in range(y+1,self.maxY+1):
					for x in range(self.wallLeft,self.wallRight):
						if self.findList([x,ny]):
							self.cellCoords.remove([x,ny])
							self.cellCoords.append([x,ny-1])

			count = 0

	def pullDown(self,shapeCoords):
		for point in shapeCoords:
			point[1] -= 1
		return shapeCoords

	def hardDrop(self,shapeCoords):
		while True:
			if self.collidePolyomino(shapeCoords):
				self.addPolyomino(shapeCoords)
				break
			shapeCoords = self.pullDown(shapeCoords)

	def verifyXMotion(self,shapeCoords,xdir):
		for point in shapeCoords:
			if self.findList([point[0] + xdir,point[1]]):
				return False
		else:
			return True

	def draw(self):
		for coord in self.cellCoords:
			i = coord[0]
			j = coord[1]
			shapes.BorderedRectangle(i*self.scale, j*self.scale, self.scale, self.scale,1,(255,179,71),(0,0,0)).draw()