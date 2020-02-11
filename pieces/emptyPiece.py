from pieces.piece import Piece

class EmptyPiece(Piece):

	def __init__(self):
		pass


	def notation(self):
		return "-"