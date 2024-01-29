import pygame

class MainCharacter:
    def __init__(self, main):
        pygame.init()
        self.dino = pygame.image.load("./images/dino.png")
        self.dino_run_right = pygame.image.load("./images/run_right.png")
        self.dino_run_left = pygame.image.load("./images/run_left.png")
        self.rect = self.dino.get_rect()
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 6
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 6
              
    def blitme(self):
        if not self.moving_left and not self.moving_right or (self.moving_right and self.moving_left):
            self.screen.blit(self.dino, self.rect)
        if self.moving_right and not self.moving_left:
            self.screen.blit(self.dino_run_right, self.rect)     
        if self.moving_left and not self.moving_right:
            self.screen.blit(self.dino_run_left, self.rect)
    

            