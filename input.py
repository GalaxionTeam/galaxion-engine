# Class that reads user input
class Input:
	def __init__(self):
		pass

	def update(self, upd):
		# Read from command line
		a = input()

		# Split words into list
		words = a.split()

		# Make all words uppercase
		for i in range(0,len(words)):
			words[i] = words[i].upper()

		# Initialize list to send instructions to update
		message = []

		# Move North
		if "NORTH" in words:
			message.append(1)
			
		# Move South
		elif "SOUTH" in words:
			message.append(2)

		# Move East
		elif "EAST" in words:
			message.append(3)

		# Move West
		elif "WEST" in words:
			message.append(4)

		# User wants to know location
		elif "LOOK" in words:
			message.append(5)
		
		# User command not understood
		else:
			message.append(0)

		# Send instructions to update
		upd.messages.append(message)
		print(message)
