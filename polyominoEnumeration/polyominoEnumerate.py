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
	
	for i in range(1,n-1): #This line represents the order of Growth For the required Polyominos
		for powerPolyomino in currentPolyominoes:
			index = 0
			while index > len(powerPolyomino.updatedPolyominoes):
				'''
				Here we are getting a list of 4 possible rotation states of the current polyomino
				all translated as if the bottom-left is at origin
				'''
				validationList = getValidationList(powerPolyomino.updatedPolyominoes[index])
				'''
				We compare this to every other polyomino in the updatedPolyominoes
				of the current Polyomino to remove different rotation states of the
				same Polyomino.
				'''
				for validator in validationList:
					powerPolyomino.updatedPolyominoes = removeByValidator(validator, powerPolyomino.updatedPolyominoes)
				index+=1

			# Adding the updatedPOlyomino list which is the next stage to nextPolyominoes
			nextPolyominoes += powerPolyomino.updatedPolyominoes
		# Removal of Duplicates
		nextPolyominoes = removeDuplicates(nextPolyominoes)
		# Resetting Current Polyominoes with the Next Polyominoes
		currentPolyominoes = [PowerPolyomino(polyomino.listOfCells) for polyomino in nextPolyominoes]
		nextPolyominoes = []

		#Moving to the next iteratoion


	# Returning all one sided polyominoes of size n
	return [BasePolyomino(powerPolyomino.listOfCells) for powerPolyomino in currentPolyominoes]

x = enumeratePolyominoes(n := int(input("Enter N: ")))