import pygame
import Screen
import const


# TODO: (x,y) coordinates of the top left corner of Soldier
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


def movement(key_pressed, player_index):
    upper_left_corner = Screen.upper_left_soldier_coordinates()
    player_width = Screen.get_player_width()
    player_height = Screen.get_player_height()

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

    # handles movements
