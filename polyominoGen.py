from random import randint,choice

import numpy as np

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
def translateToOrigin(coords):
    xCoords = [ele[0] for ele in coords]
    yCoords = [ele[1] for ele in coords]
    minX = min(xCoords)
    minY = min(yCoords)
    xCoords = [x - minX for x in xCoords]
    yCoords = [y - minY for y in yCoords]
    coords = []
    for i in range(len(xCoords)):
        coords.append([xCoords[i],yCoords[i]])
    return coords
def getPolyomino(n):
	if n <= 0:
		raise ValueError('Value of n must be greater than 0')
	elif n == 1:
		return [[0,0]],[[1]]
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
		matrixPolyomino = np.zeros((n,n), dtype='uint8')#[[0 for i in range(n)] for j in range(n)]
		
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
							if not checkForHoles(matrixPolyomino, n):
								return np.array(polyomino)
							else:
								pieces = 1
								matrixPolyomino = np.zeros((n, n), dtype='uint8')
								matrixPolyomino[0][0] = 1
							# return polyomino, matrixPolyomino	
def getPolyomino_Backtracking(n):
    if n <= 0:
    	raise ValueError('Value of n must be greater than 0')
    elif n == 1:
    	return [[0,0]],[[1]]
    else:
    	matrixPolyomino = np.zeros((n,n), dtype='uint8')
    	matrixPolyomino[0][0] = 1
    	pieces = 1
    	visited = [[0,0]]
    	current = [0,0]
    	while len(visited) < n:
    		neighbour = choice([0,1,2,3]) #'''0 for LEFT 1 for RIGHT 2 for UP 3 for DOWN'''
    		neighbours = [[current[0]-1,current[1]],[current[0]+1,current[1]],[current[0],current[1]+1],[current[0],current[1]-1]]
    		unvisited_neighbours = [cell for cell in neighbours if cell not in visited]
    		if len(unvisited_neighbours) > 0:
    			current_choice = choice(unvisited_neighbours)
    			visited.append(current_choice)
    			current = current_choice
    		else:
    			current = visited[-2]
    		if len(visited) == n:
    			
    			visited = translateToOrigin(visited)
    			# print(visited)
    			matrixPolyomino[0][0] = 0
    			for cell in visited:
    				matrixPolyomino[cell[0]][cell[1]] = 1
    			if not checkForHoles(matrixPolyomino, n):
    				return np.array(visited),matrixPolyomino
    			else:
    				pieces = 1
    				matrixPolyomino = np.zeros((n, n), dtype='uint8')
    				matrixPolyomino[0][0] = 1
    				visited = [[0,0]]
    				current = [0,0]