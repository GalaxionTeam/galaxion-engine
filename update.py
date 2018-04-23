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
			def South():
				if pla.room.y == code.SOUTH:
					mess.code = code.OUT
				else:
					mess.code = code.SOUTH
					pla.room = world.grid[pla.room.x][pla.room.y - 1]
			def East():
				if pla.room.x == len(world.grid) - 1:
					mess.code = code.OUT
				else:
					mess.code = code.EAST
					pla.room = world.grid[pla.room.x + 1][pla.room.y]
			def West():
				if pla.room.x == 0:
					mess.code = code.OUT
				else:
					mess.code = code.WEST
					pla.room = world.grid[pla.room.x - 1][pla.room.y]
			def Look():
				mess.code = code.LOOK
				mess.message = pla.room.name
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
				#print(str(pla.room.items))
			def Delete():
				mess.code = code.DELETE
				mess.message = a.message
				for b in pla.room.items:
					if a.message == b.name.upper():
						pla.room.items.pop(pla.room.items.index(b))
						#print(str(pla.room.items))

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
				try:
					data[a.args[0].upper()][a.args[1].upper()] = a.args[2]
				except:
					data.update({a.args[0].upper() : {a.args[1].upper() : a.args[2]}})
				with open("use.json", 'w') as outfile:
 					json.dump(data,outfile)
			
			def Use():
				a_in_room = False
				b_in_room = False
				for b in pla.items:
					if a.args[0] == b.name.upper():
						a_in_room = True
					if a.args[1] == b.name.upper():
						b_in_room = True
				for b in pla.room.items:
					if a.args[0] == b.name.upper():
						a_in_room = True
					if a.args[1] == b.name.upper():
						b_in_room = True
				if a.args[1] == pla.room.name.upper():
					b_in_room = True
				if a_in_room and b_in_room:
					with open('use.json', 'r') as read_file:
						data = json.load(read_file)
					try:
						mess.message = data[a.args[0].upper()][a.args[1].upper()]
						mess.code = code.USE
					except:
						mess.message = "Use not defined"
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
					   code.USE : Use,
					   code.LOAD : Load,
             		   code.DELETE : Delete,
					   code.EROOM : Edit_Room,
					   code.EITEM : Edit_Item,
					   code.CUSE : Create_Use,
					   code.LOOKITEM : Look_Item,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
