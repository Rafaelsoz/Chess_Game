from auxi.const import *
from pieces.bishop import Bishop
from pieces.king import King
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.queen import Queen
from board.board import Board


class Game:

    def __init__(self, screen):
        self.turn_white = True
        self.white_pieces = []
        self.black_pieces = []

        self.white_pieces_locations = [None] * 16
        self.black_pieces_locations = [None] * 16

        self.screen = screen
        self.board = Board(screen)

        self.__create_pieces()

    def change_turn(self):
        self.turn_white = False if self.turn_white is True else True

    def __load_positions(self):
        for idx, piece in enumerate(self.white_pieces):
            self.white_pieces_locations[idx] = piece.position.get_position()

        for idx, piece in enumerate(self.black_pieces):
            self.black_pieces_locations[idx] = piece.position.get_position()

    def __create_pieces(self):
        self.white_pieces.append(Rook(True, WHITE_LOCATIONS[0]))
        self.white_pieces.append(Knight(True, WHITE_LOCATIONS[1]))
        self.white_pieces.append(Bishop(True, WHITE_LOCATIONS[2]))
        self.white_pieces.append(King(True, WHITE_LOCATIONS[3]))
        self.white_pieces.append(Queen(True, WHITE_LOCATIONS[4]))
        self.white_pieces.append(Bishop(True, WHITE_LOCATIONS[5]))
        self.white_pieces.append(Knight(True, WHITE_LOCATIONS[6]))
        self.white_pieces.append(Rook(True, WHITE_LOCATIONS[7]))
        for i in range(8, 16):
            self.white_pieces.append(Pawn(True, WHITE_LOCATIONS[i]))

        self.black_pieces.append(Rook(False, BLACK_LOCATIONS[0]))
        self.black_pieces.append(Knight(False, BLACK_LOCATIONS[1]))
        self.black_pieces.append(Bishop(False, BLACK_LOCATIONS[2]))
        self.black_pieces.append(King(False, BLACK_LOCATIONS[3]))
        self.black_pieces.append(Queen(False, BLACK_LOCATIONS[4]))
        self.black_pieces.append(Bishop(False, BLACK_LOCATIONS[5]))
        self.black_pieces.append(Knight(False, BLACK_LOCATIONS[6]))
        self.black_pieces.append(Rook(False, BLACK_LOCATIONS[7]))
        for i in range(8, 16):
            self.black_pieces.append(Pawn(False, BLACK_LOCATIONS[i]))

        self.__load_positions()

    def save_piece_location(self, piece, idx):
        if piece.white:
            self.white_pieces_locations[idx] = piece.position.get_position()
        else:
            self.black_pieces_locations[idx] = piece.position.get_position()

    def drawing_pieces(self):

        for piece in self.white_pieces:
            if piece.die is False:
                piece.drawing_image(self.screen)
            else:
                piece.drawing_die_image(self.screen)

        for piece in self.black_pieces:
            if piece.die is False:
                piece.drawing_image(self.screen)
            else:
                piece.drawing_die_image(self.screen)

    def paint_current_position(self, position):
        pygame.draw.rect(self.screen, BLUE, (position[0] * EDGE + INITIAL_POSITION, position[1] * EDGE
                                             + INITIAL_POSITION, EDGE, EDGE))
        pygame.draw.rect(self.screen, (20, 20, 20), (position[0] * EDGE + INITIAL_POSITION, position[1] * EDGE
                                                     + INITIAL_POSITION, EDGE, EDGE), 2)

    def paint_moves_list(self, white, current_id):
        if current_id is not None:
            if white:
                piece = self.white_pieces[current_id]
                self.paint_current_position(piece.position.get_position())
                for new_pos in piece.moves_list(self.white_pieces_locations, self.black_pieces_locations):
                    pygame.draw.rect(self.screen, BLACK_GREEN, (new_pos[0] * EDGE + INITIAL_POSITION, new_pos[1] * EDGE
                                                                + INITIAL_POSITION, EDGE, EDGE))
                    pygame.draw.rect(self.screen, (20, 20, 20), (new_pos[0] * EDGE + INITIAL_POSITION, new_pos[1] * EDGE
                                                                 + INITIAL_POSITION, EDGE, EDGE), 2)
            else:
                piece = self.black_pieces[current_id]
                self.paint_current_position(piece.position.get_position())
                for new_pos in piece.moves_list(self.black_pieces_locations, self.white_pieces_locations):
                    pygame.draw.rect(self.screen, BLACK_GREEN, (new_pos[0] * EDGE + INITIAL_POSITION, new_pos[1] * EDGE
                                                                + INITIAL_POSITION, EDGE, EDGE))
                    pygame.draw.rect(self.screen, (20, 20, 20), (new_pos[0] * EDGE + INITIAL_POSITION, new_pos[1] * EDGE
                                                                 + INITIAL_POSITION, EDGE, EDGE), 2)

    def battle(self, piece):
        if piece.white:
            position = piece.position.get_position()
            for idx in range(len(self.black_pieces_locations)):
                if position == self.black_pieces_locations[idx]:
                    self.black_pieces_locations[idx] = None
                    self.black_pieces[idx].die_piece()

        else:
            position = piece.position.get_position()
            for idx in range(len(self.white_pieces_locations)):
                if position == self.white_pieces_locations[idx]:
                    self.white_pieces_locations[idx] = None
                    self.white_pieces[idx].die_piece()
