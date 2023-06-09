import pygame.transform
import pygame


HEIGHT = 700
WIDTH = 1000

EDGE = 80
INITIAL_POSITION = 30
END_POSITION = 30 + (EDGE * 8)

BOARD_COLOR = (60, 57, 57)
WHITE_COLOR = (232, 228, 194)
GRAY_COLOR = (96, 96, 96)
DARK_GREEN = (119, 154, 88)
BLACK_GREEN = (25, 56, 50)
BLUE = (60, 106, 213)

WHITE_LOCATIONS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

BLACK_LOCATIONS = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

KING_IDX = 3
KNIGHT_IDX = [1, 6]
BISHOP_IDX = [2, 5]

WHITE_ROOK = pygame.transform.scale(pygame.image.load('images/whiteRook.png'), (80, 80))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('images/whiteKnight.png'), (80, 80))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('images/whiteBishop.png'), (80, 80))
WHITE_KING = pygame.transform.scale(pygame.image.load('images/whiteKing.png'), (80, 80))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('images/whiteQueen.png'), (80, 80))
WHITE_PAWN = pygame.transform.scale(pygame.image.load('images/whitePawn.png'), (80, 80))

DIE_WHITE_ROOK = pygame.transform.scale(pygame.image.load('images/whiteRook.png'), (30, 30))
DIE_WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('images/whiteKnight.png'), (30, 30))
DIE_WHITE_BISHOP = pygame.transform.scale(pygame.image.load('images/whiteBishop.png'), (30, 30))
DIE_WHITE_KING = pygame.transform.scale(pygame.image.load('images/whiteKing.png'), (30, 30))
DIE_WHITE_QUEEN = pygame.transform.scale(pygame.image.load('images/whiteQueen.png'), (30, 30))
DIE_WHITE_PAWN = pygame.transform.scale(pygame.image.load('images/whitePawn.png'), (30, 30))

BLACK_ROOK = pygame.transform.scale(pygame.image.load('images/blackRook.png'), (80, 80))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('images/blackKnight.png'), (80, 80))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('images/blackBishop.png'), (80, 80))
BLACK_KING = pygame.transform.scale(pygame.image.load('images/blackKing.png'), (80, 80))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('images/blackQueen.png'), (80, 80))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('images/blackPawn.png'), (80, 80))

DIE_BLACK_ROOK = pygame.transform.scale(pygame.image.load('images/blackRook.png'), (30, 30))
DIE_BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('images/blackKnight.png'), (30, 30))
DIE_BLACK_BISHOP = pygame.transform.scale(pygame.image.load('images/blackBishop.png'), (30, 30))
DIE_BLACK_KING = pygame.transform.scale(pygame.image.load('images/blackKing.png'), (30, 30))
DIE_BLACK_QUEEN = pygame.transform.scale(pygame.image.load('images/blackQueen.png'), (30, 30))
DIE_BLACK_PAWN = pygame.transform.scale(pygame.image.load('images/blackPawn.png'), (30, 30))
