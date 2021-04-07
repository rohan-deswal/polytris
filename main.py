import pyglet
from gameBoard import *

n = 4 #the 'n' in n-tris

width = 600
height = 600

window = pyglet.window.Window(width, height, caption = 'Tetris')
batch = pyglet.graphics.Batch()

# cell = Cell([window.width//2, window.height//2], grid, (255,0,0))

gameBoard = GameBoard((0, 0), (width, height), 4)

# def draw_label(text, x, y, font_size):
# 	label = pyglet.text.Label("Hello, World!!",
# 					   font_name="Times New Roman",
# 					   font_size=font_size,
# 					   x=x, y=y, 
# 					   anchor_x='center', 
# 					   anchor_y='center')
# 	label.draw()

@window.event
def on_draw():
	pyglet.gl.glClearColor(0,0,0,1)
	window.clear()
	gameBoard.draw_hold(lambda x, y, b:None)
	gameBoard.draw_playing_area(lambda x, y, b:None)
	gameBoard.draw_preview(lambda x, y, b:None)


# pyglet.clock.schedule(update)
pyglet.app.run()