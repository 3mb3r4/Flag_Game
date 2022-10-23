import pygame
import Screen
import const


# TODO: func to calculate legs and upper body positions

def player_pos_start():
    player_png = pygame.image.load("C:\\Users\\jbt\\PycharmProjects\\Flag_Game\\soldier.png")
    pos = (0, 0)
    return player_png, pos


def player_touches_flag(player_body_indexes, flag_indexes):
    parts_touching_flag = 0
    for position in player_body_indexes:
        if position in flag_indexes:
            parts_touching_flag += 1
    return parts_touching_flag >= 4


def player_touches_mine(player_legs_indexes, mines_indexes):
    parts_touching_mine = 0
    for position in player_legs_indexes:
        if position in mines_indexes:
            parts_touching_mine += 1
    return parts_touching_mine >= 2


def movement(key_pressed, player_index, player_png):
    upper_left_corner = Screen.get_upper_left_soldier_coordinates()
    player_width = player_png.get_width()
    player_height = player_png.get_height()

    if upper_left_corner[0] != 0 and upper_left_corner[0] != const.WINDOW_WIDTH - player_width and \
            upper_left_corner[1] != 0 and upper_left_corner[1] != const.WINDOW_HEIGHT - player_height:
        # then player won't move put of bounds
        if key_pressed == pygame.K_UP:
            for pos in player_index:
                pos[0] += 1

        elif key_pressed == pygame.K_DOWN:
            for pos in player_index:
                pos[0] -= 1

        elif key_pressed == pygame.K_RIGHT:
            for pos in player_index:
                pos[1] += 1

        else:
            for pos in player_index:
                pos[1] -= 1


def player_pos_in_matrix_list(start_pos):
    player_pos_list = [start_pos]
    for i in range(0, 2):
        x = start_pos[0] + i
        for j in range(0, 4):
            y = start_pos[1] + j
            player_pos_list.append((x, y))
    return player_pos_list
