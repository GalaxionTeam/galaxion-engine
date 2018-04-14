from message import Message
import code
# Class that reads user input
class Input:
	def __init__(self):
		pass

	def parse_words(self, a):
		mess = Message()

		# Split words into list
		words = a.split()

		# Make all words uppercase
		for i in range(0,len(words)):
			words[i] = words[i].upper()

		# Move North
		if "NORTH" in words:
			mess.code = code.NORTH

		# Move South
		elif "SOUTH" in words:
			mess.code = code.SOUTH

		# Move East
		elif "EAST" in words:
			mess.code = code.EAST

		# Move West
		elif "WEST" in words:
			mess.code = code.WEST

		# User wants to know location
		elif "LOOK" in words:
			mess.code = code.LOOK

		elif "INVENTORY" in words:
			mess.code = code.INVENTORY

		elif "SELECT" in words:
			if words.index("SELECT") != len(words) - 1:
				mess.code = code.SELECT
				mess.message = words[words.index("SELECT") + 1]
			else:
				mess.code = code.ERR

		elif "DROP" in words:
			if words.index("DROP") != len(words) - 1:
				mess.code = code.DROP
				mess.message = words[words.index("DROP") + 1]
			else:
				mess.code = code.ERR

		elif "CREATE" in words:
			if words.index("CREATE") != len(words) - 1:
				mess.code = code.CREATE
				mess.message = words[words.index("CREATE") + 1]
			else:
				mess.code = code.ERR
		elif "DELETE" in words:
			if words.index("DELETE") != len(words) - 1:
				mess.code = code.DELETE
				mess.message = words[words.index("DELETE") + 1]
			else:
				mess.code = code.ERR

		# User command not understood
		else:
			mess.code = code.ERR

		return mess

	def update(self, upd):
		# Read from command line
		a = input()

		# Send instructions to update
		upd.messages.append(self.parse_words(a))
