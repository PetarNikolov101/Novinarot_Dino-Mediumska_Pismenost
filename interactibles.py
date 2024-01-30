import pygame

class Telefon:
    def __init__(self, main):
        pygame.init()
        self.telefon = pygame.image.load("images/telefon.png")
        self.rect = self.telefon.get_rect()
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.rect.x = 250
        self.rect.y = 360
        
    
    def blitme(self):
        self.screen.blit(self.telefon, self.rect)