import pygame
import sys
from button import Button
from constant import *
from level import Generer
from play import play

pygame.init()
SCREEN = pygame.display.set_mode((703, 500))
pygame.display.set_caption("Menu")


def easy():
    while True:
        Generer(12)

def medium():
    while True:
        Generer(20)


def hard():
    while True:
        Generer(30)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BUTTON = Button(image=pygame.image.load("assets\Button.png"), pos=(355, 400),
                             text_input="PLAY", font=get_font(19), base_color="black", hovering_color="#FEAE49")  
        QUIT_BUTTON = Button(image=pygame.image.load("assets\Button.png"), pos=(355, 450),
                             text_input="QUIT", font=get_font(19), base_color="black", hovering_color="#FEAE49")
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()
