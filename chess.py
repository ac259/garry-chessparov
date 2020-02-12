import pygame
from board.board import Board
pygame.init()

gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption('Chess Board')
clock = pygame.time.Clock()
quitGame = False

chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()

allTiles = []
allPieces = []

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])

def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    # black = (66, 134, 244)
    # white = (143, 155, 175)
    black = (128, 128, 128)
    white = (255, 255, 255)
    number = 0

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)
                if not Board.squares[number].pieceOnSquare.notation() == "-":
                    img = pygame.image.load("./images/" + Board.squares[number].pieceOnSquare.color[0].upper() + Board.squares[number].pieceOnSquare.notation().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], Board.squares[number].pieceOnSquare])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, black)
                if not Board.squares[number].pieceOnSquare.notation() == "-":
                    img = pygame.image.load("./images/" + Board.squares[number].pieceOnSquare.color[0].upper() + Board.squares[number].pieceOnSquare.notation().upper() + ".png")
                    img = pygame.transform.scale(img, (100, 100))
                    allPieces.append([img, [xpos, ypos], Board.squares[number].pieceOnSquare])
                xpos += 100

            color += 1
            number += 1
            # print(number)
        color += 1
        xpos = 0
        ypos += 100

drawChessPieces()

while not quitGame:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitGame = True
			pygame.quit()
			quit()

	for img in allPieces:
		gameDisplay.blit(img[0], img[1])


	pygame.display.update()
	clock.tick(60)