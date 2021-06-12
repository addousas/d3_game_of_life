
class Cell:
	def __init__(self, id_x, id_y):
		self.curr_state = False
		self.next_state = False
		self.id_x = id_x
		self.id_y = id_y
		self.pair = (id_x,id_y)

class Grid:
	def __init__(self, rows, cols):
		self.grid = [[0]*cols]*rows
		self.grid_cpy = [[0]*cols]*rows
		self.rows = rows
		self.cols = cols

# #If a cell is alive, and has less than 2 living neighbors, then it dies.
# If a cell is alive, and has 3 or 2 living neighbors, then it survives.
# If a cell is alive, and has more than 3 neighbors, then it dies.
# If a cell is dead, and has 3 neighbors, then it becomes alive.
	def create(self):
		for col_id in range(self.cols):
			for row_id in range(self.rows):
				cell = Cell(col_id,row_id)
				self.grid[col_id][row_id] = cell

	def evaluate(self):
		# corner case 
		# col: 0 or col: cols - 1
		# row: 0 or row: rows - 1
		for col_id in range(self.cols):
			for row_id in range(self.rows):
				neighbors = []
				cell = self.grid[col_id][row_id]
				# self.get_neighbors()

	def get_neighbors(self,row_id,col_id):
			neighbors = []
			cell = self.grid[col_id][row_id]
			neighbors.append(self.grid[col_id  % self.cols ][(row_id + 1) % self.rows].pair)
			neighbors.append(self.grid[col_id  % self.cols ][(row_id  - 1) % self.rows].pair)
			
			neighbors.append(self.grid[(col_id  + 1) % self.cols ][row_id % self.rows].pair)
			neighbors.append(self.grid[(col_id   -1) % self.cols ][row_id % self.rows].pair)
			neighbors.append(self.grid[(col_id  + 1) % self.cols ][(row_id + 1) % self.rows].pair)
			neighbors.append(self.grid[(col_id  + 1) % self.cols ][(row_id  - 1)% self.rows].pair)
			neighbors.append(self.grid[(col_id  - 1) % self.cols ][(row_id + 1) % self.rows].pair)
			neighbors.append(self.grid[(col_id  - 1)% self.cols ][(row_id - 1)% self.rows].pair)
			return neighbors



				

	def show(self):
		pass

test = Grid(3,3)
test.create()
example = test.get_neighbors(1,1)
print (example)

