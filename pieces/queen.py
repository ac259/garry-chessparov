from pieces.piece import Piece

class Queen(piece):

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def notation(self):
		return "Q" if self.color == "White" else "q"