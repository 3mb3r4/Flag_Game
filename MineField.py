import Screen
import const
import Soldier
import random

# saves flag and mines placements
# creates random placements of mines


mine_grid = []


def make_empty_field():
    for i in range(const.NUM_SQUARES_HEIGHT):
        sub_list = []
        for j in range(const.NUM_SQUARES_WIDTH):
            sub_list.append(const.EMPTY_VALUE)
        mine_grid.append(sub_list)


def create_random_mines():
    num_of_mines = 0
    while num_of_mines < 20:
        i = random.randint(0, const.NUM_SQUARES_HEIGHT - 1)
        j = random.randint(0, const.NUM_SQUARES_WIDTH - 4)
        if mine_grid[i][j] == const.EMPTY_VALUE:
            mine_grid[i][j] = const.MINE_VALUE
            num_of_mines += 1


def print_mine_matrix():
    for i in range(len(mine_grid)):
        for j in range(len(mine_grid[i])):
            print(mine_grid[i][j], end=" ")
        print()


def mine_indexes_list():
    mines_indexes_list = []
    for i in range(len(mine_grid)):
        for j in range(len(mine_grid[i])):
            if mine_grid[i][j] == const.MINE_VALUE:
                pos = [j, i]
                mines_indexes_list.append(pos)
    return mines_indexes_list


def get_flag_index(flag_start_pos):
    start_index = Screen.conversion_to_position(flag_start_pos)
    start_index = list(start_index)
    flag_indexes = [start_index]

    for i in range(3):
        for j in range(4):
            pos = [start_index[0] + j, start_index[1] + i]
            if pos == start_index:
                continue
            flag_indexes.append(pos)
    return flag_indexes

