import numpy as np

from pyglet import shapes

class Hands:
	"""
	Manages hand coordinates 
	is responsible for drawing, processing and converting to 
	useful data
	"""

	#TODO 

	def __init__(self, arena_shape, arr_shape = (21, 3)):
		self.arena_shape = arena_shape
		self.hand_coords = np.zeros(shape=arr_shape, np.float16)


	def update(self, hand_coords):
		"""
		Updates hands coords
		"""
		#TODO
		self.hand_coords = hand_coords

	def draw(self):
		if not self.hand_coords.any():
			return

		for coords in self.hand_coords:
			x, y, z = coords
			x *= self.arena_shape[0]
			y *= self.arena_shape[1]
			z *= 20

			shapes.Circle(x, y, z).draw()
