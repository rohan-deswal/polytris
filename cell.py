from pyglet import shapes

class Cell:

	def __init__(self, position, size, color):
		self.position = position
		self.size = size
		self.color = color

	def draw(self):
		shapes.Rectangle(self.position[0], self.position[1], self.size, self.size, self.color).draw()

	def update(self, dt, vx, vy):
		self.position[0] += vx*dt
		self.position[1] += vy*dt