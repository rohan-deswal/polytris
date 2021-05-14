from basePolyomino import BasePolyomino
import validationHelp
class PowerPolyomino(BasePolyomino):
	def __init__(self,listOfCells):
		super.__init__(self,listOfCells)

		self.adjacentCells = []
		self.generateAdjacentCells()

		self.updatedPolyominoes = []
		self.generateUpdatedPolyominoes()
		self.translateToOrigin()
		self.updatedPolyominoes = validationHelp.removeDuplicates(self.updatedPolyominoes)

	def generateAdjacentCells(self):
		offSets = [(-1,0),(0,1),(1,0),(0,-1)]
		for cell in self.listOfCells:
			for offSet in offSets:
				newAdjacent = [cell[0]+offSet[0],cell[1]+offSet[1]]
				if not newAdjacent in self.listOfCells and not newAdjacent in self.adjacentCells:
					self.adjacentCells.append(newAdjacent)

	def generateUpdatedPolyominoes(self):
		for cell in self.adjacentCells:
			self.updatedPolyominoes.append(BasePolyomino(self.listOfCells+[cell]))

	def translateToOrigin(self):
		for basePolyomino in self.updatedPolyominoes:
			basePolyomino = validationHelp.translateToOrigin(basePolyomino)