from pieces.piece import Piece

class Rook(Piece):

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def notation(self):
		return "R" if self.color == "White" else "r"