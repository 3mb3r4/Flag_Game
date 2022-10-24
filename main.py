import pygame
import MineField
import Screen
import Soldier
import const

# handling pygame events

game = {"run": True,
        "mines_pos": [],
        "player_indexes": [],
        "flag_indexes": [],
        "bushes_list": Screen.random_bushes_list(),
        "movements_keys": [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT],
        "game_state": const.RUNNING_STATE}


def main():
    pygame.init()
    MineField.make_empty_field()
    MineField.create_random_mines()
    game["mines_pos"] = MineField.mine_indexes_list()
    player_png, player_start_pos = Soldier.player_pos_start()

    while game["run"]:
        handle_user_events(player_png)
        game["player_indexes"] = Soldier.player_pos_in_matrix_list(player_start_pos)

        body_indexes = game["player_indexes"][:6]
        # check player touches flag
        if Soldier.player_touches_flag(body_indexes, game["flag_indexes"]):
            # game win
            game["game_state"] = const.WIN_STATE
            game["run"] = False

        # check player touched mine
        legs_index = game["player_indexes"][6:]
        if Soldier.player_touches_mine(legs_index, game["mines_pos"]):
            # game lose
            game["game_state"] = const.LOSE_STATE
            game["run"] = False

        # update variables and screen
        # draw updated screen
        Screen.draw_game(game["game_state"], game["player_indexes"][0], player_png, game["bushes_list"])
        if game["game_state"] == const.ENTER_STATE:
            game["game_state"] = const.RUNNING_STATE


def handle_user_events(player_png):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game["run"] = False

        if event.type == pygame.KEYDOWN:
            # means a key was pressed
            # make sure solider isn't out of bounds and then initiate movements
            key_pressed = event.key  # get key type
            player_pos = game["player_indexes"]
            if key_pressed in game["movements_keys"]:
                Soldier.movement(key_pressed, player_pos, player_png)

            elif event.key == pygame.K_RETURN:
                game["game_state"] = const.ENTER_STATE


if __name__ == "__main__":
    main()
