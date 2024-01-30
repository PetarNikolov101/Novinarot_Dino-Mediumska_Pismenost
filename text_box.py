import pygame

class TextBox:
    def __init__(self, main):
        self.screen = main.screen
        self.text_box = pygame.Surface([640,480], pygame.SRCALPHA, 32)
        self.text_box = self.text_box.convert_alpha()
        self.rect = pygame.draw.rect(self.text_box, (110, 123, 204, 150), (165, 50, 460, 260))

    def blitme(self):
        self.screen.blit(self.text_box, self.rect )