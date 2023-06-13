from piece import Piece
from auxi.const import WHITE_PAWN, BLACK_PAWN, DIE_BLACK_PAWN, DIE_WHITE_PAWN
from board.board import position_in_board


class Pawn(Piece):

    def __init__(self, white, axis):
        Piece.__init__(self, white, WHITE_PAWN if white else BLACK_PAWN,
                       DIE_WHITE_PAWN if white else DIE_BLACK_PAWN, axis, "Pawn")
        self._first_move = True

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        moves = []
        '''Movements for feet in board'''
        if self._first_move:
            houses = [1, 2] if self.white else [-1, -2]
            for i in range(2):
                new_pos = (self.position.axis_x, self.position.axis_y + houses[i])
                if new_pos not in partners_pieces_location:
                    if new_pos not in enemies_pieces_locations and position_in_board(new_pos):
                        moves.append(new_pos)
        else:
            houses = 1 if self.white else -1
            new_pos = (self.position.axis_x, self.position.axis_y + houses)
            if new_pos not in partners_pieces_location:
                if new_pos not in enemies_pieces_locations and position_in_board(new_pos):
                    moves.append(new_pos)

        '''Movements for battle'''
        houses = 1 if self.white else -1

        pos_attack_1 = (self.position.axis_x + 1, self.position.axis_y + houses)
        if pos_attack_1 in enemies_pieces_locations and position_in_board(pos_attack_1):
            moves.append(pos_attack_1)

        pos_attack_2 = (self.position.axis_x - 1, self.position.axis_y + houses)
        if pos_attack_2 in enemies_pieces_locations and position_in_board(pos_attack_2):
            moves.append(pos_attack_2)

        self.valid_moves = moves

        return self.valid_moves

    def move_piece(self, axis_x, axis_y):
        self.move(axis_x, axis_y)
        self._first_move = False
