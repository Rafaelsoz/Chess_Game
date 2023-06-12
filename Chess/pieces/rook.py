from piece import Piece
from auxi.const import WHITE_ROOK, BLACK_ROOK, DIE_WHITE_ROOK, DIE_BLACK_ROOK
from board.board import position_in_board


class Rook(Piece):

    def __init__(self, white, axis):
        Piece.__init__(self, white, WHITE_ROOK if white else BLACK_ROOK,
                       DIE_WHITE_ROOK if white else DIE_BLACK_ROOK, axis, "Rook")

        self._houses = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        moves = []

        for house in self._houses:
            multiplier = 1
            path = True

            while path:
                new_pos = (self.position.axis_x + (multiplier * house[0]),
                           self.position.axis_y + (multiplier * house[1]))
                if new_pos not in partners_pieces_location and position_in_board(new_pos):
                    moves.append(new_pos)
                    if new_pos in enemies_pieces_locations:
                        path = False
                    multiplier += 1
                else:
                    path = False

        self.valid_movies = moves

        return self.valid_movies
