from pyglet import shapes

class Pile:
	def __init__(self,scale,gridHeight,wl,wr,bottom = -1,):
		self.scale = scale
		self.grid = [[None for i in range(gridHeight+1)]for j in range(wr-wl)]
		self.gridHeight = gridHeight
		for i in range(wr-wl):
			self.grid[i][0] = (0, 0, 0)
		self.bottom = bottom
		self.maxY = bottom + 1
		self.wallLeft = wl
		self.wallRight = wr

	def indexX(self,point):
		return point[0] - self.wallLeft
	def indexY(self,point):
		return point[1] - self.bottom
	def addToPile(self, shapeCoords, color):
		for point in shapeCoords:
			self.grid[self.indexX(point)][self.indexY(point)] = color
			if point[1] > self.maxY:
				self.maxY = point[1]

	def rotationCheck(self,shapeCoords):
		pass

	def collidePolyomino(self,shapeCoords):
		for point in shapeCoords:
			try:
				if self.grid[self.indexX(point)][self.indexY(point) - 1] is not None:
					return True
			except IndexError:
				continue
		return False

	def update(self):
		y = 1
		while y<self.gridHeight+1:
			sumPoly = 0
			for x in range(self.wallRight-self.wallLeft):
				if self.grid[x][y] is not None:
					sumPoly += 1
					
			if sumPoly == self.wallRight-self.wallLeft:
				for x in range(self.wallRight-self.wallLeft):
					self.grid[x][y] = None

				for ny in range(y+1,self.gridHeight+1):
					for x in range(self.wallRight-self.wallLeft):
						try:
							if self.grid[x][ny] is not None:
								self.grid[x][ny-1] = self.grid[x][ny]
								self.grid[x][ny] = None
						except IndexError:
							pass
			else:
				y += 1
	def pullDown(self,shapeCoords):
		for point in shapeCoords:
			point[1] -= 1
		return shapeCoords

	def hardDrop(self,shapeCoords, color):
		while True:
			if self.collidePolyomino(shapeCoords):
				self.addToPile(shapeCoords, color)
				break
			shapeCoords = self.pullDown(shapeCoords)

	def verifyXMotion(self,shapeCoords,xdir):
		for point in shapeCoords:
			try:
				if self.grid[self.indexX(point) + xdir][self.indexY(point)] is not None:
					return False
			except IndexError:
				continue
		else:
			return True

	def draw(self):
		for x in range(len(self.grid)):
			for y in range(len(self.grid[0])):
				if self.grid[x][y] is not None:
					i = self.wallLeft + x
					j = y + self.bottom
					shapes.BorderedRectangle(i*self.scale, j*self.scale, self.scale, self.scale,1,self.grid[x][y],(0,0,0)).draw()