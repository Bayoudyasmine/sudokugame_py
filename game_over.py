import pygame
from constant import *
from button import Button
import sys
from level import *


def Game_over():
    from main import main_menu
    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        Main_menu = Button(image=pygame.image.load("assets\Button levels.png"), pos=(570, 450),
                           text_input="Main menu", font=get_font(22), base_color="BLACK", hovering_color="#FEAE49")

        for button in [Main_menu]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Main_menu.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
