class Room:
	def __init__(self, x = 0, y = 0, name = "", items = [], description = ""):
		self.items = items
		self.name = " (" + repr(x) + ", " + repr(y) + ")"
		self.description = description
		self.x = x
		self.y = y
