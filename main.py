import pygame
import MineField

# handling pygame events

game_state = {"run": True,
              "mines_pos": [],
              "movements_keys": [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
              }


def main():
    pygame.init()
    MineField.make_empty_field()
    MineField.create_random_mines()

    while game_state["run"]:
        handle_user_events()

        # check player touches flag
        player_index = Screen.get_player_index()


        # check player touched mine
        legs_index = Screen.get_legs_index()


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
            # move according to the key pressed
            if key_pressed in game_state["movements_keys"]:
                # move according to the key pressed
                pass

            elif event.key == pygame.K_RETURN:
                # pressed enter
                # show the mines for 1 sec
                pass




