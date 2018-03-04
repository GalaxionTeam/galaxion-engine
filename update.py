from message import Message

# Class that updates game stat
class Update:
	def __init__(self):
		# List of tasks
		self.messages = []
	
	def update(self, pla, out):
		
		# Loop that terminates once task list is empty
		while len(self.messages) > 0:
			
			mess = Message()			
			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				mess.code = 0
			def North():
				mess.code = 1
				pla.yLocation += 1
			def South():
				mess.code = 2
				pla.yLocation -= 1
			def East():
				mess.code = 3
				pla.xLocation += 1
			def West():
				mess.code = 4
				pla.xLocation -= 1
			def Look():
				mess.code = 5
				mess.message = " (" + repr(pla.xLocation) + ", " + repr(pla.yLocation) + ")"
				
			options = {0 : err,
					   1 : North,
					   2 : South,
					   3 : East,
					   4 : West,
					   5 : Look,
					   }
			options[a.code]()
			
			# Send instructions to output
			out.messages.append(mess)
