import pyglet
from gameBoard import *
from pyglet.window.key import *
from time import time

n = 4 #the 'n' in n-tris
width = 900
height = 600

board_size = (20, 20)

window = pyglet.window.Window(width, height, caption = 'Polytris')
batch = pyglet.graphics.Batch()
keys = KeyStateHandler()

gameBoard = GameBoard((0, 0), (width, height), n, board_size)

@window.event
def on_key_press(symbol,modifiers):
	gameBoard.event_handler(symbol, modifiers)

@window.event
def on_key_release(symbol,modifiers):
	gameBoard.event_handler(symbol, modifiers, key_release=True)

@window.event
def on_draw():
	pyglet.gl.glClearColor(0,0,0,1)
	window.clear()
	gameBoard.draw_hold()
	gameBoard.draw_playing_area()
	gameBoard.draw_preview()

@window.event
def update(dt):
	gameBoard.update(window, keys)

pyglet.clock.schedule(update)
pyglet.app.run()