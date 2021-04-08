import pyglet
from cell import *


grid = 30
window = pyglet.window.Window(20*grid,20*grid,caption = 'Tetris')

cell = Cell([window.width//2, window.height//2], grid, (255,0,0))
def draw_label(text, x, y, font_size):
	label = pyglet.text.Label("Hello, World!!",
					   font_name="Times New Roman",
					   font_size=font_size,
					   x=x, y=y, 
					   anchor_x='center', 
					   anchor_y='center')
	label.draw()

@window.event
def on_draw():
	pyglet.gl.glClearColor(0,0,0,1)
	window.clear()
	gameBoard.draw_hold(lambda x, y:None)
	gameBoard.draw_playing_area(lambda x, y:None)
	gameBoard.draw_preview(lambda x, y:None)

	pyglet.shapes.Rectangle(grid*4 + grid//2, 0, 10*grid, 20*grid, (255,255,255)).draw()

	cell.draw()

@window.event
def update(dt):
	cell.update(dt, 0, -grid)

pyglet.clock.schedule(update)
pyglet.app.run()