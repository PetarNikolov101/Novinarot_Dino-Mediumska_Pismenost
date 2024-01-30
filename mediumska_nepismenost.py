import pygame
from button import Button
from main_character import MainCharacter
from interactibles import Telefon

class MediumskaNepismenost:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1080, 450))
        self.bg_color = (0,0,0)
        self.running = False
        pygame.display.set_caption("MIK")
        self.background = pygame.image.load('./images/2210_w026_n002_2557b_p1_2557.jpg')
    
        self.dino = MainCharacter(self)
        self.button = Button(self)
        self.telefon = Telefon(self)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.dino.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.dino.moving_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.dino.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.dino.moving_left = False

    def game_loop(self):   
        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.button.rect.collidepoint(mouse_pos):
                        self.running = True
                        
            self.screen.fill(self.bg_color)
            self.button.draw_button()
            pygame.display.flip()
             
        while self.running:
            self.clock.tick(60)
            self._check_events()
            self.dino.update()
            self.screen.blit(self.background, (0, 0))
            self.dino.blitme()
            self.telefon.blitme()
            pygame.display.flip()
game = MediumskaNepismenost()
game.game_loop()