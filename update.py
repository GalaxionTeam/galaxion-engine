import json
from message import Message
import code
from assets.item import Item
from assets.world import World
from assets.room import Room

# Class that updates game stat
class Update:
	def __init__(self):
		# List of tasks
		self.messages = []

	def update(self, pla, out, world):

		# Loop that terminates once task list is empty
		while len(self.messages) > 0:

			mess = Message()
			# Select and remove most recent task from task list
			a = self.messages.pop()

			def err():
				mess.code = code.ERR
				mess.message = a.message
			def North():
				if pla.room.y == len(world.grid[0]) - 1:
					mess.code = code.OUT
				else:
					mess.code = code.NORTH
					pla.room = world.grid[pla.room.x][pla.room.y + 1]
					mess.message = pla.room.name + "\n" + pla.room.description

			def South():
				if pla.room.y == 0:
					mess.code = code.OUT
				else:
					mess.code = code.SOUTH
					pla.room = world.grid[pla.room.x][pla.room.y - 1]
					mess.message = pla.room.name + "\n" + pla.room.description
			def East():
				if pla.room.x == len(world.grid) - 1:
					mess.code = code.OUT
				else:
					mess.code = code.EAST
					pla.room = world.grid[pla.room.x + 1][pla.room.y]
					mess.message = pla.room.name + "\n" + pla.room.description
			def West():
				if pla.room.x == 0:
					mess.code = code.OUT
				else:
					mess.code = code.WEST
					pla.room = world.grid[pla.room.x - 1][pla.room.y]
					mess.message = pla.room.name + "\n" + pla.room.description
			def Look():
				mess.code = code.LOOK
				mess.message = pla.room.name + "\n" + pla.room.description
				mess.args = pla.room.items
			def Look_Item():
				mess.code = code.ERR
				for b in pla.room.items:
					if a.message == b.name.upper():
						mess.code = code.LOOKITEM
						mess.args.append(b)
			def Inventory():
				mess.code = code.INVENTORY
				mess.args = pla.items
			def Select():
				mess.code = code.ERR
				for b in pla.room.items:
					if a.message == b.name.upper():
						pla.items.append(pla.room.items.pop(pla.room.items.index(b)))
						mess.code = code.SELECT
						mess.message = b.name
			def Drop():
				mess.code = code.DROP
				for b in pla.items:
					if a.message == b.name.upper():
						pla.room.items.append(pla.items.pop(pla.items.index(b)))
						mess.code = code.DROP
						mess.message = b.name
			def Create():
				mess.code = code.CREATE
				mess.message = a.message
				pla.room.items.append(Item(a.message))
			def Save():
				mess.code = code.SAVE
				item_x = []
				item_y = []
				item_name = []
				item_description = []
				item_loc_des = []
				room_name = []
				room_description = []
				for d in range(len(world.grid)):
					for b in range(len(world.grid[0])):
						room_name.append(world.grid[d][b].name)
						room_description.append(world.grid[d][b].description)
						for c in world.grid[d][b].items:
							# Item x/y coordinate
							item_x.append(world.grid[d][b].x)
							item_y.append(world.grid[d][b].y)
							item_name.append(c.name)
							item_description.append(c.description)
							item_loc_des.append(c.location_desc)

				for d in pla.items:
					# If item is in player's inventory, x and y = -1
					item_x.append(-1)
					item_y.append(-1)
					item_name.append(d.name)
					item_description.append(d.description)
					item_loc_des.append(d.location_desc)
				json_data = {
					"Player" : {"x_loc" : pla.room.x, "y_loc" : pla.room.y},
					"Items" : {"x_loc" : item_x, "y_loc" : item_y, "name" : item_name, "description" : item_description, "loc_des" : item_loc_des},
					"World" : {"x_dim" : len(world.grid), "y_dim" : len(world.grid[0])},
					"Room" : {"name" : room_name, "description" : room_description}
				}
				with open(a.message.lower() + ".json", 'w') as outfile:
 					json.dump(json_data,outfile)

			def Load():
				mess.code = code.LOAD

				with open(a.message.lower() + ".json", "r") as read:
					json_data = json.load(read)
				item_x = json_data["Items"]["x_loc"]
				item_y = json_data["Items"]["y_loc"]
				item_name = json_data["Items"]["name"]
				item_description = json_data["Items"]["description"]
				item_loc_des = json_data["Items"]["loc_des"]
				room_name = json_data["Room"]["name"]
				room_description = json_data["Room"]["description"]
				world.copy(json_data["World"]["x_dim"],json_data["World"]["y_dim"])
				pla.room = world.grid[json_data["Player"]["x_loc"]][json_data["Player"]["y_loc"]]
				room = 0
				for d in range(json_data["World"]["x_dim"]):
					for b in range(json_data["World"]["y_dim"]):
						if room < len(room_name):
							world.grid[d][b].name = room_name[room]
							world.grid[d][b].description = room_description[room]
						room += 1
				pla.items.clear()

				for d in range(len(item_x)):
					# If x/y = -1, item in inventory, else item in specific x/y
					if item_x[d] == -1:
						pla.items.append(Item(item_name[d],item_description[d]),item_loc_des[d])
					else:
						world.grid[item_x[d]][item_y[d]].items.append(Item(item_name[d],item_description[d],item_loc_des[d]))

			def Delete():
				mess.code = code.DELETE
				mess.message = a.message
				for b in pla.room.items:
					if a.message.upper() == b.name.upper():
						pla.room.items.pop(pla.room.items.index(b))

			def Edit_Room():
				mess.code = code.EROOM
				if a.args[0].upper() == "NAME":
					pla.room.name = a.args[1]
				elif a.args[0].upper() == "DESCRIPTION":
					pla.room.description = a.args[1]
				else:
					mess.code = code.ERR

			def Create_Use():
				mess.code = code.CUSE
				with open('use.json', 'r') as read_file:
					data = json.load(read_file)
				data.update({a.args[0].upper() : {"COMPLETE" : False, "MESSAGE" : "", "ANCHOR" : "", "CREATE": "", "TASKS" : {}}})
				with open("use.json", 'w') as outfile:
 					json.dump(data,outfile)


			def Add_Task():
				mess.code = code.ATAS
				with open('use.json', 'r') as read_file:
					data = json.load(read_file)
				try:
					data[a.args[0].upper()]["TASKS"].update({a.args[1].upper() : False})
					with open("use.json", 'w') as outfile:
 						json.dump(data,outfile)
				except:
					mess.code = code.ERR
					mess.message = "Use does not exist"

			def Delete_Use():
				mess.code = code.DUSE
				with open('use.json', 'r') as read_file:
					data = json.load(read_file)
				try:
					del data[a.args[0].upper()]
					with open("use.json", 'w') as outfile:
 						json.dump(data,outfile)
				except:
					mess.code = code.ERR
					mess.message = "Use cannot be deleted"

			def Remove_Task():
				mess.code = code.RTAS
				with open('use.json', 'r') as read_file:
					data = json.load(read_file)
				try:
					del data[a.args[0].upper()]["TASKS"][a.args[1].upper()]
					with open("use.json", 'w') as outfile:
 						json.dump(data,outfile)
				except:
					mess.code = code.ERR
					mess.message = "Task cannot be removed"

			def Edit_Use():
				mess.code = code.EUSE
				with open('use.json', 'r') as read_file:
					data = json.load(read_file)
				try:
					data[a.args[0].upper()][a.args[1].upper()] = a.args[2]
					with open("use.json", 'w') as outfile:
 						json.dump(data,outfile)
				except:
					mess.code = code.ERR
					mess.message = "Use cannot be edited"

			def Use():
				a_in_room = False
				b_in_room = False
				for b in pla.items:
					if a.args[0].upper() == b.name.upper():
						a_in_room = True
					if a.args[1].upper() == b.name.upper():
						b_in_room = True
				for b in pla.room.items:
					if a.args[0].upper() == b.name.upper():
						a_in_room = True
					if a.args[1].upper() == b.name.upper():
						b_in_room = True
				if a.args[1].upper() == pla.room.name.upper():
					b_in_room = True

				if a_in_room:
					with open('use.json', 'r') as read_file:
						data = json.load(read_file)
					try:
						use = data[a.args[1].upper()]
						if use["ANCHOR"] == "" or (use["ANCHOR"] == a.args[1].upper() and b_in_room):
							data[a.args[1].upper()]["TASKS"][a.args[0].upper()] = True
							mess.message = a.args[0].upper() + " used on " + a.args[1].upper()
							mess.code = code.USE
						else:
							mess.code = code.ERR
							mess.message = "Items not in room"
						if use["COMPLETE"] == False:
							complete = True
							use = use["TASKS"]
							for key,val in use.items():
								if val == False:
									complete = False
							data[a.args[1].upper()]["COMPLETE"] = complete
							if complete:
								mess.message += "\n" + data[a.args[1].upper()]["MESSAGE"]
								if data[a.args[1].upper()]["CREATE"] != "":
									mess2 = Message()
									mess2.code = code.CREATE
									mess2.message = data[a.args[1].upper()]["CREATE"]
									self.messages.append(mess2)

							#	for key1 in data:
							#		for key,val in data[key1]["TASKS"]:
							#			if key == a.args[1].upper():
							#				data[key1]["TASKS"][key] = True


						with open("use.json", 'w') as outfile:
 							json.dump(data,outfile)
					except:
						mess.message = "Use not defined!"
						mess.code = code.ERR
				else:
					mess.code = code.ERR
					mess.message = "Items not in room"

			def Edit_Item():
				mess.code = code.EITEM
				inside = False
				loc = 0
				for i in range(len(pla.room.items)):
					if (a.args[0].upper() == pla.room.items[i].name.upper()):
						inside = True
						loc = i
				if inside:
					if a.args[1].upper() == "NAME":
						pla.room.items[loc].name = a.args[2]
					elif a.args[1].upper() == "DESCRIPTION":
						pla.room.items[loc].description = a.args[2]
					elif a.args[1].upper() == "LOCATION DESCRIPTION":
						pla.room.items[loc].location_desc = a.args[2]
					else:
						mess.code = code.ERR
				else:
					mess.code = code.ERR

			def Exit():
				exit()

			options = {code.ERR : err,
					   code.NORTH : North,
					   code.SOUTH : South,
					   code.EAST : East,
					   code.WEST : West,
					   code.LOOK : Look,
					   code.INVENTORY : Inventory,
					   code.SELECT : Select,
					   code.DROP : Drop,
					   code.CREATE : Create,
					   code.SAVE : Save,
					   code.EUSE : Edit_Use,
					   code.USE : Use,
					   code.LOAD : Load,
             		   code.DELETE : Delete,
             		   code.DUSE : Delete_Use,
             		   code.ATAS : Add_Task,
             		   code.RTAS : Remove_Task,
					   code.EROOM : Edit_Room,
					   code.EITEM : Edit_Item,
					   code.CUSE : Create_Use,
					   code.LOOKITEM : Look_Item,
					   code.EXIT : Exit,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
