import pygame
import MineField
import Screen
import Soldier

# handling pygame events

game_state = {"run": True,
              "mines_pos": [],
              "movements_keys": [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT],
              "flag_indexes": Screen.get_flag_indexes}


def main():
    pygame.init()
    MineField.make_empty_field()
    MineField.create_random_mines()

    while game_state["run"]:
        handle_user_events()



        # check player touches flag
        player_index = Screen.get_player_index()
        if Soldier.player_touches_flag(player_index, game_state["flag_indexes"]):
            # game win
            pass

        # check player touched mine
        legs_index = Screen.get_legs_index()
        if Soldier.player_touches_mine(legs_index, MineField.mine_indexes_list()):
            # game lose
            pass


        # update variables and screen
        # draw updated screen


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["run"] = False

        if event.type == pygame.KEYDOWN:
            # means a key was pressed
            # make sure solider isn't out of bounds and then initiate movements
            key_pressed = event.key  # get key type
            player_pos = Screen.get_player_index
            if key_pressed in game_state["movements_keys"]:
                Soldier.movement(key_pressed, player_pos)

            elif event.key == pygame.K_RETURN:
                # pressed enter
                # show the mines for 1 sec
                pass




