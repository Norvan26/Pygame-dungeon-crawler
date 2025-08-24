import pygame

class Gui:
    def __init__(self, display, health = 100, mana = 100, stamina = 100):
        self.display = display
        self.health = health
        self.mana = mana
        self.stamina = stamina
        self.fullHealth = health
        self.fullMana = mana
        self.fullStamina = stamina
        self.image = pygame.image.load('assets/uiBar.png')
        self.w, self.h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (self.w*1.6, self.h*1.6))
        self.x = 10
        self.y = 10
        self.stamina = 20 
        self.mana = 50
        self.health = 75

    def run(self):
        self.display.blit(self.image, (self.x, self.y))
        pygame.draw.rect(self.display, (255,0,0), pygame.Rect(128, 20, (self.health/self.fullHealth)*165, 18))
        pygame.draw.rect(self.display, (0,255,0), pygame.Rect(128, 53, (self.mana/self.fullMana)*165, 18))
        pygame.draw.rect(self.display, (0,0,255), pygame.Rect(127, 84, (self.stamina/self.fullStamina)*165, 18))