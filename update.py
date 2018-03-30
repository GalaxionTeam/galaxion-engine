import json
from message import Message
from assets.item import Item

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
				mess.code = 0
			def North():
				if pla.room.y == len(world.grid[0]) - 1:
					mess.code = 9
				else:
					mess.code = 1
					pla.room = world.grid[pla.room.x][pla.room.y + 1]
			def South():
				if pla.room.y == 0:
					mess.code = 9
				else:
					mess.code = 2
					pla.room = world.grid[pla.room.x][pla.room.y - 1]
			def East():
				if pla.room.x == len(world.grid) - 1:
					mess.code = 9
				else:
					mess.code = 3
					pla.room = world.grid[pla.room.x + 1][pla.room.y]
			def West():
				if pla.room.x == 0:
					mess.code = 9
				else:
					mess.code = 4
					pla.room = world.grid[pla.room.x - 1][pla.room.y]
			def Look():
				mess.code = 5
				mess.message = pla.room.name
				mess.args = pla.room.items
			def Inventory():
				mess.code = 6
				mess.args = pla.items
			def Select():
				mess.code = 0
				for b in pla.room.items:
					if a.message == b.name:
						pla.items.append(pla.room.items.pop(pla.room.items.index(b)))
						mess.code = 7
						mess.message = a.message
			def Drop():
				mess.code = 0
				for b in pla.items:
					if a.message == b.name:
						pla.room.items.append(pla.items.pop(pla.items.index(b)))
						mess.code = 8
						mess.message = a.message
			def Create():
				mess.code = 10
				mess.message = a.message
				pla.room.items.append(Item(a.message))

			def Save():
				mess.code = 11
				item_x = []
				item_y = []
				item_name = []
				item_description = []
				room_name = []
				room_description = []
				for d in range(len(world.grid)):
					for b in range(len(world.grid[0])):
						room_name.append(world.grid[d][b].name)
						room_description.append(world.grid[d][b].description)
						for c in world.grid[d][b].items:
							item_x.append(world.grid[d][b].x)
							item_y.append(world.grid[d][b].y)
							item_name.append(c.name)
							item_description.append(c.description)

				for d in pla.items:
					item_x.append(-1)
					item_y.append(-1)
					item_name.append(d.name)
					item_description.append(d.description)
				json_data = {
					"Player" : {"x_loc" : pla.room.x, "y_loc" : pla.room.y},
					"Items" : {"x_loc" : item_x, "y_loc" : item_y, "name" : item_name, "description" : item_description},
					"World" : {"x_dim" : len(world.grid), "y_dim" : len(world.grid[0])},
					"Room" : {"name" : room_name, "description" : room_description}
				}
				with open(a.message.lower() + ".json", 'w') as outfile:
 					json.dump(json_data,outfile)

			def Load():
				mess.code = 12

				with open(a.message.lower() + ".json", "r") as read:
					json_data = json.load(read)
				pla.room = world.grid[json_data["Player"]["x_loc"]][json_data["Player"]["y_loc"]]
				item_x = json_data["Items"]["x_loc"]
				item_y = json_data["Items"]["y_loc"]
				item_name = json_data["Items"]["name"]
				item_description = json_data["Items"]["description"]
				room_name = json_data["Room"]["name"]
				room_description = json_data["Room"]["description"]

				room = 0
				for d in range(json_data["World"]["x_dim"]):
					for b in range(json_data["World"]["x_dim"]):
						world.grid[d][b].items.clear()
						world.grid[d][b].name = room_name[room]
						world.grid[d][b].description = room_description[room]
						room += 1
				pla.items.clear()

				for d in range(len(item_x)):
					if item_x[d] == -1:
						pla.items.append(Item(item_name[d],item_description[d]))
					else:
						world.grid[item_x[d]][item_y[d]].items.append(Item(item_name[d],item_description[d]))

			options = {0 : err,
					   1 : North,
					   2 : South,
					   3 : East,
					   4 : West,
					   5 : Look,
					   6 : Inventory,
					   7 : Select,
					   8 : Drop,
					   10 : Create,
					   11 : Save,
					   12 : Load,
					   }
			options[a.code]()

			# Send instructions to output
			out.messages.append(mess)
