import Screen
import const
import random

mine_grid = []


def make_empty_field():
    # makes empty minefield, according to the screen sizes in consts
    for i in range(const.NUM_SQUARES_HEIGHT):
        sub_list = []
        for j in range(const.NUM_SQUARES_WIDTH):
            sub_list.append(const.EMPTY_VALUE)
        mine_grid.append(sub_list)


def create_random_mines(flag_indexes):
    # creates mines at random places according to num of mines specified in consts
    num_of_mines = 0

    while num_of_mines < const.NUM_OF_MINES:
        i = random.randint(0, const.NUM_SQUARES_HEIGHT - 1)
        j = random.randint(0, const.NUM_SQUARES_WIDTH - 4)
        # to make sure mines don't spawn outside screen
        if mine_grid[i][j] == const.EMPTY_VALUE and (i, j) not in const.DONT_SPAWN_MINES_LIST \
                and (i, j) not in flag_indexes:  # to make sure a win isn't impossible
            mine_grid[i][j] = const.MINE_VALUE
            num_of_mines += 1


def print_mine_matrix():
    # a function for developing part only, to check the mine grid is working
    # function isn't in use in the game itself
    for i in range(len(mine_grid)):
        for j in range(len(mine_grid[i])):
            print(mine_grid[i][j], end=" ")
        print()


def mine_indexes_list():
    # return list of mines indexes
    mines_indexes_list = []
    for i in range(len(mine_grid)):
        for j in range(len(mine_grid[i])):
            if mine_grid[i][j] == const.MINE_VALUE:
                pos = [j, i]
                mines_indexes_list.append(pos)
    return mines_indexes_list


def get_flag_index(flag_start_pos):
    # return a list of the flag indexes on the matrix
    start_index = list(Screen.conversion_to_position(flag_start_pos))
    flag_indexes = [start_index]

    for i in range(3):  # flag height
        for j in range(4):  # flag width
            pos = [start_index[0] + j, start_index[1] + i]
            if pos == start_index:  # the first item will be the same as the start index, so we skip it
                continue
            flag_indexes.append(pos)
    return flag_indexes
