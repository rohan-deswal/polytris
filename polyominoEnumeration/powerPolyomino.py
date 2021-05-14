from basePolyomino import BasePolyomino
import validationHelp
class PowerPolyomino(BasePolyomino):
	def __init__(self,listOfCells):
		BasePolyomino.__init__(self,listOfCells)

		self.adjacentCells = []
		self.generateAdjacentCells()

		self.updatedPolyominoes = []
		self.generateUpdatedPolyominoes()		

		print("pretrans")
		for i in range(len(self.updatedPolyominoes)):
			print(self.updatedPolyominoes[i].listOfCells)
		# for p in self.updatedPolyominoes:
		# 	print(p.listOfCells)
			
		self.translateOrigin()
		# for x in self.updatedPolyominoes:
		# 	print(x.listOfCells)
		
		# print("posttrans")
		# for p in self.updatedPolyominoes:
		# 	validationHelp.printPoly(p.listOfCells, len(p.listOfCells))
		
		self.updatedPolyominoes = validationHelp.removeDuplicates(self.updatedPolyominoes)

	def translateOrigin(self):
		for i in range(len(self.updatedPolyominoes)):
			print("_________________________")
			listOfCells = [cell for cell in self.updatedPolyominoes[i].listOfCells].copy()
			print(listOfCells)
			newList = validationHelp.translateToOrigin(listOfCells.copy())
			self.updatedPolyominoes[i].listOfCells = newList.copy()
			print("_________________________")
		a = input()
	def generateAdjacentCells(self):
		offSets = [(-1,0),(0,1),(1,0),(0,-1)]
		for cell in self.listOfCells:
			for offSet in offSets:
				newAdjacent = [cell[0]+offSet[0],cell[1]+offSet[1]]
				if not newAdjacent in self.listOfCells:
					if not newAdjacent in self.adjacentCells:
						self.adjacentCells.append(newAdjacent)

	def generateUpdatedPolyominoes(self):
		for cell in self.adjacentCells:
			self.updatedPolyominoes.append(BasePolyomino(self.listOfCells+[cell]))


