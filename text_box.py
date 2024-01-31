import pygame

class TextBox:
    def __init__(self, main, text):
        self.screen = main.screen
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 20)
        self.text_box = pygame.Surface([640,480], pygame.SRCALPHA, 32)
        self.text_box = self.text_box.convert_alpha()
        self.rect = pygame.draw.rect(self.text_box, (110, 123, 204, 150), (165, 50, 460, 260))
        self.text = text
        
        self.msg_image = self.font.render(self.text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def blitme(self):
        self.screen.blit(self.text_box, self.rect )
        self.screen.blit(self.msg_image, self.msg_image_rect)