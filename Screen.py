import pygame
import const
import MineField
import random
import time

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


def conversion_to_position(indexes):
    x, y = indexes[0] // const.SQUARE_SIZE, indexes[1] // const.SQUARE_SIZE
    indexes = x, y
    return indexes


def draw_message(message):
    font = pygame.font.SysFont(const.FONT_NAME, const.FONT_SIZE)
    text_img = font.render(message, True, const.MESSAGE_COLOR)
    screen.blit(text_img, const.MESSAGE_LOCATION)


def draw_lose_message():
    draw_message(const.LOSE_MESSAGE)


def draw_win_message():
    draw_message(const.WIN_MESSAGE)


def draw_side_message():
    font = pygame.font.SysFont(const.FONT_NAME, const.SIDE_MESSAGE_FONT_SIZE)
    text_1_img = font.render(const.SIDE_MESSAGE_1, True, const.SIDE_MESSAGE_COLOR)
    screen.blit(text_1_img, const.SIDE_MESSAGE_1_LOCATION)
    text_2_img = font.render(const.SIDE_MESSAGE_2, True, const.SIDE_MESSAGE_COLOR)
    screen.blit(text_2_img, const.SIDE_MESSAGE_2_LOCATION)


def draw_game(game_state, player_position, player_png, bushes_list):
    screen.fill(const.BACKGROUND_COLOR)
    player_x_y = conversion_to_coordinates(player_position)
    draw_bushes(bushes_list)
    draw_object(const.FLAG_START_POS, const.FlAG_PNG)
    draw_object(player_x_y, player_png)
    draw_side_message()
    wait_time = 0

    if game_state == const.ENTER_STATE:
        visualize_grid()
        draw_mines()
        draw_object(player_x_y, const.NIGHT_SOLDIER_PNG)
        wait_time = 1
    elif game_state == const.WIN_STATE:
        current_time = pygame.time.get_ticks()
        pause_time = current_time + const.SECOND * 5
        if pause_time > current_time:
            draw_win_message()
        wait_time = 3

    elif game_state == const.LOSE_STATE:
        current_time = pygame.time.get_ticks()
        pause_time = current_time + const.SECOND * 5
        if pause_time > current_time:
            draw_lose_message()
        wait_time = 3

    pygame.display.flip()
    if wait_time != 0:
        pygame.time.delay(const.SECOND * wait_time)
