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

		# User wants to move
		if "MOVE" in words:
			message.append("M")

			# Move North
			if "NORTH" in words:
				message.append("N")
			
			# Move South
			elif "SOUTH" in words:
				message.append("S")

			# Move East
			elif "EAST" in words:
				message.append("E")

			# Move West
			elif "WEST" in words:
				message.append("W")

			# Error in move instruction
			else:
				message.append("X")
		
		# User wants to know location
		elif "POSITION" in words:
			message.append("P")
		
		# User command not understood
		else:
			message.append("X")

		# Send instructions to update
		upd.toDo.append(message)
