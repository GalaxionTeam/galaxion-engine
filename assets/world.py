from room import Room

class World:
	def __init__(self, x_dimension = 1, y_dimension = 1):
		self.grid = [[Room() for i in range(x_dimension)] for j in range(y_dimension)]
