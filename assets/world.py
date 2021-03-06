from assets.room import Room

class World:
	def __init__(self, x_dimension = 1, y_dimension = 1):
		self.grid = [[Room(j, i) for i in range(y_dimension)] for j in range(x_dimension)]

	def copy(self, x_dimension = 1, y_dimension = 1):
		self.grid = [[Room(j, i) for i in range(y_dimension)] for j in range(x_dimension)]
