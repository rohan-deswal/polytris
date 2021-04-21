import pyglet
from gameBoard import *
from polyomino import *
from pyglet.window.key import *

n = 4 #the 'n' in n-tris

width = 600
height = 600

window = pyglet.window.Window(width, height, caption = 'Tetris')
batch = pyglet.graphics.Batch()

# cell = Cell([window.width//2, window.height//2], grid, (255,0,0))

gameBoard = GameBoard((0, 0), (width, height), 4)
polyomino = Polyomino(n, 5, 10, width//20)
# def draw_label(text, x, y, font_size):
# 	label = pyglet.text.Label("Hello, World!!",
# 					   font_name="Times New Roman",
# 					   font_size=font_size,
# 					   x=x, y=y, 
# 					   anchor_x='center', 
# 					   anchor_y='center')
# 	label.draw()
@window.event
def on_key_press(symbol,modifiers):
	if symbol == LEFT:
		polyomino.update(-1,0)
	elif symbol == RIGHT:
		polyomino.update(1,0)
	if symbol == UP:
		polyomino.rotate('c')
	elif symbol == SPACE:
		polyomino.rotate('a')


@window.event
def on_draw():
	pyglet.gl.glClearColor(0,0,0,1)
	window.clear()
	gameBoard.draw_hold(lambda x, y:None)
	gameBoard.draw_playing_area(lambda x, y:None)
	gameBoard.draw_preview(lambda x, y:None)
	polyomino.draw()

@window.event
def update(dt):
	# polyomino.update(0,-1)
	pass

pyglet.clock.schedule(update)
pyglet.app.run()