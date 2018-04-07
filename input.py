from message import Message

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
			mess.code = 1

		# Move South
		elif "SOUTH" in words:
			mess.code = 2

		# Move East
		elif "EAST" in words:
			mess.code = 3

		# Move West
		elif "WEST" in words:
			mess.code = 4

		# User wants to know location
		elif "LOOK" in words:
			mess.code = 5

		elif "INVENTORY" in words:
			mess.code = 6

		elif "SELECT" in words:
			if words.index("SELECT") != len(words) - 1:
				mess.code = 7
				mess.message = words[words.index("SELECT") + 1]
			else:
				mess.code = 0

		elif "DROP" in words:
			if words.index("DROP") != len(words) - 1:
				mess.code = 8
				mess.message = words[words.index("DROP") + 1]
			else:
				mess.code = 0

		elif "CREATE" in words:
			if words.index("CREATE") != len(words) - 1:
				mess.code = 10
				mess.message = words[words.index("CREATE") + 1]
			else:
				mess.code = 0
		elif "DELETE" in words:
			if words.index("DELETE") != len(words) - 1:
				mess.code = 14
				mess.message = words[words.index("DELETE") + 1]
			else:
				mess.code = 0
		# User command not understood
		else:
			mess.code = 0

		return mess

	def update(self, upd):
		# Read from command line
		a = input()

		# Send instructions to update
		upd.messages.append(self.parse_words(a))
