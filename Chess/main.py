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

    '''Save piece'''
    current_piece = None

    while True:
        clock.tick(60)

        game.board.draw_board()
        game.paint_turn_game()
        game.paint_round()
        game.paint_score()
        game.paint_moves_list(current_piece)
        game.drawing_pieces()

        for event in pygame.event.get():

            '''Condition for ending the game'''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            '''Selection the piece'''
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                pieces = game.white_pieces if game.turn_white else game.black_pieces
                for piece in pieces:
                    if piece is not None and piece.rect.collidepoint(event.pos):
                        piece.moving = True
                        current_piece = piece

            '''Mouse button activate'''
            if event.type == pygame.MOUSEMOTION and not game.game_over:
                new_pos = calc_position(event.pos)

                if current_piece is not None and current_piece.moving:
                    partners, enemies = game.partners_and_enemies_positions(current_piece)

                    if new_pos in current_piece.moves_list(partners, enemies):
                        current_piece.mask_move(new_pos[0], new_pos[1])

            '''Ending move the piece'''
            if event.type == pygame.MOUSEBUTTONUP and not game.game_over:
                text_winner = 'White' if game.turn_white else 'Black'

                new_pos = calc_position(event.pos)

                if current_piece is not None and current_piece.moving:
                    partners, enemies = game.partners_and_enemies_positions(current_piece)

                    if new_pos in current_piece.moves_list(partners, enemies):
                        current_piece.move_piece(new_pos[0], new_pos[1])

                        game.battle(current_piece)

                        if game.check_mate():
                            game.set_winner(text_winner)

                        if game.a_tie():
                            game.set_winner('Tied')

                        current_piece.moving = False
                        current_piece = None

                        game.change_turn()

                    else:
                        current_piece.return_piece()
                        current_piece.moving = False
                        current_piece = None

            if event.type == pygame.KEYDOWN and game.game_over:
                if event.key == pygame.K_RETURN:
                    current_piece = None
                    game.reset(game.winner)
                    screen.fill(const.BOARD_COLOR)

        if game.winner is not None:
            game.game_over = True
            game.draw_game_over()

        pygame.display.update()


if __name__ == '__main__':
    main()
