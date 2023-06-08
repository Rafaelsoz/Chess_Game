import pygame
from auxi import const
from game import *
from auxi.position import calc_position
import sys
import os


def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = '80,80'

    pygame.init()

    screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
    screen.fill(const.BOARD_COLOR)
    pygame.display.set_caption("Chess")

    game = Game(screen)
    clock = pygame.time.Clock()

    '''Save id the current piece'''
    current_white_piece = None
    current_black_piece = None

    while True:
        clock.tick(60)

        game.board.draw_board()
        game.paint_moves_list(True, current_white_piece)
        game.paint_moves_list(False, current_black_piece)
        game.drawing_pieces()

        for event in pygame.event.get():
            '''Condition for ending the game'''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            '''Selection the piece'''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.turn_white is True:
                    for idx, piece in enumerate(game.white_pieces):
                        if piece is not None and piece.rect.collidepoint(event.pos):
                            piece.moving = True
                            current_white_piece = idx
                            current_black_piece = None

                else:
                    for idx, piece in enumerate(game.black_pieces):
                        if piece is not None and piece.rect.collidepoint(event.pos):
                            piece.moving = True
                            current_black_piece = idx
                            current_white_piece = None

            '''Mouse button activate'''
            if event.type == pygame.MOUSEMOTION:
                new_pos = calc_position(event.pos)
                if game.turn_white is True:
                    if current_white_piece is not None:
                        piece = game.white_pieces[current_white_piece]
                        if piece.moving:
                            if new_pos in piece.moves_list(game.white_pieces_locations, game.white_pieces_locations):
                                piece.mask_move(new_pos[0], new_pos[1])
                else:
                    if current_black_piece is not None:
                        piece = game.black_pieces[current_black_piece]
                        if piece.moving:
                            if new_pos in piece.moves_list(game.black_pieces_locations, game.white_pieces_locations):
                                piece.mask_move(new_pos[0], new_pos[1])

            '''Ending move the piece'''
            if event.type == pygame.MOUSEBUTTONUP:
                new_pos = calc_position(event.pos)
                if game.turn_white is True:
                    if current_white_piece is not None:
                        piece = game.white_pieces[current_white_piece]
                        if piece.moving:
                            if new_pos in piece.moves_list(game.white_pieces_locations, game.black_pieces_locations):
                                piece.move_piece(new_pos[0], new_pos[1])
                                game.save_piece_location(piece, current_white_piece)

                                game.battle(piece)

                                current_white_piece = None
                                piece.moving = False

                                game.change_turn()

                            else:
                                piece.return_piece()
                                current_white_piece = None
                                piece.moving = False
                else:
                    if current_black_piece is not None:
                        piece = game.black_pieces[current_black_piece]
                        if piece.moving:
                            if new_pos in piece.moves_list(game.black_pieces_locations, game.white_pieces_locations):
                                piece.move_piece(new_pos[0], new_pos[1])
                                game.save_piece_location(piece, current_black_piece)

                                game.battle(piece)

                                current_black_piece = None
                                piece.moving = False

                                game.change_turn()

                            else:
                                piece.return_piece()
                                current_black_piece = None
                                piece.moving = False

        pygame.display.update()


if __name__ == '__main__':
    main()
