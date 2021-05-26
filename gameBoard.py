from pyglet import shapes
from time import time
from pyglet.window.key import *
from random import shuffle

from polyomino import *
from pile_redesign import *
from polyominoEnumerate import *
from basePolyomino import *

def width_height(bottom_left, top_right, game_board_size):
	'''Maintains the required aspect ratio of the board and changes the provided top_right point
	   This is done to properly accomodate the preview polynimo and the hold chamber'''

	grid_width_wise = (top_right[0] - bottom_left[0])//game_board_size[0]
	grid_height_wise = (top_right[1] - bottom_left[1])//game_board_size[1]

	if grid_width_wise * game_board_size[1] < top_right[1] - bottom_left[1]:
		return (top_right[0] - bottom_left[0], grid_width_wise * game_board_size[1], grid_width_wise)
	else:
		return (grid_height_wise * game_board_size[0], top_right[1] - bottom_left[1], grid_height_wise)

class GameBoard:
	'''GameBoard object manages the actual playing area
	   the polymino holding area and the upcoming polymino area'''

	def __init__(self, bottom_left, top_right, n, playing_area_size):
		'''Inititalizes the GameBoard object, can take any values for bottom_left and top_right coordinates
		   the top_right coordinate is modified to fit the aspect ratio of the gameBoard'''

		self.init_x = bottom_left[0]
		self.init_y = bottom_left[1]

		#Playing area grid size +n+1 for hold area and +n+1 for Preview area
		self.game_board_size = (n + 1 + playing_area_size[0] + n + 1, playing_area_size[1])

		self.width, self.height, self.grid = width_height(bottom_left, top_right, self.game_board_size)

		self.startX, self.startY = self.game_board_size[0]//2, self.game_board_size[1]

		self.n = n

		#Timing variables for tuck and DAS
		self.velocity = -1
		self.begin = time()
		self.delayedAutoShiftRate = 1
		self.polyominoTuckDelay = 1
		self.polyominoTuckDelayCounter = 0
		self.pieceIsDown = False

		#generate a of all possible polyominoes
		self.polyominoList = list(enumerate(enumeratePolyominoes(n)))
		self.bag = list(range(len(self.polyominoList)))*2
		self.current_piece_counter = 0

		self.no_of_polyomino = len(self.polyominoList)

		#Handles the current falling polyomino, its position, collision, rotation, etc
		self.polyomino = Polyomino(n, self.startX, self.startY, self.grid, n+1, \
			self.game_board_size[0] - (n+1), self.velocity, self.no_of_polyomino, self.next_piece())

		#Handles the pile accumulated, line clearing, collision with current polyomino, etc
		self.pile = Pile_redesign(self.grid, self.game_board_size[1], n+1, self.game_board_size[0] - (n+1))

	def draw_hold(self):
		'''Draws the polynimo holding chamber, by default the box is 4 grid widths wide
		   this value is kind of hard coded, but it will be visually appealing 
		   Pieces have to be shrunk to display

		   block_drawing_function represents the function to draw held blocks by the polynimo
		   class, the polynimo should be shrunk to properly fit in the hold area, no transformations 
		   are to be done by the polynimo class
		   all transformations are handled by the GameBoard class'''

		hold_size = (self.n)*self.grid
		hold_x = self.init_x + self.grid//2
		hold_y = self.init_y + self.height - hold_size - self.grid//2
		shapes.Rectangle(hold_x, hold_y, hold_size, hold_size, (255,255,255)).draw()

	def draw_playing_area(self):
		'''Draws the actual palying area, dimensions are hard coded to be 10x20 following the 
		   standard tetris board

		   block_drawing_function represents the drawing function of the polynimo that will be handled
		   by the polynimo class, the polynimo drawing functions should take in the x and y values for the
		   playing area and draw the pieces accordingly without any transformation
		   all transformations are handled by the GameBoard class'''

		play_x = self.init_x + (self.n+1)*self.grid
		play_y = self.init_y
		play_width = self.grid * (self.game_board_size[0]-2*(self.n+1))
		play_height = self.grid * self.game_board_size[1]
		shapes.Rectangle(play_x, play_y, play_width, play_height, (255,255,255)).draw()

		self.polyomino.draw()
		self.pile.draw()

	def draw_preview(self):
		'''Draws the next piece, currently the number of pieces that can be displayed is 1
		   But it can be easily changed to any value

		   block_drawing_function represents the function of polynimo class that will draw the
		   upcoming polynimos, pieces are to be shrunk to properly fit in the preview area
		   no transformations are to be done by the polynimo class
		   all transformations are handled by the GameBoard class'''

		preview_size = (self.n)*self.grid
		preview_x = self.init_x + ((self.game_board_size[0] - (self.n+1))*2 + 1)*self.grid//2
		preview_y = self.init_y + self.height - preview_size - self.grid//2
		shapes.Rectangle(preview_x, preview_y, preview_size, preview_size, (255,255,255)).draw()

	def update(self, window, keys):
		if self.pile.collidePolyomino(self.polyomino.shapeCoords):
			if not self.pieceIsDown:
				self.polyominoTuckDelayCounter = time()
			self.polyomino.update(0)
			self.pieceIsDown = True
		else:
			self.polyomino.update(-1)
			self.pieceIsDown = False

		if time() - self.polyominoTuckDelayCounter >= self.polyominoTuckDelay and self.pieceIsDown:
			self.pile.addToPile(self.polyomino.shapeCoords, self.polyomino.color)
			self.polyomino.reset(self.startX, self.startY, self.next_piece())
			self.pile.update()
			self.pieceIsDown = False

		if time() - self.begin > abs(self.delayedAutoShiftRate - (time()-self.begin)):
			window.push_handlers(keys)
			if keys[LEFT]:
				if self.pile.verifyXMotion(self.polyomino.shapeCoords,-1):
					self.polyomino.setxdir(-1)
			elif keys[RIGHT]:
				if self.pile.verifyXMotion(self.polyomino.shapeCoords,1):
					self.polyomino.setxdir(1)

	def event_handler(self, symbol, modifiers, key_release = False):
		if not key_release:	
			if symbol == LEFT:
				if self.pile.verifyXMotion(self.polyomino.shapeCoords,-1):
					self.polyomino.setxdir(-1)
					self.begin = time()
			elif symbol == RIGHT:
				if self.pile.verifyXMotion(self.polyomino.shapeCoords,1):
					self.polyomino.setxdir(1)
					self.begin = time()
			elif symbol == UP:
				self.polyomino.rotate('c')
			elif symbol == LCTRL:
				self.polyomino.rotate('a')
			elif symbol == SPACE:
				self.pile.hardDrop(self.polyomino.shapeCoords, self.polyomino.color)
				self.polyomino.reset(self.startX, self.startY, self.next_piece())
				self.pile.update()
		else:
			if symbol == LEFT or symbol == RIGHT:
			    self.polyomino.setxdir(0)

	def next_piece(self):
		piece_index = self.bag[self.current_piece_counter]
		self.current_piece_counter = (self.current_piece_counter + 1) % len(self.bag)
		
		if self.current_piece_counter == 0:
			shuffle(self.bag)

		return self.polyominoList[piece_index]