from pyglet import shapes
from time import time
from pyglet.window.key import *
from random import shuffle

from polyomino import *
from pile import *
from polyominoEnumeration.polyominoEnumerate import *

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

		#Timing variables for velocity, tuck and DAS
		self.velocity = -3
		self.begin = time()
		self.delayedAutoShiftRate = 1
		self.polyominoTuckDelay = 1
		self.polyominoTuckDelayCounter = 0
		self.pieceIsDown = False

		#generate a of all possible polyominoes
		self.polyominoList = list(enumerate(enumeratePolyominoes(n)))
		self.no_of_polyomino = len(self.polyominoList)

		self.bag = list(range(self.no_of_polyomino))
		self.next_bag = self.bag.copy()
		# shuffle(self.bag)
		# shuffle(self.next_bag)
		self.current_piece_counter = -1

		self.held_piece = None

		#Handles the current falling polyomino, its position, collision, rotation, etc
		self.polyomino = Polyomino(n, self.startX, self.startY, self.grid, n+1, \
			self.game_board_size[0] - (n+1), self.velocity, self.no_of_polyomino, self.next_piece())

		#Handles the pile accumulated, line clearing, collision with current polyomino, etc
		self.pile = Pile(self.grid, self.game_board_size[1], n+1, self.game_board_size[0] - (n+1))

	def draw_hold(self):
		'''Draws the polynimo holding chamber, by default the box is 4 grid widths wide
		   this value is kind of hard coded, but it will be visually appealing 
		   Pieces have to be shrunk to display'''

		hold_size = (self.n)*self.grid
		hold_x = self.init_x + self.grid//2
		hold_y = self.init_y + self.height - hold_size - self.grid//2
		shapes.Rectangle(hold_x, hold_y, hold_size, hold_size, (255,255,255)).draw()

		if self.held_piece is not None:
			held_piece_shapeCoords = self.held_piece[1].listOfCells
			held_piece_type = self.held_piece[0]
			for point in held_piece_shapeCoords:
				piece_x = point[0]*self.grid + hold_x
				piece_y = point[1]*self.grid + hold_y
				shapes.BorderedRectangle(piece_x, piece_y,
										  self.grid, self.grid, 1,
										  type_color(held_piece_type, self.no_of_polyomino),(0,0,0)).draw()

	def draw_playing_area(self):
		'''Draws the actual palying area, dimensions are hard coded to be 10x20 following the 
		   standard tetris board'''

		play_x = self.init_x + (self.n+1)*self.grid
		play_y = self.init_y
		play_width = self.grid * (self.game_board_size[0]-2*(self.n+1))
		play_height = self.grid * self.game_board_size[1]
		shapes.Rectangle(play_x, play_y, play_width, play_height, (255,255,255)).draw()

		self.polyomino.draw()
		self.pile.draw()

	def draw_preview(self):
		'''Draws the next piece, currently the number of pieces that can be displayed is 1
		   But it can be easily changed to any value'''

		preview_size = (self.n)*self.grid
		preview_x = self.init_x + ((self.game_board_size[0] - (self.n+1))*2 + 1)*self.grid//2
		preview_y = self.init_y + self.height - preview_size - self.grid//2
		shapes.Rectangle(preview_x, preview_y, preview_size, preview_size, (255,255,255)).draw()
		
		next_piece = self.next_piece(view = True)
		next_piece_shapeCoords = next_piece[1].listOfCells
		next_piece_type = next_piece[0]
		for point in next_piece_shapeCoords:
			piece_x = point[0]*self.grid + preview_x
			piece_y = point[1]*self.grid + preview_y
			shapes.BorderedRectangle(piece_x, piece_y,
									  self.grid, self.grid, 1,
									  type_color(next_piece_type, self.no_of_polyomino),(0,0,0)).draw()

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
			elif symbol == LSHIFT:
				self.polyomino.reset(self.startX, self.startY, self.hold_piece())
		else:
			if symbol == LEFT or symbol == RIGHT:
			    self.polyomino.setxdir(0)

	def next_piece(self, view = False):
		if view:
			try:
				return self.polyominoList[self.bag[self.current_piece_counter + 1]]
			except IndexError:
				return self.polyominoList[self.next_bag[0]]

		self.current_piece_counter = (self.current_piece_counter + 1) % len(self.bag)
		piece_index = self.bag[self.current_piece_counter]

		if self.current_piece_counter == 0:
			self.bag = self.next_bag.copy()
			shuffle(self.next_bag)

		return self.polyominoList[piece_index]

	def hold_piece(self):
		if self.held_piece == None:
			self.held_piece = self.polyomino.polyomino_piece
			return self.next_piece()

		to_be_returned_piece = self.held_piece
		self.held_piece = self.polyomino.polyomino_piece
		return to_be_returned_piece