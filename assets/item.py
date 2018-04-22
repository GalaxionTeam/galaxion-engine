class Item:
	# Assign unique item IDs in the order that they're created
	class_ID = 0

	def __init__(self, name = "", description = "", location_desc = "", ID = 0):
		self.name = name
		self.description = description
		self.location_desc = location_desc
		self.ID = Item.class_ID
		Item.class_ID += 1

	def __str__(self):
		return "{}: {}".format(self.name, self.description)

