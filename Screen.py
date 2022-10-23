import pygame
import const
import MineField
import random

screen = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
screen.fill(const.BACKGROUND_COLOR)


def draw_random_bushes():
    random_bushes_indexes = []
    for i in range(const.SQUARE_SIZE):
        x = random.randint(0, const.NUM_SQUARES_WIDTH - const.BUSH_WIDTH)
        y = random.randint(0, const.NUM_SQUARES_HEIGHT - const.BUSH_HEIGHT)
        index = (x, y)
        random_bushes_indexes.append(index)
    for bush in random_bushes_indexes:
        x, y = bush
        screen.blit(const.BUSH_PNG, (x, y))


def draw_mines():
    for item in MineField.mine_indexes_list():
        x, y = item
        screen.blit(const.MINE_PNG, (x * const.SQUARE_SIZE, y * const.SQUARE_SIZE))


def visualize_grid():
    screen.fill(const.MINES_BACKGROUND_COLOR)
    pixel_x = 0
    pixel_y = 0
    pixel_x_end = const.WINDOW_WIDTH
    pixel_y_end = const.WINDOW_HEIGHT
    while pixel_y != const.WINDOW_HEIGHT + const.SQUARE_SIZE:
        pygame.draw.line(screen, const.LINE_COLOR, (pixel_x, pixel_y), (pixel_x_end, pixel_y))
        pixel_y += const.SQUARE_SIZE
    while pixel_x != const.WINDOW_WIDTH + const.SQUARE_SIZE:
        pygame.draw.line(screen, const.LINE_COLOR, (pixel_x, pixel_y), (pixel_x, pixel_y_end))
        pixel_x += const.SQUARE_SIZE


def create_player():
    pass


def object_draw():
    pass


def draw_game(game_state):
    screen.fill(const.BACKGROUND_COLOR)
    draw_random_bushes()
    if game_state == const.ENTER_STATE:
        visualize_grid()
        draw_mines()
        pygame.time.delay(const.SECOND)
    elif game_state == const.WIN_STATE:
        # draw win message for 3 sec
        pass
    elif game_state == const.LOSE_STATE:
        # draw lise state for 3 sec
        pass

    pygame.display.flip()