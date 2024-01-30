import pygame

class Button:
    def __init__(self, main):
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()  
        self.button_color = (110,123,204)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 30)
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class StartButton(Button):
    def __init__(self, main):
        super().__init__(main)
        self.width, self.height = 100, 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)        
        self.rect.x = 470
        self.rect.y = 220    
        self.msg_image = self.font.render("PLAY", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        

class PostButton(Button):
    def __init__(self, main):
        super().__init__(main)
        self.width, self.height = 100, 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 350
        self.rect.y = 400
        self.msg_image = self.font.render("POST", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        
class FactCheckButton(Button):
    def __init__(self, main):
        super().__init__(main)
        self.width, self.height = 165, 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 590
        self.rect.y = 400
        self.msg_image = self.font.render("FACT-CHECK", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
