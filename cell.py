from pyglet import shapes

class Cell:

	def __init__(self, position):
		self.position = position

	def draw(self, scale, wl, bottom):
		shapes.BorderedRectangle((self.position[0] + wl)*scale, (self.position[1] + bottom)*scale,
									  scale, scale, 1,
									  (150, 150, 150),(50, 50, 50)).draw()

	def update(self, dt, vx, vy):
		self.position[0] += vx*dt
		self.position[1] += vy*dt