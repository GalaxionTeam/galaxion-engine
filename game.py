import json
from input import Input
from update import Update
from assets.player import Player
from output import Output
from assets.world import World
import protologue
	
class Game:
	def __init__(self):
		print(protologue)
		self.inp = Input()
		self.upd = Update()
		self.world = World(3,5)
		self.player1 = Player(self.world)
		self.out = Output()

	def update(self):
		self.inp.update(self.upd)
		self.upd.update(self.player1, self.out, self.world)
		self.out.update()

if __name__ == "__main__":

	with open('use.json', 'r') as read_file:
		data = json.load(read_file)
	for key, value in data.items():
		data[key]["COMPLETE"] = False
		for key1, value1 in data[key]["TASKS"].items():
			data[key]["TASKS"][key1] = False
	with open("use.json", 'w') as outfile:
 		json.dump(data,outfile)

	game = Game()

	# Call update functions in a forever loop
	try:
		while True:
			game.update()
	except KeyboardInterrupt:
		print("\nThanks for playing!")
