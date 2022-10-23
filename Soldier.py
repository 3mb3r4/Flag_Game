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

def player_touches_mine(player_legss_indexes, mines_indexes):