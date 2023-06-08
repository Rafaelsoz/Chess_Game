import pygame
from auxi.const import *


class Board:
    def __init__(self, screen):
        self.screen = screen

    def __draw_lines_in_board(self):

        for i in range(9):
            pygame.draw.line(self.screen, (0, 0, 0), (INITIAL_POSITION + (EDGE * i), INITIAL_POSITION),
                             (INITIAL_POSITION + (EDGE * i), END_POSITION))

            pygame.draw.line(self.screen, (0, 0, 0), (INITIAL_POSITION, INITIAL_POSITION + (EDGE * i)),
                             (END_POSITION, INITIAL_POSITION + (EDGE * i)))

    def __draw_board_dead_pieces(self):
        pygame.draw.rect(self.screen, DARK_GREEN, (END_POSITION + 40, INITIAL_POSITION, EDGE * 3 + 10, EDGE * 8))
        pygame.draw.rect(self.screen, (0, 0, 0), (END_POSITION + 40, INITIAL_POSITION, EDGE * 3 + 10, EDGE * 8), 2)

    def draw_board(self):

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
        self.__draw_lines_in_board()
        self.__draw_board_dead_pieces()


def position_in_board(axis):
    if 0 <= axis[0] < 8 and 0 <= axis[1] < 8:
        return True
    else:
        return False
