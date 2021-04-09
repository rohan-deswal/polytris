import numpy as np

def getRandomPolyomino(n):
	# 1-n Polyomino
	polyominoBase = np.array([[0,0]])
	piecesAdded = 1
	for piece in polyominoBase:
		x = piece[0]
		y = piece[1]

		for i in range(-1,2):
			for j in range(-1,2):
				if i != 0 or j != 0:
					newX = x-i
					newY = y-j

					if not ([newX,newY] in polyominoBase) and any([ele in polyominoBase for ele in np.array([[newX-1,newY],[newX+1,newY],[newX,newY+1],[newX,newY-1]])]):
						polyominoBase = np.append(polyominoBase,[newX,newY])
						np.random.shuffle(polyominoBase)
						piecesAdded += 1
						if piecesAdded == n:
							print(piecesAdded)
							return polyominoBase


print(getRandomPolyomino(4))
