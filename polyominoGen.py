from random import randint

def getPolyomino(n):
	if n <= 0:
		raise ValueError('Value of n must be greater than 0')
	elif n == 1:
		return [[0,0]]
		'''
		Here we have initialized the N=1 Polyomino which is a single cell
		'''

	else:
		'''
		The function returns a list of coordinates from [0,0] to [n-1,n-1]
		which form the Polyomino.
		'''

		'''
		Initialization of the matrix that represents the polyomino
		'''
		matrixPolyomino = [[0 for i in range(n)] for j in range(n)]
		
		'''
		Seed Cell is begin set at [0,0]
		'''
		matrixPolyomino[0][0] = 1

		pieces = 1
		while pieces < n:
			for i in range(n):
				for j in range(n):
					if matrixPolyomino[i][j] == 1:
						'''
						Generating a random number to pick whether to
						go UP, DOWN, LEFT OR RIGHT
						'''
						valRandom = randint(0, 3)
						if valRandom == 0:
							if i-1 >= 0:
								if matrixPolyomino[i-1][j] != 1:
									matrixPolyomino[i-1][j] = 1
									pieces += 1
						elif valRandom == 1:
							if i+1 < n:
								if matrixPolyomino[i+1][j] != 1:
									matrixPolyomino[i+1][j] = 1
									pieces += 1
						elif valRandom == 2:
							if j-1 >= 0:
								if matrixPolyomino[i][j-1] != 1:
									matrixPolyomino[i][j-1] = 1
									pieces += 1
						elif valRandom == 3:
							if j+1 < n:
								if matrixPolyomino[i][j+1] != 1:
									matrixPolyomino[i][j+1] = 1
									pieces += 1
						if pieces == n:
							polyomino = []
							for x in range(n):
								for y in range(n):
									'''
									Here the list of coordinates is being formed based
									on the values in the matrix that represents the polyomino.
									'''
									if matrixPolyomino[x][y] == 1:
										polyomino.append([x,y])
							return polyomino	

def checkForHoles(matrixPolyomino,n):
	'''
	Function to check for holes 
	to discard undesired polyominoes
	'''
	for i in range(n):
		for j in range(n):
			if matrixPolyomino[i][j] == 0:
				boolList = [i-1>=0,i+1<n,j-1>=0,j+1<n]
				if all(boolList):
					newBoolList = [
					matrixPolyomino[i-1][j] == 1,
					matrixPolyomino[i+1][j] == 1,
					matrixPolyomino[i][j-1] == 1,
					matrixPolyomino[i][j+1] == 1
					]
					if all(newBoolList):
						return True
	return False