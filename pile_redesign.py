from pyglet import shapes
class Pile_redesign:
	def __init__(self,scale,gridHeight,wl,wr,bottom = -1,):
		self.scale = scale
		self.grid = [[0 for i in range(gridHeight+1)]for j in range(wr-wl)]
		self.gridHeight = gridHeight
		for i in range(wr-wl):
			self.grid[i][0] = 1
		self.bottom = bottom
		self.maxY = bottom + 1
		self.wallLeft = wl
		self.wallRight = wr

	def addToPile(self,shapeCoords):
		for point in shapeCoords:
			self.grid[point[0]-self.wallLeft][point[1]-self.bottom] = 1
			if point[1] > self.maxY:
				self.maxY = point[1]

	def collidePolyomino(self,shapeCoords):
		for piece in shapeCoords:
			try:
				if self.grid[piece[0]-self.wallLeft][piece[1]-self.bottom - 1] == 1:
					return True
			except IndexError:
				continue
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
		for y in range(1,len(self.gridHeight)):
			sumPoly = 0
			for x in range(self.wallLeft-self.wallRight):
				if grid[x][y] == 1:
					sumPoly += 1
			if sumPoly == self.wallLeft-self.wallRight:
				for x in range(self.wallLeft-self.wallRight):
					grid[x][y] = 0

			for ny in range(y+1,self.gridHeight):
				if grid[x][y+1] == 1:
					grid[x][y-1] == 1

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
			try:
				if self.grid[point[0] - self.wallLeft + xdir][point[1]-self.bottom] == 1:
					return False
			except IndexError:
				continue
		else:
			return True

	def draw(self):
		for x in range(len(self.grid)):
			for y in range(len(self.grid[0])):
				if self.grid[x][y] == 1:
					i = self.wallLeft + x
					j = y + self.bottom
					shapes.BorderedRectangle(i*self.scale, j*self.scale, self.scale, self.scale,1,(255,179,71),(0,0,0)).draw()