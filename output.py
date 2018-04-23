import code
# Class for game output
class Output:
	def __init__(self):
		# List of tasts
		self.messages = []

	def update(self):
		# Loop that terminates once task list is empty
		while len(self.messages) > 0:

			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				print(a.message)
				#I'm pretty sure we handle this case back in input
			def North():
				print("North 1 Space")
			def South():
				print("South 1 Space")
			def East():
				print("East 1 Space")
			def West():
				print("West 1 Space")
			def Look():
				print("Player located at " + a.message)
				if len(a.args) > 0:
					print("Items in room: ")
					for b in a.args:
						print(b.name +  "\n" + b.location_desc)
			def Look_Item():
				print(a.args[0].name + " " + a.args[0].description)
			def Inventory():
				if len(a.args) > 0:
					print("Items in inventory:")
					for b in a.args:
						print(b.name)
				else:
					print("Inventory empty")
			def Select():
				print(a.message + " selected")
			def Drop():
				print(a.message + " dropped")
			def Out():
				print("Out of Bounds")
			def Create():
				print(a.message + " created")
			def Save():
				print("Saved")
			def Load():
				print("Loaded")
			def Delete():
				print(a.message + " deleted")
			def Edit_Room():
				print("Room Edited")
			def Edit_Item():
				print("Item Edited")


			options = {code.ERR : err,
					   code.NORTH : North,
					   code.SOUTH : South,
					   code.EAST : East,
					   code.WEST : West,
					   code.LOOK : Look,
					   code.INVENTORY : Inventory,
					   code.SELECT : Select,
					   code.DROP : Drop,
					   code.OUT : Out,
					   code.CREATE: Create,
					   code.SAVE : Save,
					   code.LOAD : Load,
             		   code.DELETE: Delete,
					   code.EROOM : Edit_Room,
					   code.EITEM : Edit_Item,
					   code.LOOKITEM : Look_Item,
					   code.EXIT : Exit
					   }
			options[a.code]()
