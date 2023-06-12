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

        game.screen.fill(const.BOARD_COLOR)
        game.board.draw_board()
        game.board.draw_turn_game(game.turn_white)
        game.board.draw_round(game.round)
        game.board.draw_score(game.white_score, game.black_score)
        game.board.draw_moves_without_death(game.moves_without_death)
        game.draw_moves_list(current_piece)
        game.draw_check()
        game.drawing_pieces()

        for event in pygame.event.get():

            '''Condition for ending the game'''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            '''Selection the piece'''
            if event.type == pygame.MOUSEBUTTONDOWN and not game.over and not game.pause:
                pieces = game.white_pieces if game.turn_white else game.black_pieces
                for piece in pieces:
                    if piece is not None and piece.rect.collidepoint(event.pos):
                        piece.moving = True
                        current_piece = piece

            '''Mouse button activate'''
            if event.type == pygame.MOUSEMOTION and not game.over and not game.pause:
                new_pos = calc_position(event.pos)

                if current_piece is not None and current_piece.moving:
                    partners, enemies = game.partners_and_enemies_positions(current_piece)

                    if new_pos in current_piece.moves_list(partners, enemies):
                        current_piece.mask_move(new_pos[0], new_pos[1])

            '''Ending move the piece'''
            if event.type == pygame.MOUSEBUTTONUP and not game.over and not game.pause:
                text_winner = 'White' if game.turn_white else 'Black'

                new_pos = calc_position(event.pos)

                if current_piece is not None and current_piece.moving:
                    partners, enemies = game.partners_and_enemies_positions(current_piece)

                    if new_pos in current_piece.moves_list(partners, enemies):
                        current_piece.move_piece(new_pos[0], new_pos[1])

                        if game.battle(current_piece):
                            game.moves_without_death = 0
                        else:
                            game.moves_without_death += 1

                        if game.some_king_died():
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

            if event.type == pygame.KEYDOWN and game.over:
                if event.key == pygame.K_RETURN:
                    current_piece = None
                    game.reset(game.winner)
                    screen.fill(const.BOARD_COLOR)

            if event.type == pygame.KEYDOWN and game.pause:
                if event.key == pygame.K_b:
                    game.pause = False
                    game.promotion(Bishop)
                elif event.key == pygame.K_k:
                    game.pause = False
                    game.promotion(Knight)
                elif event.key == pygame.K_r:
                    game.pause = False
                    game.promotion(Rook)
                elif event.key == pygame.K_q:
                    game.pause = False
                    game.promotion(Queen)

            if event.type == pygame.KEYDOWN and not game.pause:
                if event.key == pygame.K_t:
                    game.pause = True
                    game.agreement = True

            if event.type == pygame.KEYDOWN and game.agreement:
                if event.key == pygame.K_y:
                    game.pause = False
                    game.agreement = False
                    game.set_winner('Tied')

            if event.type == pygame.KEYDOWN and game.agreement:
                if event.key == pygame.K_n:
                    game.pause = False
                    game.agreement = False

        if game.agreement:
            game.board.draw_agreement(game.turn_white)

        if game.check_promotion() and not game.over:
            game.pause = True
            game.board.draw_promotion()

        if game.winner is not None and not game.pause:
            game.over = True
            game.board.draw_game_over(game.winner)

        pygame.display.update()


if __name__ == '__main__':
    main()
