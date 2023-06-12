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
        self.over = False
        self.pause = False
        self.agreement = False
        self.turn_white = True
        self.white_pieces = []
        self.black_pieces = []
        self.winner = None
        self.round = 1
        self.white_score = 0
        self.black_score = 0
        self.moves_without_death = 0

        self.screen = screen
        self.board = Board(screen)

        self.__create_pieces()

    def reset(self, winner_or_tied):
        self.over = False
        self.turn_white = True
        self.white_pieces = []
        self.black_pieces = []
        self.winner = None
        self.moves_without_death = 0
        self.round += 1

        if winner_or_tied == 'White':
            self.white_score += 1
        elif winner_or_tied == 'Black':
            self.black_score += 1

        self.screen = self.screen
        self.board = Board(self.screen)

        self.__create_pieces()

    def change_turn(self):
        self.turn_white = False if self.turn_white is True else True

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

    def set_winner(self, winner_or_tied):
        self.winner = winner_or_tied

    def get_piece(self, class_piece, position, white):
        vector = []
        pieces = self.white_pieces if white else self.black_pieces

        if position:
            for piece in pieces:
                if isinstance(piece, class_piece):
                    vector.append(piece.position.get_position())
        else:
            for piece in pieces:
                if isinstance(piece, class_piece):
                    vector.append(piece)

        return vector

    def get_positions_of_living(self, king, white):
        vector = []
        pieces = self.white_pieces if white else self.black_pieces

        if king:
            for piece in pieces:
                if not piece.die:
                    vector.append(piece.position.get_position())
        else:
            for piece in pieces:
                if not isinstance(piece, King) and not piece.die:
                    vector.append(piece.position.get_position())

        return vector

    def get_status_pieces(self, king, white):
        vector = []
        pieces = self.white_pieces if white else self.black_pieces
        if king:
            for piece in pieces:
                vector.append(piece.die)
        else:
            for piece in pieces:
                if not isinstance(piece, King):
                    vector.append(piece.die)

        return vector

    def check_promotion(self):
        pieces = self.get_piece(Pawn, False, not self.turn_white)

        for piece in pieces:
            if not piece.die:
                if piece.position.axis_y == 0 or piece.position.axis_y == 7:
                    return True

    def promotion(self, new_class):
        pieces = self.black_pieces if self.turn_white else self.white_pieces

        for idx, piece in enumerate(pieces):
            if not piece.die and isinstance(piece, Pawn):
                if piece.position.axis_y == 0 or piece.position.axis_y == 7:
                    aux_rect = pieces[idx].dead_rect
                    aux_rect_x = pieces[idx].dead_rect.x
                    aux_rect_y = pieces[idx].dead_rect.y

                    pieces[idx] = new_class(not self.turn_white, piece.position.get_position())

                    pieces[idx].dead_rect = aux_rect
                    pieces[idx].dead_rect.x = aux_rect_x
                    pieces[idx].dead_rect.y = aux_rect_y

    def partners_and_enemies_positions(self, piece):
        partners = self.get_positions_of_living(True, piece.white)
        if isinstance(piece, King):
            enemies = self.get_piece(King, True, not piece.white)
        else:
            enemies = self.get_positions_of_living(True, not piece.white)

        return partners, enemies

    def drawing_pieces(self):
        color_pieces = [self.black_pieces, self.white_pieces] if self.turn_white else [self.white_pieces,
                                                                                       self.black_pieces]
        for i in range(2):
            for piece in color_pieces[i]:
                if piece.die is False:
                    self.board.drawing_image(piece.image, piece.rect)
                else:
                    self.board.drawing_dead_image(piece.dead_image, piece.dead_rect)

    def draw_check(self):
        if not self.over:
            kings_pos = [self.get_piece(King, True, True)[0],
                         self.get_piece(King, True, False)[0]]
            enemies = [self.black_pieces, self.white_pieces]

            for idx, king in enumerate(kings_pos):
                enemies_list = enemies[idx]
                for enemy in enemies_list:
                    if not enemy.die:
                        current_partners, current_enemies = self.partners_and_enemies_positions(enemy)
                        list_moves = enemy.moves_list(current_partners, current_enemies)

                        if len(list_moves) > 0 and king in list_moves:
                            self.board.draw_square(king, (204, 20, 20), (20, 20, 20))
                            break

    def draw_current_position(self, position):
        self.board.draw_square(position, BLUE, (20, 20, 20))

    def draw_moves_list(self, piece):
        if piece is not None:
            partners, enemies = self.partners_and_enemies_positions(piece)
            self.draw_current_position(piece.position.get_position())
            for new_pos in piece.moves_list(partners, enemies):
                self.board.draw_square(new_pos, GREEN, (20, 20, 20))

    def battle(self, piece):
        enemies = self.black_pieces if piece.white else self.white_pieces
        for enemy in enemies:
            if not enemy.die:
                if piece.position.get_position() == enemy.position.get_position():
                    enemy.die_piece()
                    return True
        return False

    def _only_kings(self):
        dead_white_pieces = self.get_status_pieces(False, True)
        dead_black_pieces = self.get_status_pieces(False, False)

        if all(dead_white_pieces) and all(dead_black_pieces):
            return True

    def _only_kings_and(self, class_target, white):
        target = self.get_piece(class_target, False, white)
        alive_target = 0
        for current in target:
            if not current.die:
                alive_target += 1

        if alive_target != 1:
            return False

        partners = self.white_pieces if white else self.black_pieces
        partners_status = []
        for ally in partners:
            if not isinstance(ally, class_target) and not isinstance(ally, King):
                partners_status.append(ally.die)

        enemies_status = self.get_status_pieces(False, not white)

        if alive_target == 1 and all(enemies_status) and all(partners_status):
            return True

        return False

    def a_tie(self):
        status = False
        if self._only_kings():
            status = True

        if self._only_kings_and(Knight, True) or self._only_kings_and(Knight, False):
            status = True

        if self._only_kings_and(Bishop, True) or self._only_kings_and(Bishop, False):
            status = True

        if self.moves_without_death >= 50:
            status = True

        return status

    def some_king_died(self):
        white_king = self.get_piece(King, False, True)[0]
        black_king = self.get_piece(King, False, False)[0]

        if white_king.die or black_king.die:
            return True
        else:
            return False
