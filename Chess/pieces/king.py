from piece import Piece
from auxi.const import WHITE_KING, BLACK_KING, DIE_WHITE_KING, DIE_BLACK_KING
from board.board import position_in_board


class King(Piece):

    def __init__(self, white, axis):
        Piece.__init__(self, white, WHITE_KING if white else BLACK_KING,
                       DIE_WHITE_KING if white else DIE_BLACK_KING, axis, "King")
        self.houses = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        moves = []
        for house in self.houses:

            new_pos = (self.position.axis_x + house[0],
                       self.position.axis_y + house[1])

            if new_pos not in partners_pieces_location and new_pos not in enemies_pieces_locations:
                if position_in_board(new_pos):
                    moves.append(new_pos)

        self.valid_movies = moves

        return self.valid_movies
