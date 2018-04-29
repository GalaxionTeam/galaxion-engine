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
				elif(words[1].upper() == "USE"):
					if len(words) == 4 and words[2].upper() == "CREATE":
						args.append(words[3])
						mess.code = code.CUSE
					elif len(words) == 5 and words[2].upper() == "ADD":
						mess.code = code.ATAS
						args.append(words[3])
						args.append(words[4])
					elif len(words) == 5 and words[2].upper() == "REMOVE":
						mess.code = code.RTAS
						args.append(words[3])
						args.append(words[4])
					elif len(words) == 4 and words[2].upper() == "DELETE":
						mess.code = code.DUSE
						args.append(words[3])			
					elif len(words) == 6 and words[2].upper() == "EDIT":
						mess.code = code.EUSE
						args.append(words[3])
						args.append(words[4])
						args.append(words[5])
					else:
						mess.code = code.ERR
						mess.message = "Use command not recognized"
				else:
					print("Unrecognized Command!")
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
			if words.index("LOOK") != len(words) - 1:
				mess.code = code.LOOKITEM
				mess.message = words[words.index("LOOK") + 1]
			else:
				mess.code = code.LOOK
			

		elif "INVENTORY" in words:
			mess.code = code.INVENTORY

		elif "SELECT" in words:
			if words.index("SELECT") != len(words) - 1:
				mess.code = code.SELECT
				mess.message = words[words.index("SELECT") + 1]
			else:
				mess.code = code.ERR
				mess.message = "Item cannot be selected"

		elif "DROP" in words:
			if words.index("DROP") != len(words) - 1:
				mess.code = code.DROP
				mess.message = words[words.index("DROP") + 1]
			else:
				mess.code = code.ERR
				mess.message = "Item cannot be dropped"

		elif "CREATE" in words:
			if words.index("CREATE") != len(words) - 1:
				mess.code = code.CREATE
				mess.message = words[words.index("CREATE") + 1]
			else:
				mess.code = code.ERR

		elif "SAVE" in words:
			if words.index("SAVE") != len(words) - 1:
				mess.code = code.SAVE
				mess.message = words[words.index("SAVE") + 1]
			else:
				mess.code = code.SAVE
				mess.message = "data"

		elif "LOAD" in words:
			if words.index("LOAD") != len(words) - 1:
				mess.code = code.LOAD
				mess.message = words[words.index("LOAD") + 1]
			else:
				mess.code = code.LOAD
				mess.message = "data"
				mess.message = "Item cannot be created"

		elif "DELETE" in words:
			if words.index("DELETE") != len(words) - 1:
				mess.code = code.DELETE
				mess.message = words[words.index("DELETE") + 1]
			else:
				mess.code = code.ERR
				mess.message = "Item cannot be deleted"
		elif "USE" in words:
			if words.index("USE") != len(words) - 2:
				mess.code = code.USE
				mess.args.append(words[words.index("USE") + 1])
				mess.args.append(words[words.index("USE") + 2])
			else:
				mess.code = code.ERR
				mess.message = "Incorrect Syntax"

		# User command not understood
		else:
			mess.code = code.ERR
			mess.message = "Error"

		return mess

	def update(self, upd):
		# Read from command line
		a = input()

		# Send instructions to update
		upd.messages.append(self.parse_words(a))
