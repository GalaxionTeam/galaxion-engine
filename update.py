from message import Message

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
				if pla.room.y == 0:
					mess.code = 6
				else:
					mess.code = 1
					pla.room = world.grid[pla.room.x][pla.room.y - 1]
			def South():
				if pla.room.y == len(world.grid[0]) - 1:
					mess.code = 6
				else:
					mess.code = 2
					pla.room = world.grid[pla.room.x][pla.room.y + 1]
			def East():
				if pla.room.x == len(world.grid) - 1:
					mess.code = 6
				else:
					mess.code = 3
					pla.room = world.grid[pla.room.x + 1][pla.room.y]
			def West():
				if pla.room.x == 0:
					mess.code = 6
				else:
					mess.code = 4
					pla.room = world.grid[pla.room.x - 1][pla.room.y]
			def Look():
				mess.code = 5
				mess.message = pla.room.name

			options = {0 : err,
					   1 : North,
					   2 : South,
					   3 : East,
					   4 : West,
					   5 : Look,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
