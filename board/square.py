class Square:

	'''
	The rows of squares on the chessboard are called ranks 
	and the columns of squares are called files. 
	The ranks are labelled from 1 to 8 and the files are labelled from a - h.
	'''
	pieceOnSquare = None
	squareCoord = None

	def __init__(self, piece, coordinate):
		self.pieceOnSquare = piece
		self.squareCoord = coordinate
		