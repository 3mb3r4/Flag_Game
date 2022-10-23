import pygame

WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_colour = (0, 128, 0)
screen.fill(background_colour)


def pygame_screen():
    pygame.display.flip()
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
    pygame.quit()