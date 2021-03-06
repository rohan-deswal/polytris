from math import sin,cos,radians
from polyominoEnumeration.basePolyomino import *
import numpy as np
'''
These are various helper functinos aid in 
polyomino enumeration
'''

def getRotations(basePolyomino):
	'''
	This polyomino generates a list of 
	polyominoes which are various rotation states
	of the input polyomino

	Right Now it Generates the following states:
		0 Degree
		90 Degree
		180 Degree
		270 Degree

	The above can be modified by changing the parameters
	of range function in the initial for loop
	'''
	rotations = []

	rotate0    = lambda cell: [cell[0],cell[1]]
	rotate90   = lambda cell: [cell[1],-cell[0]]
	rotate180  = lambda cell: [-cell[0],-cell[1]]
	rotate270  = lambda cell: [-cell[1],cell[0]]
	'''
	Here we apply the rotation matrix to every cell
	to get the rotated polyomino
	'''
	rotatedPolyominoListOfCells = []
	for cell in basePolyomino.listOfCells:
		newX,newY = rotate0(cell)
		rotatedPolyominoListOfCells.append([newX,newY])

	rotations.append(BasePolyomino(rotatedPolyominoListOfCells.copy()))
	rotatedPolyominoListOfCells = []
	for cell in basePolyomino.listOfCells:
		newX,newY = rotate90(cell)
		rotatedPolyominoListOfCells.append([newX,newY])

	rotations.append(BasePolyomino(rotatedPolyominoListOfCells.copy()))
	rotatedPolyominoListOfCells = []
	for cell in basePolyomino.listOfCells:
		newX,newY = rotate180(cell)
		rotatedPolyominoListOfCells.append([newX,newY])

	rotations.append(BasePolyomino(rotatedPolyominoListOfCells.copy()))
	rotatedPolyominoListOfCells = []
	for cell in basePolyomino.listOfCells:
		newX,newY = rotate270(cell)
		rotatedPolyominoListOfCells.append([newX,newY])

	rotations.append(BasePolyomino(rotatedPolyominoListOfCells.copy()))
	rotatedPolyominoListOfCells = []

	return rotations

def translateToOrigin(listOfCells):
	'''
	This function translates the given list of cells 
	such that all the cells have coordinates greater
	than or equal to 0.

	That is origin is the bottom-left most coordinate
	i.e. all cells are in the first quadrant of the cartesian plane
	'''
	minX = min([cell[0] for cell in listOfCells])
	minY = min([cell[1] for cell in listOfCells])

	
	for i in range(len(listOfCells)):
		listOfCells[i][0] -= minX
		listOfCells[i][1] -= minY

	return listOfCells

def getValidationList(basePolyomino):
	'''
	This function returns a list of translated rotation states of the given polyomino
	'''
	return [BasePolyomino(translateToOrigin(rotatedBasePolyomino.listOfCells)) for rotatedBasePolyomino in getRotations(basePolyomino)]

def removeDuplicates(polyominoes):
	'''
	This function is to remove duplucate polyominoes
	from a given list
	'''
	index = 0
	indicesToRemove = []
	while index < len(polyominoes)-1:
		 # Here we initiate a list of which indices we have delete
		for i in range(index+1,len(polyominoes)):
			'''
			We are first picking a polyomino at index
			then we compare it to all others after it and so on for each polyomino
			in the input list
			'''
			'''
			The line below compares the list of cells of the current polyomino
			to the list of cells of the next polyomino
			'''
			
			
			if compareListsOfLists(sorted([list(x) for x in polyominoes[index].listOfCells]),sorted([list(y) for y in polyominoes[i].listOfCells])):
				indicesToRemove.append(i) # Adding the index to which has to be removed
		index += 1

		'''
		The four lines below make a list of unique indices to delete
		then we sort the list in reverse and use the del keyword
		to delete polyominoes by index
		'''
	indicesToRemove = list(set(indicesToRemove))
	indicesToRemove = sorted(indicesToRemove, reverse=True)
	for subIndex in indicesToRemove:
		polyominoes = np.delete(polyominoes, subIndex)
	'''
	Now we return a list of unique polyominoes

	'''
	return polyominoes

def removeByValidator(validator,polyominoes):
	'''
	This function removes the copies of a given polyomino
	from a given list using the same logic as in above.
	'''
	index = 0
	indicesToRemove = []

	while index < len(polyominoes):
		if compareListsOfLists(sorted([list(x) for x in polyominoes[index].listOfCells]),sorted([list(y) for y in validator.listOfCells])):
			indicesToRemove.append(index)
		index+=1
	
	indicesToRemove = list(set(indicesToRemove))
	indicesToRemove = sorted(indicesToRemove, reverse=True)
	for index in indicesToRemove:
		polyominoes = np.delete(polyominoes, index)
	
	return polyominoes

def printPoly(listOfCells,n):
	'''
	This function gives a textual representation of a given list of cells
	'''
	print("_________________________")
	print("Polyomino: ")
	for i in range(n):
		for j in range(n):
			if searchListInListOfLists([i,j], listOfCells):
				print('#',end='')
			else:
				print(' ',end='')
		print('')
	print("_________________________")


'''
Searching Functions
'''
def searchListInListOfLists(subList,listOfLists):
	found = False
	for _subList in listOfLists:
		if compareList(_subList,subList):
			found = True
			break
	return found
def compareListsOfLists(listOfLists1,listOfLists2):
	count = 0
	for i in range(len(listOfLists1)):
		if compareList(listOfLists1[i], listOfLists2[i]):
			count += 1
	return count == len(listOfLists1)
def compareList(list1,list2):
	count = 0
	for i in range(len(list1)):
		if list1[i] == list2[i]:
			count += 1
	return count == len(list1)