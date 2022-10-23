import pygame

# handling pygame events

game_state = {"run": True,
              "mines_pos": [],
              "movements_keys": [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
              }

pygame.init()


def main():
    while game_state["run"]:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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


