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

		# User command not understood
		else:
			mess.code = code.ERR

		return mess

	def update(self, upd):
		# Read from command line
		a = input()

		# Send instructions to update
		upd.messages.append(self.parse_words(a))
