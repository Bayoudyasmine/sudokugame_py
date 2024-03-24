import pygame
from constant import *
from button import Button
from level import *


def destribution(grid, myfont, original_grid_element_color, a, b):
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):
                value = myfont.render(
                    str(grid[i][j]), True, original_grid_element_color)
                SCREEN.blit(value, ((j+1)*40+a, (i+1)*40+b))
    pygame.display.update()