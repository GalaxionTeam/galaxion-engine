class Item:
	# Assign unique item IDs in the order that they're created
	_ID = 0

	def __init__(self, name = "", description = ""):
		self.name = name
		self.description = description
		self.ID = _ID + 1

	def __str__(self):
		return "{}: {}".format(self.name, self.description)