from piece import Piece
from auxi.const import WHITE_KNIGHT, BLACK_KNIGHT, DIE_BLACK_KNIGHT, DIE_WHITE_KNIGHT
from board.board import position_in_board


class Knight(Piece):

    def __init__(self, white, axis):
        Piece.__init__(self, white, WHITE_KNIGHT if white else BLACK_KNIGHT,
                       DIE_WHITE_KNIGHT if white else DIE_BLACK_KNIGHT, axis, "Knight")
        self._houses = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        moves = []

        for house in self._houses:

            new_pos = (self.position.axis_x + house[0],
                       self.position.axis_y + house[1])

            if new_pos not in partners_pieces_location and position_in_board(new_pos):
                moves.append(new_pos)

        self.valid_movies = moves

        return self.valid_movies
