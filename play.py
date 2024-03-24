import pygame
from constant import *
from button import Button
import sys
from level import *


def play():
    from main import easy,medium,hard
    while True:

        SCREEN.blit(BG1, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        EASY_BUTTON = Button(image=pygame.image.load("assets\Button levels.png"), pos=(351, 155),
                             text_input="EASY", font=get_font(19), base_color="BLACK", hovering_color="#FEAE49")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets\Button levels.png"), pos=(351, 257),
                               text_input="MEDIUM", font=get_font(19), base_color="BLACK", hovering_color="#FEAE49")
        HARD_BUTTON = Button(image=pygame.image.load("assets\Button levels.png"), pos=(351, 359),
                             text_input="HARD", font=get_font(19), base_color="BLACK", hovering_color="#FEAE49")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    easy()

                if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    print('3succes')
                    medium()

                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    print('4succes')
                    hard()
        pygame.display.update()
