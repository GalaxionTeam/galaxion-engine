class Item:
	# Assign unique item IDs in the order that they're created
	_ID = 0

	def __init__(self, name = "", description = "", location_desc = ""):
		self.name = name
		self.description = description
		self.location_desc = location_desc
		self.ID = _ID + 1

	def __str__(self):
		return "{}: {}".format(self.name, self.description)

