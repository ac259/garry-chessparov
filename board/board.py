from board.square import Square
from pieces.emptyPiece import EmptyPiece

class Board:
	squares = {}

	def __init__(self):
		pass

	def createBoard(self):
		for square in range(64):
			self.squares[square] = Square(EmptyPiece(), square)

	def printBoard(self):
		count = 0
		for square in range(64):
			print("|", end = self.squares[square].pieceOnSquare.notation())
			count += 1
			if count == 8:
				print("|", end='\n')
				count = 0
