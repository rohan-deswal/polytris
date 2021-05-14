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

def translateToOrigin(basePolyomino):
	minX = [min([cell[0] for cell in basePolyomino.listOfCells])]
	minY = [min([cell[1] for cell in basePolyomino.listOfCells])]

	for cell in basePolyomino.listOfCells:
		cell[0] -= minX
		cell[1] -= minY
	return basePolyomino

def getValidationList(basePolyomino):
	return [translateToOrigin(rotatedBasePolyomino) for rotatedBasePolyomino in getRotations(basePolyomino)]

def removeDuplicates(polyominoes):
	index = 0
	indicesToRemove = []
	while index < len(polyominoes)-1:
		for i in range(index+1,len(polyominoes)):
			if sorted(polyominoes[index].listOfCells) == sorted(polyominoes[index+i].listOfCells):
				indicesToRemove.append(index+i)
	for index in indicesToRemove:
		del polyominoes[index]
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