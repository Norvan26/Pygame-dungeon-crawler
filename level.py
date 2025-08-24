import pygame 
import sys
import os
import random
import math


clock = pygame.time.Clock()

class Level:
    def __init__(self, display):
        self.display = display

    def run(self):
        clock.tick(60)
        
        self.pos = pygame.mouse.get_pos()
        #-------------------------------------------------------------------------------------------------------------------
        keys = pygame.key.get_pressed()


        #pygame.mixer.Sound.play(self.music)
        #pygame.mixer.music.stop()
        
        self.display.fill((100,22,22,255))