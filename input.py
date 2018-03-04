from message import Message

# Class that reads user input
class Input:
	def __init__(self):
		pass

	def parse_words(self, a):
		# Split words into list
		words = a.split()

		# Make all words uppercase
		for i in range(0,len(words)):
			words[i] = words[i].upper()

		# Move North
		if "NORTH" in words:
			return(1)

		# Move South
		elif "SOUTH" in words:
			return(2)

		# Move East
		elif "EAST" in words:
			return(3)

		# Move West
		elif "WEST" in words:
			return(4)

		# User wants to know location
		elif "LOOK" in words:
			return(5)
		
		# User command not understood
		else:
			return(0)

	def update(self, upd):
		# Read from command line
		a = input()
		mess = Message()
		mess.code = self.parse_words(a)

		# Send instructions to update
		upd.messages.append(mess)
