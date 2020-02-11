import pygame
from board.board import Board
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Chess Board')
clock = pygame.time.Clock()
quitGame = False

chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()

while not quitGame:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitGame = True
			pygame.quit()
			quit()


	pygame.display.update()
	clock.tick(60)