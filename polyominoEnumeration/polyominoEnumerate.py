from powerPolyomino import PowerPolyomino
from basePolyomino import BasePolyomino
from validationHelp import *

def enumeratePolyominoes(n):

	currentPolyominoes = [PowerPolyomino([[0,0]])]
	nextPolyominoes = []
	for i in range(1,n-1):
		for powerPolyomino in currentPolyominoes:
			index = 0
			while index > len(powerPolyomino.updatedPolyominoes):
				validationList = getValidationList(powerPolyomino.updatedPolyominoes[index])
				for validator in validationList:
					powerPolyomino.updatedPolyominoes = removeByValidator(validator, powerPolyomino.updatedPolyominoes)
				index+=1

			nextPolyominoes += powerPolyomino.updatedPolyominoes

		nextPolyominoes = removeDuplicates(nextPolyominoes)
		currentPolyominoes = [PowerPolyomino(polyomino.listOfCells) for polyomino in nextPolyominoes]
		nextPolyominoes = []

	return [BasePolyomino(powerPolyomino.listOfCells) for powerPolyomino in currentPolyominoes]

x = enumeratePolyominoes(n := int(input("Enter N: ")))
print("List of Polyominoes")
for ele in x:
	printPoly(ele.listOfCells,n)
	a = input()