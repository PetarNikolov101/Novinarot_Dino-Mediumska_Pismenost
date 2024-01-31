import pygame
from button import StartButton
from button import PostButton
from button import FactCheckButton
from main_character import MainCharacter
from interactibles import Telefon
from interactibles import Rat
from text_box import TextBox
import json

class MediumskaNepismenost:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1080, 450))
        self.bg_color = (0,0,0)
        self.running = False
        self.running_start = True
        pygame.display.set_caption("Новинарот Дино")
        self.background = pygame.image.load('./images/2210_w026_n002_2557b_p1_2557.jpg')
        self.close = False
    
        self.dino = MainCharacter(self)
        self.start_button = StartButton(self)
        self.post_button = PostButton(self)
        self.fact_check_button = FactCheckButton(self)
        self.telefon = Telefon(self)
        self.rat = Rat(self)
        
    
    def check_collisions(self):
        with open('text.json', 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
        if self.dino.rect.colliderect(self.rat.rect) or self.dino.rect.colliderect(self.telefon.rect):
            self.post_button.draw_button()
            self.fact_check_button.draw_button()
            if self.dino.rect.colliderect(self.rat.rect):
                self.textbox = TextBox(self, data.get('rat_start'))
            else:
                self.textbox = TextBox(self, "phone")
            self.textbox.blitme()
                        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.dino.moving_right = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.dino.moving_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.dino.moving_right = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.dino.moving_left = False

    def game_loop(self):   
        while not self.running and self.running_start is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button.rect.collidepoint(mouse_pos):
                        self.running = True
                        
            self.screen.fill(self.bg_color)
            self.start_button.draw_button()
            pygame.display.flip()
             
        while self.running:
            self.clock.tick(60)
            self._check_events()
            self.dino.update()
            self.screen.blit(self.background, (0, 0))
            self.rat.blitme()
            self.telefon.blitme()
            self.dino.blitme()
            self.check_collisions()
            pygame.display.flip()
            
game = MediumskaNepismenost()
game.game_loop()