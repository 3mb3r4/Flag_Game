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
        i = random.randint(0, const.NUM_SQUARES_HEIGHT)
        j = random.randint(0, const.NUM_SQUARES_WIDTH)
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
                pos = (j, i)
                mines_indexes_list.append(pos)

