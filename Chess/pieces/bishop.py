from piece import Piece
from auxi.const import WHITE_BISHOP, BLACK_BISHOP, DIE_WHITE_BISHOP, DIE_BLACK_BISHOP
from board.board import position_in_board


class Bishop(Piece):

    def __init__(self, white, axis):
        Piece.__init__(self, white, WHITE_BISHOP if white else BLACK_BISHOP,
                       DIE_WHITE_BISHOP if white else DIE_BLACK_BISHOP, axis, "Bishop")
        self._houses = [(1, -1), (-1, -1), (1, 1), (-1, 1)]

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
