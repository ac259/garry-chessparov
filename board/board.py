from board.square import Square
from pieces.emptyPiece import EmptyPiece
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.king import King
from pieces.queen import Queen
from pieces.pawn import Pawn

class Board:
	squares = {}

	def __init__(self):
		pass

	def createBoard(self):
		for square in range(64):
			self.squares[square] = Square(square, EmptyPiece())
		
		self.squares[0] = Square(0, Rook("Black",0))
		self.squares[1] = Square(1, Knight("Black",1)) 
		self.squares[2] = Square(2, Bishop("Black",2))
		self.squares[3] = Square(3, Queen("Black",3))
		self.squares[4] = Square(4, King("Black",4))
		self.squares[5] = Square(5, Bishop("Black",5))
		self.squares[6] = Square(6, Knight("Black",6))
		self.squares[7] = Square(7, Rook("Black",7))

		self.squares[8] = Square(8, Pawn("Black", 8))
		self.squares[9] = Square(9, Pawn("Black", 9))
		self.squares[10] = Square(10, Pawn("Black", 10))
		self.squares[11] = Square(11, Pawn("Black", 11))
		self.squares[12] = Square(12, Pawn("Black", 12))
		self.squares[13] = Square(13, Pawn("Black", 13))
		self.squares[14] = Square(14, Pawn("Black", 14))
		self.squares[15] = Square(15, Pawn("Black", 15))



		self.squares[56] = Square(56, Rook("White",56))
		self.squares[57] = Square(57, Knight("White",57)) 
		self.squares[58] = Square(58, Bishop("White",58))
		self.squares[59] = Square(59, Queen("White",59))
		self.squares[60] = Square(60, King("White",60))
		self.squares[61] = Square(61, Bishop("White",61))
		self.squares[62] = Square(62, Knight("White",62))
		self.squares[63] = Square(63, Rook("White",63))

		self.squares[48] = Square(48, Pawn("White", 48))
		self.squares[49] = Square(49, Pawn("White", 49))
		self.squares[50] = Square(50, Pawn("White", 50))
		self.squares[51] = Square(51, Pawn("White", 51))
		self.squares[52] = Square(52, Pawn("White", 52))
		self.squares[53] = Square(53, Pawn("White", 53))
		self.squares[54] = Square(54, Pawn("White", 54))
		self.squares[55] = Square(55, Pawn("White", 55))


	def printBoard(self):
		count = 0
		for square in range(64):
			print("|", end = self.squares[square].pieceOnSquare.notation())
			count += 1
			if count == 8:
				print("|", end='\n')
				count = 0
