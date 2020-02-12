from pieces.piece import Piece

class Bishop(Piece):
	color = None
	position = None

	def __init__(self, color, position):
		self.color = color
		self.position = position

	def notation(self):
		return "B" if self.color == "White" else "b"