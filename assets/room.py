from coordinate import Coordinate

class Room:
	def __init__(self, x_dimension = 1, y_dimension = 1):
		self.grid = [[Coordinate(i,j) for i in range(x_dimension)] for j in range(y_dimension)]

if __name__ == "__main__":
	
	test = Room(5,5)
	for i in range(5):
		for j in range(5):
			print(test.grid[i][j].x_location)
			print(test.grid[i][j].y_location)
			print()