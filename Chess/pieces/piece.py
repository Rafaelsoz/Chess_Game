from auxi.position import Position
from auxi.const import INITIAL_POSITION, END_POSITION, EDGE, WIDTH, HEIGHT


class Piece:

    def __init__(self, white, image, die_image, axis, name):
        self.name = name
        self.image = image
        self.die = False
        self.die_image = die_image
        self.valid_movies = None
        self.white = white

        self.current_position = Position(axis[0], axis[1])
        self.position = Position(axis[0], axis[1])
        self.rect = self.image.get_rect()
        self.rect.x = INITIAL_POSITION + self.position.axis_x * EDGE
        self.rect.y = INITIAL_POSITION + self.position.axis_y * EDGE

        self.die_piece_position = Position(axis[1], axis[0])
        self.die_rect = self.die_image.get_rect()
        self.die_rect.x = self.die_piece_position.axis_x * 25 + END_POSITION + 60
        self.die_rect.y = INITIAL_POSITION + 20 + self.die_piece_position.axis_y * EDGE

        self.second_current_position = Position(axis[0], axis[1])
        self.second_position = Position(axis[0], axis[1])

        self.moving = False

    def get_name(self):
        return self.name

    def drawing_image(self, screen):
        screen.blit(self.image, self.rect)

    def drawing_die_image(self, screen):
        screen.blit(self.die_image, self.die_rect)

    def moves_list(self, partners_pieces_location, enemies_pieces_locations):
        pass

    def move_piece(self, axis_x, axis_y):
        self.move(axis_x, axis_y)

    def move(self, axis_x, axis_y):
        self.current_position.axis_x = axis_x
        self.current_position.axis_y = axis_y

        self.position = self.current_position

        self.rect.x = INITIAL_POSITION + self.position.axis_x * EDGE
        self.rect.y = INITIAL_POSITION + self.position.axis_y * EDGE

    def mask_move(self, axis_x, axis_y):
        self.second_current_position.axis_x = axis_x
        self.second_current_position.axis_y = axis_y

        self.second_position = self.second_current_position

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

        self.second_current_position.axis_x = None
        self.second_current_position.axis_y = None
        self.second_current_position = None

        self.rect.x = WIDTH
        self.rect.y = HEIGHT
