import pygame

SQUARE_SIZE = 20
NUM_SQUARES_WIDTH = 50
NUM_SQUARES_HEIGHT = 25
WINDOW_WIDTH = SQUARE_SIZE * NUM_SQUARES_WIDTH
WINDOW_HEIGHT = SQUARE_SIZE * NUM_SQUARES_HEIGHT
BACKGROUND_COLOR = (0, 128, 0)
LINE_COLOR = BACKGROUND_COLOR
EMPTY_VALUE = 0
MINE_VALUE = 1
MINES_BACKGROUND_COLOR = (24, 24, 24)
# FLAG_MEASUREMENTS
FlAG_PNG = pygame.image.load("flag.png")
FlAG_PNG = pygame.transform.scale(FlAG_PNG, (SQUARE_SIZE * 4, SQUARE_SIZE * 4))
FLAG_WIDTH = FlAG_PNG.get_width()
FLAG_HEIGHT = FlAG_PNG.get_height()
FLAG_START_POS = (WINDOW_WIDTH - FLAG_WIDTH, WINDOW_HEIGHT - FLAG_HEIGHT)

NIGHT_SOLDIER_PNG = pygame.image.load('soldier_nigth.png')
NIGHT_SOLDIER_PNG = pygame.transform.scale(NIGHT_SOLDIER_PNG, (SQUARE_SIZE * 4, SQUARE_SIZE * 4))

BUSH_PNG = pygame.image.load("grass.png")
BUSH_PNG = pygame.transform.scale(BUSH_PNG, (SQUARE_SIZE * 3, SQUARE_SIZE * 2))
BUSH_WIDTH = BUSH_PNG.get_width()
BUSH_HEIGHT = BUSH_PNG.get_height()

MINE_PNG = pygame.image.load("mine.png")
MINE_PNG = pygame.transform.scale(MINE_PNG, (SQUARE_SIZE * 3, SQUARE_SIZE * 1))
MINE_WIDTH = MINE_PNG.get_width()
MINE_HEIGHT = MINE_PNG.get_height()

SIDE_MESSAGE_1 = "Welcome to The Flag Game."
SIDE_MESSAGE_2 = "Have Fun!"
SIDE_MESSAGE_1_LOCATION = (SQUARE_SIZE * 3, SQUARE_SIZE)
SIDE_MESSAGE_2_LOCATION = (SQUARE_SIZE * 3, SQUARE_SIZE * 2)
SIDE_MESSAGE_COLOR = (255, 255, 255)
SIDE_MESSAGE_FONT_SIZE = 20
FONT_NAME = "Calibri"
FONT_SIZE = 200
WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "You lose!"
MESSAGE_LOCATION = (140, 150)
MESSAGE_COLOR = (255, 255, 255)
RUNNING_STATE = 0
LOSE_STATE = 1
WIN_STATE = 2
ENTER_STATE = 3

SECOND = 1000

DONT_SPAWN_MINES_LIST = [(0, 3)]  # so it won't spawn a mine in the player start location, which will cause instant lose
NUM_OF_MINES = 20
