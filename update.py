from message import Message
import code
# Class that updates game stat
class Update:
	def __init__(self):
		# List of tasks
		self.messages = []

	def update(self, pla, out):

		# Loop that terminates once task list is empty
		while len(self.messages) > 0:

			mess = Message()
			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				mess.code = code.ERR
			def North():
				mess.code = code.NORTH
				pla.yLocation += 1
			def South():
				mess.code = code.SOUTH
				pla.yLocation -= 1
			def East():
				mess.code = code.EAST
				pla.xLocation += 1
			def West():
				mess.code = code.WEST
				pla.xLocation -= 1
			def Look():
				mess.code = code.LOOK
				mess.message = " (" + repr(pla.xLocation) + ", " + repr(pla.yLocation) + ")"

			options = {code.ERR : err,
					   code.NORTH : North,
					   code.SOUTH : South,
					   code.EAST : East,
					   code.WEST : West,
					   code.LOOK : Look,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
