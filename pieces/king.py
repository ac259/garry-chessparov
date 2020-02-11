from pieces.piece import Piece

class King(piece):

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def notation(self):
		return "K" if self.color == "White" else "k"