import pygame
import MineField
import Screen
import Soldier
import const

# handling pygame events

game = {"run": True,
        "mines_pos": [],
        "movements_keys": [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT],
        "flag_indexes": Screen.get_flag_indexes,
        "game_state": const.RUNNING_STATE}


def main():
    pygame.init()
    MineField.make_empty_field()
    MineField.create_random_mines()
    game["mines_pos"] = MineField.mine_indexes_list()
    player_png, player_pos = Soldier.player_pos_start()

    while game["run"]:
        handle_user_events()

        # check player touches flag
        player_index = Screen.get_player_index()
        if Soldier.player_touches_flag(player_index, game["flag_indexes"]):
            # game win
            game["game_state"] = const.WIN_STATE

        # check player touched mine
        legs_index = Screen.get_legs_index()
        if Soldier.player_touches_mine(legs_index, game["mines_pos"]):
            # game lose
            game["game_state"] = const.LOSE_STATE

        # update variables and screen
        # draw updated screen


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game["run"] = False

        if event.type == pygame.KEYDOWN:
            # means a key was pressed
            # make sure solider isn't out of bounds and then initiate movements
            key_pressed = event.key  # get key type
            player_pos = Screen.get_player_index
            if key_pressed in game["movements_keys"]:
                Soldier.movement(key_pressed, player_pos)

            elif event.key == pygame.K_RETURN:
                game["game_state"] = const.ENTER_STATE
