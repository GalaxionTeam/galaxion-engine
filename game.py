from input import Input
from update import Update
from assets.player import Player
from output import Output
from assets.world import World

class Game:
	def __init__(self):
		self.inp = Input()
		self.upd = Update()
		self.world = World(3,4)
		self.player1 = Player(self.world)
		self.out = Output()

	def update(self):
		self.inp.update(self.upd)
		self.upd.update(self.player1, self.out, self.world)
		self.out.update()

if __name__ == "__main__":

	game = Game()

	# Call update functions in a forever loop
	while True:
		game.update()
