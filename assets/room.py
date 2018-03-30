class Room:
	def __init__(self, x = 0, y = 0, name = "", items = None, description = ""):
		if items is None:
			items = {}
		self.items = items
		self.name = " (" + str(x) + ", " + str(y) + ")"
		self.description = description
		self.x = x
		self.y = y
