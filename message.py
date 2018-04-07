class Message:
	def __init__(self, code=0, message="", debug="", args = None):
		self.code = code
		self.message = message
		self.debug = debug
		if args is None:
			args = []
		self.args = args
