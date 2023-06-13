from auxi.position import Position
from auxi.const import INITIAL_POSITION, END_POSITION, EDGE, WIDTH, HEIGHT


class Piece:

    def __init__(self, white, image, die_image, axis, name):
        self.name = name
        self.image = image
        self.dead_image = die_image
        self.die = False
        self.valid_moves = None
        self.white = white
        self.moving = False

        self.position = Position(axis[0], axis[1])
        self.second_position = Position(axis[0], axis[1])

        self.rect = self.image.get_rect()
        self.rect.x = INITIAL_POSITION + self.position.axis_x * EDGE
        self.rect.y = INITIAL_POSITION + self.position.axis_y * EDGE

        self.dead_piece_position = Position(axis[1] * 25 + END_POSITION + 60,
                                            INITIAL_POSITION + 20 + axis[0] * EDGE)

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        pass

    def move_piece(self, axis_x, axis_y):
        self.move(axis_x, axis_y)

    def move(self, axis_x, axis_y):
        self.position = Position(axis_x, axis_y)

        self.rect.x = INITIAL_POSITION + self.position.axis_x * EDGE
        self.rect.y = INITIAL_POSITION + self.position.axis_y * EDGE

    def mask_move(self, axis_x, axis_y):
        self.second_position = Position(axis_x, axis_y)

        self.rect.x = INITIAL_POSITION + self.second_position.axis_x * EDGE
        self.rect.y = INITIAL_POSITION + self.second_position.axis_y * EDGE

    def return_piece(self):
        self.rect.x = INITIAL_POSITION + self.position.axis_x * EDGE
        self.rect.y = INITIAL_POSITION + self.position.axis_y * EDGE

    def die_piece(self):
        self.die = True
        self.position.axis_x = None
        self.position.axis_y = None
        self.position = None

        self.rect.x = WIDTH
        self.rect.y = HEIGHT
