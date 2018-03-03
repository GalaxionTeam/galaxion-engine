# Class that updates game stat
class Update:
	def __init__(self):
		# List of tasks
		self.messages = []
	
	def update(self, pla, out):
		
		# Loop that terminates once task list is empty
		while len(self.messages) > 0:
			
			# Initialize message to send to output
			message = []
			
			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				message.append(0)
			def North():
				message.append(1)
				pla.yLocation += 1
			def South():
				message.append(2)
				pla.yLocation -= 1
			def East():
				message.append(3)
				pla.xLocation += 1
			def West():
				message.append(4)
				pla.xLocation -= 1
			def Look():
				message.append(5)
				message.append(pla.xLocation)
				message.append(pla.yLocation)
			options = {0 : err,
					   1 : North,
					   2 : South,
					   3 : East,
					   4 : West,
					   5 : Look,
					   }
			options[a[0]]()
			
			# Send instructions to output
			out.messages.append(message)
			