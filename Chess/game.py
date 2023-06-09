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

        self.white_pieces_locations = [None] * 16
        self.black_pieces_locations = [None] * 16

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

        self.white_pieces_locations = [None] * 16
        self.black_pieces_locations = [None] * 16

        self.screen = self.screen
        self.board = Board(self.screen)

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
        position = [(800, 5), (800, 990)]
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

    def set_winner(self, winner_or_tied):
        self.winner = winner_or_tied

    def battle(self, piece):
        if piece.white:
            for idx, enemy in enumerate(self.black_pieces):
                if piece.position.get_position() == enemy.position.get_position():
                    enemy.die_piece()
                    self.black_pieces_locations[idx] = None

        else:
            for idx, enemy in enumerate(self.white_pieces):
                if piece.position.get_position() == enemy.position.get_position():
                    enemy.die_piece()
                    self.white_pieces_locations[idx] = None

    def _king_die(self):
        white_king = self.white_pieces[KING_IDX]
        black_king = self.black_pieces[KING_IDX]

        if white_king.die is True or black_king.die is True:
            return True
        else:
            return False

    def _only_kings(self):
        dead_white_pieces = list([piece.die for piece in self.white_pieces])
        dead_white_pieces.pop(KING_IDX)

        dead_black_pieces = list([piece.die for piece in self.black_pieces])
        dead_black_pieces.pop(KING_IDX)

        if all(dead_white_pieces) is True and all(dead_black_pieces) is True:
            return True

    def _get_dead_pieces(self, white):
        if white:
            return list([piece.die for piece in self.white_pieces])
        else:
            return list([piece.die for piece in self.black_pieces])

    def _get_target_alive(self, white, class_):
        idx = None

        if white:
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces

        if isinstance(class_, Knight):
            idx = KNIGHT_IDX
        elif isinstance(class_, Bishop):
            idx = BISHOP_IDX

        if idx is not None:
            dead_target_pieces = [pieces[idx[0]].die, pieces[idx[1]].die]
            amount = 0

            for piece in dead_target_pieces:
                if piece is False:
                    amount += 1

            return amount

    def _only_kings_and_knight(self):

        amount_white_knight = self._get_target_alive(True, Knight)
        amount_black_knight = self._get_target_alive(False, Knight)

        dead_white_pieces = self._get_dead_pieces(True)
        dead_white_pieces.pop(KING_IDX)
        dead_white_pieces.pop(KNIGHT_IDX[0])
        dead_white_pieces.pop(KNIGHT_IDX[1])

        dead_black_pieces = self._get_dead_pieces(False)
        dead_black_pieces.pop(KING_IDX)
        dead_black_pieces.pop(KNIGHT_IDX[0])
        dead_black_pieces.pop(KNIGHT_IDX[1])

        if amount_white_knight == 1 and amount_black_knight == 0 and all(dead_black_pieces):
            return True

        if amount_white_knight == 0 and amount_black_knight == 1 and all(dead_white_pieces):
            return True

        return False

    def _only_king_and_bishop(self):
        pass

    def a_tie(self):

        if self._only_kings():
            return True

        if self._only_kings_and_knight():
            return True

        if self._only_king_and_bishop():
            return True

        else:
            return False

    def check_mate(self):

        if self._king_die():
            return True

        else:
            return False
