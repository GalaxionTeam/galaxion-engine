from message import Message
import code
from assets.item import Item
from assets.room import Room

# Class that updates game stat
class Update:
	def __init__(self):
		# List of tasks
		self.messages = []

	def update(self, pla, out, world):

		# Loop that terminates once task list is empty
		while len(self.messages) > 0:

			mess = Message()
			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				mess.code = code.ERR
				mess.message = a.message
			def North():
				if pla.room.y == len(world.grid[0]) - 1:
					mess.code = code.OUT
				else:
					mess.code = code.NORTH
					pla.room = world.grid[pla.room.x][pla.room.y + 1]
			def South():
				if pla.room.y == code.SOUTH:
					mess.code = code.OUT
				else:
					mess.code = code.SOUTH
					pla.room = world.grid[pla.room.x][pla.room.y - 1]
			def East():
				if pla.room.x == len(world.grid) - 1:
					mess.code = code.OUT
				else:
					mess.code = code.EAST
					pla.room = world.grid[pla.room.x + 1][pla.room.y]
			def West():
				if pla.room.x == 0:
					mess.code = code.OUT
				else:
					mess.code = code.WEST
					pla.room = world.grid[pla.room.x - 1][pla.room.y]
			def Look():
				mess.code = code.LOOK
				mess.message = pla.room.name
				mess.args = pla.room.items
			def Look_Item():
				mess.code = code.ERR
				for b in pla.room.items:
					if a.message == b.name.upper():
						mess.code = code.LOOKITEM
						mess.args.append(b)
			def Inventory():
				mess.code = code.INVENTORY
				mess.args = pla.items
			def Select():
				mess.code = code.ERR
				for b in pla.room.items:
					if a.message == b.name.upper():
						pla.items.append(pla.room.items.pop(pla.room.items.index(b)))
						mess.code = code.SELECT
						mess.message = a.message
			def Drop():
				mess.code = code.DROP
				for b in pla.items:
					if a.message == b.name.upper():
						pla.room.items.append(pla.items.pop(pla.items.index(b)))
						mess.code = code.DROP
						mess.message = a.message
			def Create():
				mess.code = code.CREATE
				mess.message = a.message
				pla.room.items.append(Item(a.message))
				#print(str(pla.room.items))
			def Delete():
				mess.code = code.DELETE
				mess.message = a.message
				for b in pla.room.items:
					if a.message == b.name.upper():
						pla.room.items.pop(pla.room.items.index(b))
						#print(str(pla.room.items))

			def Edit_Room():
				mess.code = code.EROOM
				if a.args[0].upper() == "NAME":
					pla.room.name = a.args[1]
				elif a.args[0].upper() == "DESCRIPTION":
					pla.room.description = a.args[1]
				else:
					mess.code = code.ERR

			def Edit_Item():
				mess.code = code.EITEM
				inside = False
				loc = 0
				for i in range(len(pla.room.items)):
					if (a.args[0].upper() == pla.room.items[i].name.upper()):
						inside = True
						loc = i
				if inside:
					if a.args[1].upper() == "NAME":
						pla.room.items[loc].name = a.args[2]
					elif a.args[1].upper() == "DESCRIPTION":
						pla.room.items[loc].description = a.args[2]
					elif a.args[1].upper() == "LOCATION DESCRIPTION":
						pla.room.items[loc].location_desc = a.args[2]
					else:
						mess.code = code.ERR
				else:
					mess.code = code.ERR

			options = {code.ERR : err,
					   code.NORTH : North,
					   code.SOUTH : South,
					   code.EAST : East,
					   code.WEST : West,
					   code.LOOK : Look,
					   code.INVENTORY : Inventory,
					   code.SELECT : Select,
					   code.DROP : Drop,
					   code.CREATE : Create,
             		   code.DELETE : Delete,
					   code.EROOM : Edit_Room,
					   code.EITEM : Edit_Item,
					   code.LOOKITEM : Look_Item,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
