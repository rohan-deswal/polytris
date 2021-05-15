import numpy as np

'''
This is the minimal class that defines a Polyomino 
'''
class BasePolyomino:
	def __init__(self,listOfCells):
		self.listOfCells = np.array([cell for cell in listOfCells])
