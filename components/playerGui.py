import pygame

class Gui:
    def __init__(self, display, health = 100, mana = 100):
        self.display = display
        self.health = health
        self.mana = mana
        self.image = pygame.image.load('assets/uiBar.png')
        self.image = pygame.transform.scale(self.image, (350, 100))
        self.x = 10
        self.y = 10

    def run(self):
        self.display.blit(self.image, (self.x, self.y))