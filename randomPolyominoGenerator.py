from random import shuffle
def getRandomPolyomino(n):
	# 1-n Polyomino
	polyominoBase = ([[0,0]])
	piecesAdded = 1
	for piece in polyominoBase:
		x = piece[0]
		y = piece[1]
		# print('x = '+str(x),'y = '+str(y))
		for i in range(-1,2):
			for j in range(-1,2):
				if i**2 + j**2 != 0:
					newX = x+i
					newY = y+j
					# print('newX = '+str(newX),'newY = '+str(newY))
					if [newX,newY] not in polyominoBase:
						if [newX-1,newY] in polyominoBase or [newX+1,newY] in polyominoBase or [newX,newY-1] in polyominoBase or [newX,newY+1] in polyominoBase:
							polyominoBase.append([newX,newY])
							# print(polyominoBase)
							shuffle(polyominoBase)
							piecesAdded += 1
							if piecesAdded == n:
								return polyominoBase


print(getRandomPolyomino(4))
