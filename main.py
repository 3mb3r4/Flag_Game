import pygame
import MineField
import Screen
import Soldier
import const

game = {"run": True,
        "mines_pos": [],
        "player_indexes": [],
        "flag_indexes": [],
        "bushes_list": Screen.random_bushes_list(),
        "movements_keys": [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT],
        "game_state": const.RUNNING_STATE,
        }


def main():
    pygame.init()  # initializes game
    game["flag_indexes"] = MineField.get_flag_index(const.FLAG_START_POS)  # adds flag indexes
    # making mines
    MineField.make_empty_field()
    MineField.create_random_mines(game["flag_indexes"])
    game["mines_pos"] = MineField.mine_indexes_list()

    # create player png, and start pos
    player_png, player_start_pos = Soldier.player_pos_start()
    game["player_indexes"] = Soldier.player_pos_in_matrix_list(player_start_pos)

    while game["run"]:
        handle_user_events(player_png)  # handles inputs

        body_indexes = game["player_indexes"][:3]  # gets only the body indexes (upper half of player)
        # check player touches flag
        if Soldier.player_touches_flag(body_indexes, game["flag_indexes"]):
            # game win, player touched flag
            game["game_state"] = const.WIN_STATE
            game["run"] = False  # to make game stop running

        # check player touched mine
        legs_index = game["player_indexes"][6:]
        if Soldier.player_touches_mine(legs_index, game["mines_pos"]):
            # game lose, player touched mine
            game["game_state"] = const.LOSE_STATE
            game["run"] = False  # to make game stop running

        # updated variables and screen
        # draw updated screen
        Screen.draw_game(game["game_state"], game["player_indexes"][0], player_png, game["bushes_list"])

        if game["game_state"] == const.ENTER_STATE:
            game["game_state"] = const.RUNNING_STATE  # so the game will go back to running game screen


def handle_user_events(player_png):
    for event in pygame.event.get():  # for every event in the game
        if event.type == pygame.QUIT:
            game["run"] = False

        if event.type == pygame.KEYDOWN:
            # means a key was pressed
            key_pressed = event.key  # get key type
            if event.key == pygame.K_RETURN:
                game["game_state"] = const.ENTER_STATE  # means the screen needs to change to show grid and mines
            elif key_pressed in game["movements_keys"]:
                Soldier.movement(key_pressed, game["player_indexes"], player_png)  # means solider needs to move


if __name__ == "__main__":
    main()
