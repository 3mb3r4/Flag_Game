import pygame


# png file of soldier
# (x,y) coordinates of the top left corner of Soldier
# func to calculate legs and upper body positions
# checks out of bounds

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
    # TODO: handles out of bounds
    upper_left_corner = Screen.upper_left_soldier_coordinates()

    # handles movements
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

