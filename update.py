from message import Message
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
				mess.code = 0
			def North():
				if pla.room.y == len(world.grid[0]) - 1:
					mess.code = 9
				else:
					mess.code = 1
					pla.room = world.grid[pla.room.x][pla.room.y + 1]
			def South():
				if pla.room.y == 0:
					mess.code = 9
				else:
					mess.code = 2
					pla.room = world.grid[pla.room.x][pla.room.y - 1]
			def East():
				if pla.room.x == len(world.grid) - 1:
					mess.code = 9
				else:
					mess.code = 3
					pla.room = world.grid[pla.room.x + 1][pla.room.y]
			def West():
				if pla.room.x == 0:
					mess.code = 9
				else:
					mess.code = 4
					pla.room = world.grid[pla.room.x - 1][pla.room.y]
			def Look():
				mess.code = 5
				if a.args[0] == "ROOM":
					# Pops the Room into the output queue
					mess.args.append(pla.room)
					mess.message = pla.room.name
				# Assume the arg refers to an Item if args is non-empty
				elif a.args:
					item = a.args[0]
					mess.args.append(item)
					# Pops an Item into the output queue
					mess.message = [k for k,v in pla.room.items.items() if v.upper() == item].pop()
			def Inventory():
				mess.code = 6
				mess.args = pla.items
			def Select():
				mess.code = 0
				for b in pla.room.items:
					if a.message == b.name:
						pla.items.append(pla.room.items.pop(pla.room.items.index(b)))
						mess.code = 7
						mess.message = a.message
			def Drop():
				mess.code = 0
				for b in pla.items:
					if a.message == b.name:
						pla.room.items.append(pla.items.pop(pla.items.index(b)))
						mess.code = 8
						mess.message = a.message
			def Create():
				mess.code = 10
				mess.message = a.message
				pla.room.items.append(Item(a.message))

			options = {0 : err,
					   1 : North,
					   2 : South,
					   3 : East,
					   4 : West,
					   5 : Look,
					   6 : Inventory,
					   7 : Select,
					   8 : Drop,
					   10 : Create,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
