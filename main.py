import pygame 
import sys
import random
import math
from level import *
from components.button import Button
from components.playerGui import Gui

#
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 736
FPS = 60


# Initialize Pygame
pygame.init()


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('start')
        self.level = Level(self.screen)

        self.start = Start(self.screen)

        self.states = {'start': self.start, 'level': self.level}


    def run(self):
        while True:
            for event in pygame.event.get():
                #if the event type is clicking the x button then the game quits
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pos = pygame.mouse.get_pos()

                self.states[self.gameStateManager.getState()].run()

            pygame.display.update()
            self.clock.tick(FPS)


class Start:
    def __init__(self, display):
        self.display = display
        self.gui = Gui(self.display)


    def run(self):
        self.display.fill('white')
        pygame.draw.rect(self.display, (255,0,0), pygame.Rect(30, 30, 60, 60))
        self.btn = Button(500, 100, 540, 300, pygame.image.load('assets/button.png'), self.display)
        self.gui.run()
        if self.btn.run() and pygame.mouse.get_pressed()[0]:
            print('clicked')


class GameStateManager:
    def __init__(self, initialState):
        self.currentState = ''
        self.currentState = initialState
        print('Hello')

    def setState(self, setterState):
        self.currentState = setterState
    

    def getState(self):
        return(self.currentState)
    

if __name__ == '__main__':
    game = Game()
    game.run()

