<<<<<<< HEAD
from assets.room import Room
from assets.item import Item

=======
import code
>>>>>>> 35d38cb9c26e12f6a65c7b83fb6e8d060ed3ba43
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
				print("Command not recognized")
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
				# Should implement an error code here to make this easier
				#if a.debug == "NO INPUT":
				#	print("You didn't say what to look at!")
				#elif type(a.args[0]) is Room:
				#	room = a.args[0]
				#	print("You are in: " + room.name)
				#	print("You are at: ({}, {})".format(room.x, room.y))
				#	# Prints the Room description
				#	print(a.message)
				# Gotta be a better way of checking this
				#elif a.args.pop() == 'ITEMS':
				#	# Prints "Following items in room:" message
				#	print(a.message)
				#	for item in a.args:
				#		print(item)
				#print(a.room.description)
				print("Player located at " + a.message)
				if len(a.args) > 0:
					print("Items in room: ")
					for b in a.args:
						print(b.name +  "\n" + b.location_desc)
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
             		                   code.DELETE: Delete,
					   code.EROOM : Edit_Room,
					   code.EITEM : Edit_Item,
					   }
			options[a.code]()
