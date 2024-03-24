import pygame

pygame.init()

BG = pygame.image.load("assets\Welcome.png")
BG1 = pygame.image.load("assets\Levels D.png")
BG3 = pygame.image.load("assets\easy level.png")
BG4 = pygame.image.load("assets\Excellent.png")
BG5 = pygame.image.load("assets\GameOver.png")
score = 0
s = 0
black = (0, 0, 0)
srn = 3
background_color = (255, 255, 255)
original_grid_element_color = (52, 31, 151)
buffer = 5
base = 3
side = base*base
myfont = pygame.font.SysFont('Comic Sans MS', 25)
SCREEN = pygame.display.set_mode((703, 500))
issalah = False


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets\Inter-ExtraBold.ttf", size)
