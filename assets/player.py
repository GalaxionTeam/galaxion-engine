from assets.room import Room

# Class that holds player info
class Player:
	def __init__(self, world = None, items = None):
		self.room = world.grid[0][0]
		if items is None:
			items = []
		self.items = items
