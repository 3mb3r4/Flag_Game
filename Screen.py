import pygame
import const
import MineField


screen = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
background_colour = (0, 128, 0)
screen.fill(background_colour)

def draw_bushes():


def draw_mines_and_lines():
    mine_img = pygame.image.load('mine.png')
    for item in MineField.mine_indexes_list():
        x , y = item
        screen.blit(mine_img, (x * 20, y *20))

def visualize_grid():
    line_color = const.BACKGROUND_COLOR
    pixel_x = 0
    pixel_y = 20
    pixel_x_end = 1000
    while pixel_y != 500:
        pygame.draw.line(screen, line_color, (pixel_x, pixel_y), (pixel_x_end, pixel_y))
        pixel_y += 20
    while pixel_x != 1000:
        pygame.draw.line(screen, line_color, (pixel_x, pixel_y), (pixel_x_end, pixel_y))






def object_draw():




