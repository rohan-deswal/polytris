from math import sin,cos,radians
def getRotations(basePolyomino):
	rotations = []
	for angle in range(0,360,90):
		for cell in basePolyomino.listOfCells:
			cosAngle,sinAngle = cos(radians(angle)),sin(radians(angle))
			x = cell[0]
			y = cell[1]

			newX = int(x*cosAngle - y*sinAngle)
			newY = int(x*sinAngle + y*cosAngle)

			cell[0],cell[1] = newX,newY

			rotations.append(basePolyomino)
	return rotations

def translateToOrigin(listOfCells):
	minX = min([cell[0] for cell in listOfCells])
	minY = min([cell[1] for cell in listOfCells])
	print(minX,minY)
	print("Before:",listOfCells)
	for i in range(len(listOfCells)):
		listOfCells[i][0] -= minX
		listOfCells[i][1] -= minY
	print("After:",listOfCells)
	return listOfCells

def getValidationList(basePolyomino):
	return [translateToOrigin(rotatedBasePolyomino) for rotatedBasePolyomino in getRotations(basePolyomino)]

def removeDuplicates(polyominoes):
	index = 0
	
	while index < len(polyominoes)-1:
		indicesToRemove = []
		for i in range(index+1,len(polyominoes)):
			if sorted(polyominoes[index].listOfCells) == sorted(polyominoes[i].listOfCells):
				indicesToRemove.append(i)
		index += 1
		indicesToRemove = list(set(indicesToRemove))
		indicesToRemove = sorted(indicesToRemove, reverse=True)
		for subIndex in indicesToRemove:
			del polyominoes[subIndex]
	return polyominoes
def removeByValidator(validator,polyominoes):
	index = 0
	indicesToRemove = []
	while index < len(polyominoes):
		if sorted(validator.listOfCells) == sorted(polyominoes.listOfCells):
			indicesToRemove.append(index)
	for index in indicesToRemove:
		del polyominoes[index]
	return polyominoes

def printPoly(listOfCells,n):
	print("Printing")
	for i in range(n):
		for j in range(n):
			if [i,j] in listOfCells:
				print('#',end='')
			else:
				print(' ',end='')
		print('')