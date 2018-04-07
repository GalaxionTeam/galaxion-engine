from message import Message

# Class that reads user input
class Input:
		
	def __init__(self):
		pass

	def generate_message(user_command):

		#Valid commands
    		regular_commands = 
{"ERROR" : "ERR_CMD", "NORTH" : "PLA_N_WRLD", "SOUTH" : "PLA_S_WRLD", "EAST" : "PLA_E_WRLD", "WEST" : "PLA_W_WRLD", "DROP" : "PLA_RMV_INV"}

		special_commands = 
["CREATE", "DROP", "SELECT", "GRAB", "TAKE"]
	
		mess = Message()

		# Make all words uppercase
		user_command = user_command.upper()

		#Make list of words
		command_list = user_command.split()
		
		#Check for regular and special commands, return relevant message 
		for i in range(0,len(command_list)):
			if command_list[i] in special_commands and i+1 < len(command_list):
				command_list[i] = command_list[i] + " " + command_list[i+1]
				return command_list[i]
			elif command_list[i] in regular_commands:
				return regular_commands[command_list[i]]
			else:
				return "ERR_CMD"

	def update(self, upd):
		# Read from command line
		a = input()

		# Send instructions to update
		upd.messages.append(self.generate_message(a))
