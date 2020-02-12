from pieces.piece import Piece

class Knight(Piece):

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def notation(self):
		return "N" if self.color == "White" else "n"