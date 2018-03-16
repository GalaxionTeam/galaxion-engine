# Class for game output
class Output:
	def __init__(self):
		# List of tasts
		self.messages = []

	def update(self):
		# Loop that terminates once task list is empty
		while len(self.messages) > 0:

			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				print("Command not recognized")
				#I'm pretty sure we handle this case back in input
			def North():
				print("North 1 Space")
			def South():
				print("South 1 Space")
			def East():
				print("East 1 Space")
			def West():
				print("West 1 Space")
			def Look():
				print("Player located at position" + a.message)
			def Out():
				print("Out of Bounds")
			options = {0 : err,
					   1 : North,
					   2 : South,
					   3 : East,
					   4 : West,
					   5 : Look,
					   6 : Out,
					   }
			options[a.code]()
