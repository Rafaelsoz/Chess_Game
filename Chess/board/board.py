import pygame.font
from auxi.const import *


class Board:
    def __init__(self, screen):
        self.screen = screen
        self._white_score = 0
        self._black_score = 0
        self._round = 1

    def _draw_lines_in_board(self):

        for i in range(9):
            pygame.draw.line(self.screen, (0, 0, 0), (INITIAL_POSITION + (EDGE * i), INITIAL_POSITION),
                             (INITIAL_POSITION + (EDGE * i), END_POSITION))

            pygame.draw.line(self.screen, (0, 0, 0), (INITIAL_POSITION, INITIAL_POSITION + (EDGE * i)),
                             (END_POSITION, INITIAL_POSITION + (EDGE * i)))

    def _draw_board_dead_pieces(self):
        pygame.draw.rect(self.screen, DARK_GREEN, (END_POSITION + 40, INITIAL_POSITION, EDGE * 3 + 10, EDGE * 8))
        pygame.draw.rect(self.screen, (0, 0, 0), (END_POSITION + 40, INITIAL_POSITION, EDGE * 3 + 10, EDGE * 8), 2)

    @staticmethod
    def _create_msg(msg, size, color):
        font = pygame.font.SysFont('Times New Roman', size, True, False)
        text = font.render(msg, True, color)
        return text

    def drawing_image(self, image, rect):
        self.screen.blit(image, rect)

    def drawing_dead_image(self, dead_image, dead_rect):
        self.screen.blit(dead_image, dead_rect)

    def draw_square(self, position, color_square, color_line):
        pygame.draw.rect(self.screen, color_square, (position[0] * EDGE + INITIAL_POSITION, position[1] * EDGE
                                                     + INITIAL_POSITION, EDGE, EDGE))
        pygame.draw.rect(self.screen, color_line, (position[0] * EDGE + INITIAL_POSITION, position[1] * EDGE
                                                   + INITIAL_POSITION, EDGE, EDGE), 2)

    def _draw_round(self, round_game):
        msg = self._create_msg('Round :: {}'.format(round_game), 22, WHITE_COLOR)
        pos_text = msg.get_rect(topright=(500, 5))
        self.screen.blit(msg, pos_text)

    def _draw_moves_without_death(self, moves_without_death):
        msg = self._create_msg('Moves without death :: {}'.format(moves_without_death), 21, WHITE_COLOR)
        pos_text = msg.get_rect(bottomleft=(350, 698))
        self.screen.blit(msg, pos_text)

    def _draw_score(self, white_score, black_score):
        scores = [white_score, black_score]
        for idx, score in enumerate(scores):
            msg = self._create_msg('Score :: {}'.format(score), 17, WHITE_COLOR)
            if idx == 0:
                pos_text = msg.get_rect(topright=(800, 7))
            else:
                pos_text = msg.get_rect(bottomleft=(735, 695))
            self.screen.blit(msg, pos_text)

    def _draw_turn_game(self, turn_white):
        msg = self._create_msg("Turn :: White pieces", 18, WHITE_COLOR if turn_white else (0, 0, 0))
        pos_text = msg.get_rect(topleft=(30, 6))
        self.screen.blit(msg, pos_text)

        msg = self._create_msg("Turn :: Black pieces", 18, (0, 0, 0) if turn_white else WHITE_COLOR)
        pos_text = msg.get_rect(bottomleft=(30, HEIGHT - 6))
        self.screen.blit(msg, pos_text)

    def draw_promotion(self):
        msg = self._create_msg('Hear a promotion make your choice', 35, WHITE_COLOR)
        choice = self._create_msg('B: Bishop      K: Knight      R: Rook      Q: Queen', 20, WHITE_COLOR)

        pygame.draw.rect(self.screen, (40, 40, 40), (190, 240, 600, 170))
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (790, 240), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (190, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 410), (790, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (790, 240), (790, 410), 3)

        self.screen.blit(msg, (222, 280))
        self.screen.blit(choice, (305, 335))

    def draw_agreement(self, turn_white):
        if turn_white:
            text = 'White king asks for a draw, do you accept?'
        else:
            text = 'Black king asks for a draw, do you accept?'

        msg = self._create_msg(text, 30, WHITE_COLOR)
        choice = self._create_msg('y: Yes      N: No', 38, WHITE_COLOR)

        pygame.draw.rect(self.screen, (40, 40, 40), (190, 240, 600, 170))
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (790, 240), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (190, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 410), (790, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (790, 240), (790, 410), 3)

        self.screen.blit(msg, (220, 280))
        self.screen.blit(choice, (360, 335))

    def draw_game_over(self, winner):
        if winner != 'Tied':
            end_msg = self._create_msg('Game Over :: Winner is {}'.format(winner), 40, WHITE_COLOR)
            pos = (230, 280)
        else:
            end_msg = self._create_msg('Game Over :: Tied Game'.format(winner), 40, WHITE_COLOR)
            pos = (265, 280)

        reset = self._create_msg('Press ENTER to restart', 25, WHITE_COLOR)

        pygame.draw.rect(self.screen, (40, 40, 40), (190, 240, 600, 170))
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (790, 240), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 240), (190, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (190, 410), (790, 410), 3)
        pygame.draw.line(self.screen, WHITE_COLOR, (790, 240), (790, 410), 3)

        self.screen.blit(end_msg, pos)
        self.screen.blit(reset, (355, 335))

    def draw_board(self, turn_white, moves_without_death):

        self.screen.fill(BOARD_COLOR)

        for axis_x in range(8):
            for axis_y in range(8):
                if (axis_x + axis_y) % 2 == 0:
                    pygame.draw.rect(self.screen, DARK_GREEN, (INITIAL_POSITION + (axis_x * EDGE),
                                                               INITIAL_POSITION + (axis_y * EDGE),
                                                               EDGE, EDGE))
                else:
                    pygame.draw.rect(self.screen, WHITE_COLOR, (INITIAL_POSITION + (axis_x * EDGE),
                                                                INITIAL_POSITION + (axis_y * EDGE),
                                                                EDGE, EDGE))

        self._draw_lines_in_board()
        self._draw_board_dead_pieces()
        self._draw_turn_game(turn_white)
        self._draw_round(self._round)
        self._draw_score(self._white_score, self._black_score)
        self._draw_moves_without_death(moves_without_death)

    def reset_board(self, winner_or_tied):
        self._round += 1
        if winner_or_tied == 'White':
            self._white_score += 1
        elif winner_or_tied == 'Black':
            self._black_score += 1


def position_in_board(axis):
    if 0 <= axis[0] < 8 and 0 <= axis[1] < 8:
        return True
    else:
        return False
