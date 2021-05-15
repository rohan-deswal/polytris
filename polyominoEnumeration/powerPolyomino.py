from basePolyomino import BasePolyomino
import validationHelp
'''
This class here inherits from the BasePolyomino Class
This class has internal functions to handle growth
and internal translation to the Origin 
'''
class PowerPolyomino(BasePolyomino):
	def __init__(self,listOfCells):
		BasePolyomino.__init__(self,listOfCells)

		'''
		The next two lines generate a list of empty cells which can be used
		as a place where the next cell will be added i.e. possible 
		locations of growth
		'''
		self.adjacentCells = []
		'''
		This is a list of coordinates of available cells
		where each cell is stored as a list of x,y coordinates -> [x,y]
		'''
		self.generateAdjacentCells()

		'''
		The next two lines create a list of child polyominoes which stores
		every possible growth.
		'''
		self.updatedPolyominoes = []
		self.generateUpdatedPolyominoes()		
		
		'''
		Here we translate all the polyominoes in updatedPolyominoes
		list so that bottom-left piece is at origin
		'''
		self.translateToOrigin()

		'''
		This is to remove the duplicate polyominoes which 
		could have been generated during the growth
		'''
		self.updatedPolyominoes = validationHelp.removeDuplicates(self.updatedPolyominoes)

	def translateToOrigin(self):
		'''
		Here we translate to origin by passing through a list of cells of each
		polyomino one by one present in the updatedPolyomino list 
		to the translation function in validationHelp.py
		'''
		for i in range(len(self.updatedPolyominoes)):
			print("_________________________") #Debugging
			# Creation of list to be sent translated
			listOfCells = [cell for cell in self.updatedPolyominoes[i].listOfCells].copy()
			print(listOfCells) #Debugging
			'''
			Calling the translate function in validationHelp.py
			and storing the new translated list
			'''
			newList = validationHelp.translateToOrigin(listOfCells.copy())
			'''
			Resetting the current Polyomino with the new translated list
			'''
			self.updatedPolyominoes[i].listOfCells = newList.copy()
			print("_________________________") #Debugging

	def generateAdjacentCells(self):
		'''
		This is the function to generate a list cells
		which are available for growth
		'''
		'''
		Next line is a list of off sets that is to go
		Left, Up, Right, Down
		'''
		offSets = [(-1,0),(0,1),(1,0),(0,-1)]
		for cell in self.listOfCells:
			for offSet in offSets:
				'''
				Getting the a new adjacent cell by adding the offset to the current cell
				'''
				newAdjacent = [cell[0]+offSet[0],cell[1]+offSet[1]]

				'''
				Checking if the new cell is already there or
				previously occupied
				'''
				if not newAdjacent in self.listOfCells:
					if not newAdjacent in self.adjacentCells:
						self.adjacentCells.append(newAdjacent)

	def generateUpdatedPolyominoes(self):
		'''
		Here we generate the list of updated or child polyominoes
		by making an object of BasePolyomino class
		with the current list of cells added to it is a new cell from
		an available adjacent cell.

		Therefore we store every possible growth state
		for the polyomino
		'''
		for cell in self.adjacentCells:
			self.updatedPolyominoes.append(BasePolyomino(self.listOfCells+[cell]))


