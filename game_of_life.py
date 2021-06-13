
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
i = 0
class Cell:
	def __init__(self, id_row, id_col, curr_state):
		self.curr_state = curr_state
		self.next_state = 0
		self.id_row = id_row
		self.id_col = id_col
		self.pair = (id_row,id_col)

class Grid:
	def __init__(self, rows, cols):
		self.grid = [[0]*cols for x in range(rows)] 
		self.rows = rows
		self.cols = cols

	def create(self):
		for row_id in range(self.rows):
			for  col_id in range(self.cols):
				cell = Cell(row_id,col_id,0)
				self.grid[row_id][col_id] = cell

# For a space that is populated:
# Each cell with one or no neighbors dies, as if by solitude.
# Each cell with four or more neighbors dies, as if by overpopulation.
# Each cell with two or three neighbors survives.
# For a space that is empty or unpopulated
# Each cell with three neighbors becomes populated.

	def evaluate(self):
		for row_id in range(self.rows):
			for col_id in range(self.cols):
				neighbors = []
				cell = self.grid[row_id][col_id]
				states = self.get_neighbors_status(row_id,col_id)
				if cell.curr_state:

					if states.count(255) <= 1:
						cell.next_state = 0
					elif states.count(255) >= 4:
						cell.next_state = 0
					elif states.count(255) == 2 or states.count == 3:
						cell.next_state = 255
                    	
				else:
					# if cell is dead
					if states.count(255) == 3:
						cell.next_state = 255
						#cell.curr_state = 255
				self.grid[row_id][col_id] = cell

	def update(self):
		for row_id in range(self.rows):
			for col_id in range(self.cols):
				cell = self.grid[row_id][col_id]
				cell.curr_state = cell.next_state
				self.grid[row_id][col_id] = cell

# update(frameNum, img, grid, N):

	def animate(self, frameNum, img):
		#print ('[info] get_imag', frame)

		self.evaluate()
		self.update()
		img_nu = [[0]*self.cols for x in range(self.rows)] 
		for i in range(self.rows):
			for j in range(self.cols):
				img_nu[i][j] = self.grid[i][j].curr_state
		
		img.set_data(img_nu)

		return img_nu

	def get_img(self):

		img_nu = [[0]*self.cols for x in range(self.rows)] 
		for i in range(self.rows):
			for j in range(self.cols):
				img_nu[i][j] = self.grid[i][j].curr_state
		print(img_nu)
		return img_nu

	def get_neighbors_status(self,row_id,col_id):
			neighbors = []
			cell = self.grid[row_id][col_id]

			neighbors.append(self.grid[(row_id + 1) % self.rows][col_id  % self.cols ].curr_state)
			neighbors.append(self.grid[(row_id  - 1) % self.rows][col_id  % self.cols ].curr_state)

			neighbors.append(self.grid[(row_id) % self.rows][(col_id + 1)  % self.cols ].curr_state)
			neighbors.append(self.grid[(row_id) % self.rows][(col_id - 1) % self.cols ].curr_state)
			

			neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id + 1) % self.cols ].curr_state)
			neighbors.append(self.grid[(row_id  - 1) % self.rows][(col_id  -1) % self.cols ].curr_state)
			
			neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id - 1)  % self.cols ].curr_state)
			neighbors.append(self.grid[(row_id - 1) % self.rows][(col_id + 1) % self.cols ].curr_state)

			return neighbors
	
	def _get_neighbors_check(self,row_id,col_id):
			neighbors = []
			cell = self.grid[row_id][col_id]

			neighbors.append(self.grid[(row_id + 1) % self.rows][col_id  % self.cols ].pair)
			neighbors.append(self.grid[(row_id  - 1) % self.rows][col_id  % self.cols ].pair)

			neighbors.append(self.grid[(row_id) % self.rows][(col_id + 1)  % self.cols ].pair)
			neighbors.append(self.grid[(row_id) % self.rows][(col_id - 1) % self.cols ].pair)
			

			neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id + 1) % self.cols ].pair)
			neighbors.append(self.grid[(row_id  - 1) % self.rows][(col_id  -1) % self.cols ].pair)
			
			neighbors.append(self.grid[(row_id + 1) % self.rows][(col_id - 1)  % self.cols ].pair)
			neighbors.append(self.grid[(row_id - 1) % self.rows][(col_id + 1) % self.cols ].pair)

			return neighbors
# create line
	def creat_case1(self):
		self.grid[0][0] = Cell(0,0,255)
		self.grid[0][1] = Cell(0,1,255)
		self.grid[0][2] = Cell(0,2,255)
		self.grid[1][0] = Cell(1,0,0)
		self.grid[1][1] = Cell(1,1,0)
		self.grid[1][2] = Cell(1,2,0)
		self.grid[2][0] = Cell(2,0,0)
		self.grid[2][1] = Cell(2,1,0)
		self.grid[2][2] = Cell(2,2,0)

	def creat_case2(self,x_offset, y_offset):
		self.grid[0 + x_offset][1 + y_offset] = Cell(0 + x_offset ,1 + y_offset,255)
		self.grid[1 + x_offset][2 + y_offset] = Cell(0 + x_offset,2 + y_offset,255)
		self.grid[2 + x_offset][0 + y_offset] = Cell(2 + x_offset,0 + y_offset,255)
		self.grid[2 + x_offset][1 + y_offset] = Cell(2 + x_offset,1 + y_offset,255)
		self.grid[2 + x_offset][2 + y_offset] = Cell(2 + x_offset,2 +y_offset,255)


	def creat_case3(self,x_offset, y_offset):
		
		self.grid[1 + x_offset][1 + y_offset] = Cell(1 + x_offset,1 + y_offset,255)
		self.grid[2 + x_offset][0 + y_offset] = Cell(2 + x_offset,0 + y_offset,255)
		self.grid[2 + x_offset][1 + y_offset] = Cell(2 + x_offset,1 + y_offset,255)
		self.grid[2 + x_offset][2 + y_offset] = Cell(2 + x_offset,2 +y_offset,255)



test = Grid(50,50)
test.create()
test.creat_case3(25,25)

ny = test.get_img()



fig, ax = plt.subplots()
img = ax.imshow(ny, interpolation='nearest')
#                                            
ani = animation.FuncAnimation(fig, test.animate, fargs=(img,),
                              frames = 100,
                              interval=500,
                              save_count=50)
plt.show()