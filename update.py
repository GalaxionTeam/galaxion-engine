# Class that updates game stat
class Update:
	def __init__(self):
		# List of tasks
		self.toDo = []
	
	def update(self, pla, out):
		
		# Loop that terminates once task list is empty
		while len(self.toDo) > 0:
			
			# Initialize message to send to output
			message = []
			
			# Select and remove most recent task from task list
			a = self.toDo.pop()

			# User instruction not understood
			if a[0] == "X":
				message.append("X")
			
			# User wants to move
			elif a[0] == "M":
				message.append("M")

				# Move North
				if a[1] == "N":
					message.append("N")
					pla.yLocation += 1
				
				# Move South
				elif a[1] == "S":
					message.append("S")
					pla.yLocation -= 1

				# Move East
				elif a[1] == "E":
					message.append("E")
					pla.xLocation += 1

				# Move West
				elif a[1] == "W":
					message.append("W")
					pla.xLocation -= 1

				# Error in move instruction
				elif a[1] == "X":
					message.append("X")
			
			# User wants to know location
			elif a[0] == "P":
				message.append("P")
				message.append(pla.xLocation)
				message.append(pla.yLocation)

			# Send instructions to output
			out.toDo.append(message)
			