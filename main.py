import pyglet
from gameBoard import *
from polyomino import *
from pile import *
from pyglet.window.key import *
from time import time

n = 4 #the 'n' in n-tris
startX,startY = 5,21
width = 600
height = 600

window = pyglet.window.Window(width, height, caption = 'Tetris')
batch = pyglet.graphics.Batch()
keys = KeyStateHandler()

begin = time()
delayedAutoShiftRate = 1
polyominoTuckDelay = 2
polyominoTuckDelayCounter = 0
pieceIsDown = False

# cell = Cell([window.width//2, window.height//2], grid, (255,0,0))

gameBoard = GameBoard((0, 0), (width, height), 4)
polyomino = Polyomino(n, startX, startY, width//20,5,15)
pile = Pile(width//20, 5, 15)

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
	global begin
	if symbol == LEFT:
		if pile.verifyXMotion(polyomino.shapeCoords,-1):
			polyomino.setxdir(-1)
			begin = time()
	elif symbol == RIGHT:
		if pile.verifyXMotion(polyomino.shapeCoords,1):
			polyomino.setxdir(1)
			begin = time()
	elif symbol == UP:
		polyomino.rotate('c')
	elif symbol == LCTRL:
		polyomino.rotate('a')
	elif symbol == SPACE:
		pile.hardDrop(polyomino.shapeCoords)
		polyomino.reset(startX, startY)

@window.event
def on_key_release(symbol,modifiers):
	if symbol == LEFT or symbol == RIGHT:
	    polyomino.setxdir(0)

@window.event
def on_draw():
	pyglet.gl.glClearColor(0,0,0,1)
	window.clear()
	gameBoard.draw_hold(lambda x, y:None)
	gameBoard.draw_playing_area(lambda x, y:None)
	gameBoard.draw_preview(lambda x, y:None)
	polyomino.draw()
	pile.draw()

@window.event
def update(dt):
	global begin,polyominoTuckDelayCounter,polyominoTuckDelay,pieceIsDown	

	if pile.collidePolyomino(polyomino.shapeCoords):
		if not pieceIsDown:
			polyominoTuckDelayCounter = time()
		pile.update()
		polyomino.update(0)
		pieceIsDown = True
	else:
		polyomino.update(-1)
		pieceIsDown = False

	if time() - polyominoTuckDelayCounter >= polyominoTuckDelay and pieceIsDown:
		pile.addPolyomino(polyomino.shapeCoords)
		polyomino.reset(startX,startY)
		pieceIsDown = False
		
	if time() - begin > abs(delayedAutoShiftRate - (time()-begin)):
		window.push_handlers(keys)
		if keys[LEFT]:
			if pile.verifyXMotion(polyomino.shapeCoords,-1):
				polyomino.setxdir(-1)
		elif keys[RIGHT]:
			if pile.verifyXMotion(polyomino.shapeCoords,1):
				polyomino.setxdir(1)

pyglet.clock.schedule(update)
pyglet.app.run()