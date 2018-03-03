from input import Input
from update import Update
from player import Player
from output import Output

class Game:
	def __init__(self):
		self.inp = Input()
		self.upd = Update()
		self.player1 = Player()
		self.out = Output()

	def updateG(self):
		self.inp.updateI(self.upd)
		self.upd.updateU(self.player1, self.out)
		self.out.updateO()

if __name__ == "__main__":
	
	game = Game()
	
	# Call update functions in a forever loop
	while True:
		game.updateG()
