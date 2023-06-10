import pygame.font
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
        self.game_over = False
        self.turn_white = True
        self.white_pieces = []
        self.black_pieces = []
        self.winner = None
        self.round = 1
        self.white_score = 0
        self.black_score = 0

        self.screen = screen
        self.board = Board(screen)

        self.__create_pieces()

    def reset(self, winner_or_tied):
        self.game_over = False
        self.turn_white = True
        self.white_pieces = []
        self.black_pieces = []
        self.winner = None
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
                if isinstance(piece, King) is False:
                    vector.append(piece.die)

        return vector

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
                    piece.drawing_image(self.screen)
                else:
                    piece.drawing_die_image(self.screen)

    def draw_game_over(self):
        if self.winner != 'Tied':
            end_msg = self.create_msg('Game Over :: Winner is {}'.format(self.winner), 40, WHITE_COLOR)
        else:
            end_msg = self.create_msg('Game Over :: Tied Game'.format(self.winner), 40, WHITE_COLOR)

        reset = self.create_msg('Press ENTER to restart', 25, WHITE_COLOR)

        pygame.draw.rect(self.screen, (40, 40, 40), (190, 240, 600, 170))
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (790, 240), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (190, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 410), (790, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (790, 240), (790, 410), 3)

        self.screen.blit(end_msg, (230, 280))
        self.screen.blit(reset, (355, 335))

    @staticmethod
    def create_msg(msg, size, color):
        font = pygame.font.SysFont('Times New Roman', size, True, False)
        text = font.render(msg, True, color)
        return text

    def paint_turn_game(self):
        msg = self.create_msg("Turn :: White pieces", 18, WHITE_COLOR if self.turn_white else (0, 0, 0))
        pos_text = msg.get_rect(topleft=(30, 6))
        self.screen.blit(msg, pos_text)

        msg = self.create_msg("Turn :: Black pieces", 18, (0, 0, 0) if self.turn_white else WHITE_COLOR)
        pos_text = msg.get_rect(bottomleft=(30, HEIGHT - 6))
        self.screen.blit(msg, pos_text)

    def paint_round(self):
        msg = self.create_msg('Round :: {}'.format(self.round), 18, WHITE_COLOR)
        pos_text = msg.get_rect(topright=(500, 5))
        self.screen.blit(msg, pos_text)

    def paint_score(self):
        scores = [self.white_score, self.black_score]
        for idx, score in enumerate(scores):
            msg = self.create_msg('Score :: {}'.format(score), 15, WHITE_COLOR)
            if idx == 0:
                pos_text = msg.get_rect(topright=(800, 5))
            else:
                pos_text = msg.get_rect(bottomleft=(735, 695))
            self.screen.blit(msg, pos_text)

    def paint_current_position(self, position):
        pygame.draw.rect(self.screen, BLUE, (position[0] * EDGE + INITIAL_POSITION, position[1] * EDGE
                                             + INITIAL_POSITION, EDGE, EDGE))
        pygame.draw.rect(self.screen, (20, 20, 20), (position[0] * EDGE + INITIAL_POSITION, position[1] * EDGE
                                                     + INITIAL_POSITION, EDGE, EDGE), 2)

    def paint_moves_list(self, piece):
        if piece is not None:
            partners, enemies = self.partners_and_enemies_positions(piece)
            self.paint_current_position(piece.position.get_position())
            for new_pos in piece.moves_list(partners, enemies):
                pygame.draw.rect(self.screen, BLACK_GREEN, (new_pos[0] * EDGE + INITIAL_POSITION, new_pos[1] * EDGE
                                                            + INITIAL_POSITION, EDGE, EDGE))
                pygame.draw.rect(self.screen, (20, 20, 20), (new_pos[0] * EDGE + INITIAL_POSITION, new_pos[1] * EDGE
                                                             + INITIAL_POSITION, EDGE, EDGE), 2)

    def battle(self, piece):
        enemies = self.black_pieces if piece.white else self.white_pieces
        for enemy in enemies:
            if not enemy.die:
                if piece.position.get_position() == enemy.position.get_position():
                    enemy.die_piece()

    def _king_die(self):
        white_king = self.get_piece(King, False, True)[0]
        black_king = self.get_piece(King, False, False)[0]

        if white_king.die or black_king.die:
            return True
        else:
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

        return status

    def check_mate(self):
        status = False
        if self._king_die():
            status = True

        return status
    