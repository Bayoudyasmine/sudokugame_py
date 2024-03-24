import pygame
import time



DEBUG = True

class TEMPS:
    
    def __init__(self):

        self.startTime = time.time()
        self.timer = 0
        self.mins = 0
        self.sec = 0
        self.w, self.h = pygame.display.get_surface().get_size()


    
    def updateTimer(self):
        self.timer = time.time() - self.startTime
        self.mins = int(self.timer / 60)
        self.sec = int(self.timer % 60)
        if self.sec >= 60:
            self.mins += 1


    def render(self, screen):

        pygame.draw.rect(screen,'#FEAE49', (
                                        550, 50, 200, 200))
        
        clockString = f"{self.mins:02}:{self.sec:02}"
        myfont = pygame.font.SysFont('Comic Sans MS', 34)
        value = myfont.render(clockString, True, '#3D424A')
        screen.blit(value, (550, 50))
        
        if DEBUG:
            pass

        pygame.display.flip()
    
    def ShowTime(self,screen):
        pygame.draw.rect(screen,'#F0F3F9', (
                                        600, 200, 200, 200))
        clockString = f"{self.mins:02}:{self.sec:02}"
        myfont = pygame.font.SysFont('Comic Sans MS', 34)
        value = myfont.render(clockString, True, '#3D424A')
        screen.blit(value, (600, 250))




    """game = Game()
    running = True

    while running:
        game.updateTimer()
        game.render(screen)"""
     


