
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class Cell:
	def __init__(self, id_row, id_col, curr_state):
		self.curr_state = curr_state
		self.next_state = None
		self.id_row = id_row
		self.id_col = id_col

class Grid:
	def __init__(self, rows, cols):
		self.grid = [[0]*cols for x in range(rows)] 
		self.rows = rows
		self.cols = cols

	def create(self):
		"""
		create:  create a grid rows x cols and initialize with 0 
		"""
		for row_id in range(self.rows):
			for  col_id in range(self.cols):
				cell = Cell(row_id,col_id,0) # [0,255][random.randint(0,1)]
				self.grid[row_id][col_id] = cell

	def evaluate(self):
		"""
		evaluate: visit every cell and evaluate accoording John Conway's Game of life rules
		Rules

		For a space that is populated:
		Each cell with one or no neighbors dies, as if by solitude.
		Each cell with four or more neighbors dies, as if by overpopulation.
		Each cell with two or three neighbors survives.

		For a space that is empty or unpopulated
		Each cell with three neighbors becomes populated.

		"""
		for row_id in range(self.rows):
			for col_id in range(self.cols):

				cell = self.grid[row_id][col_id]
				states = self.get_neighbors_status(row_id,col_id)
				
				if cell.curr_state == 255:

					if states.count(255) <= 1:
						cell.next_state = 0
					elif states.count(255) >= 4:
						cell.next_state = 0
					elif states.count(255) == 2 or states.count == 3:
						cell.next_state = 255
					else:
						cell.next_state = None
                    	
				else:
					# if cell is dead
					if states.count(255) == 3:
						cell.next_state = 255
					else:
						cell.next_state = None
				self.grid[row_id][col_id] = cell

	def update(self):
		"""
		update: visit every cell, assign cell's next_state to curr_state if needed 
		"""
		for row_id in range(self.rows):
			for col_id in range(self.cols):
				
				cell = self.grid[row_id][col_id]
				if cell.next_state != None:
					cell.curr_state = cell.next_state
					
					self.grid[row_id][col_id] = cell
					#

	def animate(self, frameNum, img):
		"""
		animate:  The function to call at each frame. The first argument will be the next value in frames. 
		Any additional positional arguments can be supplied via the fargs parameter.
		"""
		print('[info] animate', frameNum)
		self.evaluate()
		self.update()
		img_nu = [[0]*self.cols for x in range(self.rows)] 
		for i in range(self.rows):
			for j in range(self.cols):
				img_nu[i][j] = self.grid[i][j].curr_state
		
		img.set_data(img_nu)
		return img_nu

	def get_img(self):
		"""
		get_img: returns an array of arrays that represents the current state of the grid
		"""
		img_nu = [[0]*self.cols for x in range(self.rows)] 
		for i in range(self.rows):
			for j in range(self.cols):
				img_nu[i][j] = self.grid[i][j].curr_state
		##
		return img_nu

	def get_neighbors_status(self,row_id,col_id):
		neighbors = []

		neighbors.append(self.grid[(row_id) % self.rows][(col_id - 1) % self.cols].curr_state)
		neighbors.append(self.grid[(row_id) % self.rows][(col_id + 1) % self.cols].curr_state)

		neighbors.append(self.grid[(row_id - 1) % self.rows][(col_id) % self.cols].curr_state)
		neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id) % self.cols].curr_state)

		neighbors.append(self.grid[(row_id - 1) % self.rows][(col_id - 1) % self.cols].curr_state)
		neighbors.append(self.grid[(row_id - 1) % self.rows][(col_id + 1) % self.cols].curr_state)

		neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id - 1) % self.cols].curr_state)
		neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id + 1) % self.cols].curr_state)

		return neighbors
	
	def creat_case1(self, x_offset, y_offset):

		self.grid[0 + x_offset][0 + y_offset] = Cell(0 + x_offset,0 + y_offset,255)
		self.grid[0 + x_offset][1 + y_offset] = Cell(0 + x_offset,1 + y_offset,255)
		self.grid[0 + x_offset][2 + y_offset] = Cell(0 + x_offset,2 + y_offset,255)

	def creat_case2(self,x_offset, y_offset):

		self.grid[0 + x_offset][1 + y_offset] = Cell(0 + x_offset ,1 + y_offset,255)
		self.grid[1 + x_offset][2 + y_offset] = Cell(1 + x_offset,2 + y_offset,255)
		self.grid[2 + x_offset][0 + y_offset] = Cell(2 + x_offset,0 + y_offset,255)
		self.grid[2 + x_offset][1 + y_offset] = Cell(2 + x_offset,1 + y_offset,255)
		self.grid[2 + x_offset][2 + y_offset] = Cell(2 + x_offset,2 +y_offset,255)

	def creat_case3(self,x_offset, y_offset):
		# - x -
		# x x x
		#
		self.grid[1 + x_offset][1 + y_offset] = Cell(1 + x_offset,1 + y_offset,255)
		self.grid[2 + x_offset][0 + y_offset] = Cell(2 + x_offset,0 + y_offset,255)
		self.grid[2 + x_offset][1 + y_offset] = Cell(2 + x_offset,1 + y_offset,255)
		self.grid[2 + x_offset][2 + y_offset] = Cell(2 + x_offset,2 + y_offset,255)

	def create_random(self):
		"""
		create_random:  create a grid rows x cols and initialize with 0 
		"""
		for row_id in range(self.rows):
			for  col_id in range(self.cols):
				cell = Cell(row_id,col_id,[0,255][random.randint(0,1)]) # [0,255][random.randint(0,1)]
				self.grid[row_id][col_id] = cell
	
	
	def creat_pattern(self):
		pass






game_of_life = Grid(100,100)
game_of_life.create()
game_of_life.create_random()

image = game_of_life.get_img()
game_of_life.get_neighbors_status(0,0)
fig, ax = plt.subplots()
img = ax.imshow(image, interpolation='nearest')
                                           
ani = animation.FuncAnimation(fig, game_of_life.animate, fargs=(img,),
                              frames = 1000,
                              interval=50,
                              save_count=1000)

ani.save('game_of_life.mp4')#, fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()

