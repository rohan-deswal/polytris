from pyglet import shapes

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

	def __init__(self, bottom_left, top_right, n):
		'''Inititalizes the GameBoard object, can take any values for bottom_left and top_right coordinates
		   the top_right coordinate is modified to fit the aspect ratio of the gameBoard'''
		
		self.init_x = bottom_left[0]
		self.init_y = bottom_left[1]

		self.game_board_size = (10 + 10, 20) #Conventional 10x20 playing area for tetris and 10 width to accomoodate hold and preview

		self.width, self.height, self.grid = width_height(bottom_left, top_right, self.game_board_size)

		self.n = n

	def draw_hold(self, block_drawing_function, batch):
		'''Draws the polynimo holding chamber, by default the box is 4 grid widths wide
		   this value is kind of hard coded, but it will be visually appealing 
		   Pieces have to be shrunk to display

		   block_drawing_function represents the function to draw held blocks by the polynimo
		   class, the polynimo should be shrunk to properly fit in the hold area, no transformations 
		   are to be done by the polynimo class
		   all transformations are handled by the GameBoard class'''

		hold_size = 4*self.grid
		hold_x = self.init_x + self.grid//2
		hold_y = self.init_y + self.height - hold_size - self.grid//2
		shapes.Rectangle(hold_x, hold_y, hold_size, hold_size, (255,255,255)).draw()
		block_drawing_function(hold_x, hold_y, batch)

	def draw_playing_area(self, block_drawing_function, batch):
		'''Draws the actual palying area, dimensions are hard coded to be 10x20 following the 
		   standard tetris board

		   block_drawing_function represents the drawing function of the polynimo that will be handled
		   by the polynimo class, the polynimo drawing functions should take in the x and y values for the
		   playing area and draw the pieces accordingly without any transformation
		   all transformations are handled by the GameBoard class'''

		play_x = self.init_x + 5*self.grid
		play_y = self.init_y
		play_width = self.grid * 10
		play_height = self.grid * 20
		shapes.Rectangle(play_x, play_y, play_width, play_height, (255,255,255)).draw()

		block_drawing_function(play_x, play_y, batch)

	def draw_preview(self, block_drawing_function, batch):
		'''Draws the next piece, currently the number of pieces that can be displayed is 1
		   But it can be easily changed to any value

		   block_drawing_function represents the function of polynimo class that will draw the
		   upcoming polynimos, pieces are to be shrunk to properly fit in the preview area
		   no transformations are to be done by the polynimo class
		   all transformations are handled by the GameBoard class'''

		preview_size = 4*self.grid
		preview_x = self.init_x + 31*self.grid//2
		preview_y = self.init_y + self.height - preview_size - self.grid//2
		shapes.Rectangle(preview_x, preview_y, preview_size, preview_size, (255,255,255)).draw()
		block_drawing_function(preview_x, preview_y, batch)