"""Main file of game lights out."""
import game
import pygame

WIDTH, HEIGHT = 120*6, 120*6
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LIGHTS OUT")


def draw(clicks, end_game, list_of_lights):
    """Draw window of running game.

    :param int clicks: Number of player clicks.
    :param bool end_game: True if game is still going, False if it has already ended.
    :param list[game.OneLight] list_of_lights: List of objects representing lights on the board.
    """
    WIN.fill((102, 102, 102))
    font = pygame.font.SysFont('Arial', 30)
    text_moves = font.render(f'Number of moves: {clicks}', True, (0, 0, 0))
    WIN.blit(text_moves, (70, 660))
    for c in list_of_lights:
        c.draw(WIN)
    if not end_game:
        draw_win(clicks)
    pygame.display.update()


def draw_win(clicks):
    """Draw window after the win.

    :param int clicks: Number of player clicks.
    """
    WIN.fill((102, 102, 102))
    font2 = pygame.font.SysFont('Arial', 100)
    text_win = font2.render(f'WIN in {clicks} clicks', True, (250, 0, 0))
    text_rect = text_win.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    WIN.blit(text_win, text_rect)


def main():
    """Main game loop."""
    board = game.Board(5)
    end_game = False
    clicks = 0
    run = True
    while run:
        for light in board.list_of_lights:
            end_game |= light.state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if end_game:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for idx, circle in enumerate(board.list_of_lights):
                        if circle.is_point_in(event.pos):
                            board.switch_light(idx)
                            clicks += 1
                            print(idx)
        draw(clicks, end_game, board.list_of_lights)
        end_game = False
    pygame.quit()


if __name__ == "__main__":
    main()
