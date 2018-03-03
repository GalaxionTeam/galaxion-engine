from output import Output
from player import Player

# Class that updates game stat
class Update:
	
	# List of tasks
	toDo = []
	
	def update():
		
		# Loop that terminates once task list is empty
		while len(Update.toDo) > 0:
			
			# Initialize message to send to output
			message = []
			
			# Select and remove most recent task from task list
			a = Update.toDo.pop()

			# User instruction not understood
			if a[0] == "X":
				message.append("X")
			
			# User wants to move
			elif a[0] == "M":
				message.append("M")

				# Move North
				if a[1] == "N":
					message.append("N")
					Player.yLocation += 1
				
				# Move South
				elif a[1] == "S":
					message.append("S")
					Player.yLocation -= 1

				# Move East
				elif a[1] == "E":
					message.append("E")
					Player.xLocation += 1

				# Move West
				elif a[1] == "W":
					message.append("W")
					Player.xLocation -= 1

				# Error in move instruction
				elif a[1] == "X":
					message.append("X")
			
			# User wants to know location
			elif a[0] == "P":
				message.append("P")
				message.append(Player.xLocation)
				message.append(Player.yLocation)

			# Send instructions to output
			Output.toDo.append(message)
			