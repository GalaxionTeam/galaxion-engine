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
				print(a.message)
			def South():
				print(a.message)
			def East():
				print(a.message)
			def West():
				print(a.message)
			def Look():
				print(a.message)
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
				print("The pieces of the ship you need to fix it aren't likely to have fallen this far away.")
			def Create():
				print(a.message + " created")
			def Save():
				print("Saved")
			def Load():
				print("Loaded")
			def Delete():
				print(a.message + " deleted")
			def Add_Task():
				print("Task added")
			def Create_Use():
				print("Use created")
			def Remove_Task():
				print("Task removed")
			def Delete_Use():
				print("Use deleted")
			def Use():
				print(a.message)
			def Edit_Room():
				print("Room Edited")
			def Edit_Use():
				print("Use Edited")
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
					   code.RTAS : Remove_Task,
					   code.EUSE : Edit_Use,
					   code.DROP : Drop,
					   code.OUT : Out,
					   code.DUSE : Delete_Use,
					   code.CREATE: Create,
					   code.USE : Use,
					   code.SAVE : Save,
					   code.LOAD : Load,
             		   code.DELETE: Delete,
             		   code.ATAS : Add_Task,
             		   code.CUSE : Create_Use,
					   code.EROOM : Edit_Room,
					   code.EITEM : Edit_Item,
					   code.LOOKITEM : Look_Item,
					   }
			options[a.code]()
