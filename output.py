# Class for game output
class Output:
	def __init__(self):
		# List of tasts
		self.toDo = []

	def update(self):
		print("\033[H\033[J")
		# Loop that terminates once task list is empty
		while len(self.toDo) > 0:
			
			# Select and remove most recent task from task list
			a = self.toDo.pop()
			
			# User instruction not understood
			if a[0] == "X":
				print("Command not recognized")
			
			# User wants to move
			elif a[0] == "M":
				print("Move ", end = "")

				# Move north
				if a[1] == "N":
					print("North 1 Space")

				# Move south
				elif a[1] == "S":
					print("South 1 Space")

				# Move east
				elif a[1] == "E":
					print("East 1 Space")

				# Move west
				elif a[1] == "W":
					print("West 1 Space")

				# Error in move instruction
				elif a[1] == "X":
					print("Not Recognized")
			
			# Player location
			elif a[0] == "P":
				print("Player located at position (" + repr(a[1]) + ", " + repr(a[2]) + ")")
