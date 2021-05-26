from powerPolyomino import PowerPolyomino
from basePolyomino import BasePolyomino
from validationHelp import *

'''
This is the main Polyomino Enumeration function which handles:
	Initiation
	Validation Against Rotations 
	Growth
'''
def enumeratePolyominoes(n):

	'''
	Initialization of the Base Polyomino
	'''
	currentPolyominoes = [PowerPolyomino([[0,0]])]
	nextPolyominoes = []
	
	for i in range(1,n): #This line represents the order of Growth For the required Polyominos
		for powerPolyomino in currentPolyominoes:
			index = 0

			# while index < len(powerPolyomino.updatedPolyominoes):
			while len(powerPolyomino.updatedPolyominoes) > 0: 
			
				'''
				Here we are getting a list of 4 possible rotation states of the current polyomino
				all translated as if the bottom-left is at origin
				'''
				validationList = np.copy(getValidationList(powerPolyomino.updatedPolyominoes[0]))
				'''
				We compare this to every other polyomino in the updatedPolyominoes
				of the current Polyomino to remove different rotation states of the
				same Polyomino.
				'''
				for validator in validationList:
					powerPolyomino.updatedPolyominoes = np.copy(removeByValidator(validator, powerPolyomino.updatedPolyominoes))
				index+=1
				# Adding the updatedPolyomino list which is the next stage to nextPolyominoes
				nextPolyominoes = np.concatenate((nextPolyominoes, np.array([validationList[1]])))

			nextPolyominoes = np.copy(removeDuplicates(nextPolyominoes))

				

		nextPolyominoes = np.copy(removeDuplicates(nextPolyominoes))
		currentPolyominoes = [PowerPolyomino(np.copy(polyomino.listOfCells)) for polyomino in nextPolyominoes]
		nextPolyominoes = []

		#Moving to the next iteration


	# Returning all one sided polyominoes of size n
	newList = []
	while len(currentPolyominoes) > 0:
		finalValidationList = np.copy(getValidationList(currentPolyominoes[0]))
		for validator in finalValidationList:
			currentPolyominoes = np.copy(removeByValidator(validator, currentPolyominoes))
		newList.append(finalValidationList[0])
	return newList

# n = int(input("Enter N: "))
# x = enumeratePolyominoes(n)
# print("Results")
# for polyomino in x:
# 	printPoly(polyomino.listOfCells, n)
# print(len(x))