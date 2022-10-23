import pygame
import const
import MineField
import random
import Soldier

screen = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
screen.fill(const.BACKGROUND_COLOR)


def random_bushes_list():
    random_bushes_indexes = []
    for i in range(const.SQUARE_SIZE):
        x = random.randint(0, const.WINDOW_WIDTH - const.BUSH_WIDTH)
        y = random.randint(0, const.WINDOW_HEIGHT - const.BUSH_HEIGHT)
        index = (x, y)
        random_bushes_indexes.append(index)
    return random_bushes_indexes


def draw_bushes(bushes_list):
    for bush in bushes_list:
        x, y = bush[0], bush[1]
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
    for i in range(const.SQUARE_SIZE, pixel_y_end, const.SQUARE_SIZE):
        point1 = (0, i)
        point2 = (pixel_x_end, i)
        pygame.draw.line(screen, const.LINE_COLOR, point1, point2)

    for i in range(const.SQUARE_SIZE, pixel_x_end, const.SQUARE_SIZE):
        point1 = (i, 0)
        point2 = (i, pixel_y_end)
        pygame.draw.line(screen, const.LINE_COLOR, point1, point2)


def draw_object(coordinates, png):
    conversion_to_coordinates(coordinates)
    x, y = coordinates[0], coordinates[1]
    screen.blit(png, (x, y))


def conversion_to_coordinates(coordinates):
    x, y = coordinates[0] * const.SQUARE_SIZE, coordinates[1] * const.SQUARE_SIZE
    coordinates = (x, y)
    return coordinates


def draw_message(message):
    font = pygame.font.SysFont(const.FONT_NAME, const.FONT_SIZE)
    text_img = font.render(message, True, const.MESSAGE_COLOR)
    screen.blit(text_img, const.MESSAGE_LOCATION)


def draw_lose_message():
    draw_message(const.LOSE_MESSAGE)


def draw_win_message():
    draw_message(const.WIN_MESSAGE)


def draw_game(game_state, player_position, player_png, bushes_list):
    screen.fill(const.BACKGROUND_COLOR)
    draw_object(player_position, player_png)
    draw_object(const.FLAG_START_POS, const.FlAG_PNG)
    draw_bushes(bushes_list)

    if game_state == const.ENTER_STATE:
        visualize_grid()
        draw_mines()
        pygame.time.delay(const.SECOND)
    elif game_state == const.WIN_STATE:
        draw_win_message()
        pygame.time.delay(const.SECOND * 3)

    elif game_state == const.LOSE_STATE:
        draw_lose_message()
        pygame.time.delay(const.SECOND * 3)

    pygame.display.flip()
