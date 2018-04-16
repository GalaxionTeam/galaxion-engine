from message import Message
import code
# Class that reads user input
class Input:
	def __init__(self):
		pass

	def parse_words(self, a):
		mess = Message()


		if len(a) > 0:
			if a[0] == '~':
				words = a.split('~')
				args = []
				if(words[1].upper() == "ROOM"):
					if len(words) == 4:
						args.append(words[2])
						args.append(words[3])
						mess.code = code.EROOM
					else:
						mess.code = code.ERR
				elif(words[1].upper() == "ITEM"):
					if len(words) == 5:
						args.append(words[2])
						args.append(words[3])
						args.append(words[4])
						mess.code = code.EITEM
					else:
						mess.code = code.ERR
				else:
					print("Unrecognized Command")
					mess.code = code.ERR
				mess.args = args
				return mess

		# Capitalize all words and split into list
		words = a.upper().split()

		# Assign message code based on identified keywords
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
<<<<<<< HEAD
			mess.code = 5
			# Passes every token after "LOOK" as a list of message args
			arg_index = words.index("LOOK") + 1
			mess.args = words[arg_index::]
=======
			mess.code = code.LOOK
>>>>>>> 35d38cb9c26e12f6a65c7b83fb6e8d060ed3ba43

		elif "INVENTORY" in words:
			mess.code = code.INVENTORY

		elif "SELECT" in words:
			if words.index("SELECT") != len(words) - 1:
				mess.code = code.SELECT
				mess.message = words[words.index("SELECT") + 1]
			else:
				mess.code = code.ERR

		elif "DROP" in words:
			if words.index("DROP") != len(words) - 1:
				mess.code = code.DROP
				mess.message = words[words.index("DROP") + 1]
			else:
				mess.code = code.ERR

		elif "CREATE" in words:
			if words.index("CREATE") != len(words) - 1:
				mess.code = code.CREATE
				mess.message = words[words.index("CREATE") + 1]
			else:
				mess.code = code.ERR
		elif "DELETE" in words:
			if words.index("DELETE") != len(words) - 1:
				mess.code = code.DELETE
				mess.message = words[words.index("DELETE") + 1]
			else:
				mess.code = code.ERR

		# User command not understood
		else:
			mess.code = code.ERR

		return mess

	def update(self, upd):
		# Read from command line
		a = input()

		# Send instructions to update
		upd.messages.append(self.parse_words(a))
