from pieces.piece import Piece

class Pawn(piece):

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def notation(self):
		return "P" if self.color == "White" else "p"