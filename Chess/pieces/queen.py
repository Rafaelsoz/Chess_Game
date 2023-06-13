from piece import Piece
from auxi.const import WHITE_QUEEN, BLACK_QUEEN, DIE_WHITE_QUEEN, DIE_BLACK_QUEEN
from board.board import position_in_board


class Queen(Piece):

    def __init__(self, white, axis):
        Piece.__init__(self, white, WHITE_QUEEN if white else BLACK_QUEEN,
                       DIE_WHITE_QUEEN if white else DIE_BLACK_QUEEN, axis, "Queen")
        self._diagonal_houses = [(1, -1), (-1, -1), (1, 1), (-1, 1)]
        self._horizontal_houses = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        moves = []

        '''Bishop movies'''
        for house in self._diagonal_houses:
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

        '''Rook movies'''
        for house in self._horizontal_houses:
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

        self.valid_moves = moves

        return self.valid_moves
