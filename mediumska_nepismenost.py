import pygame
import json
import random
from button import StartButton
from button import PostButton
from button import FactCheckButton
from main_character import MainCharacter
from interactables import Telefon
from interactables import Rat
from text_box import Text
from text_box import Box

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
        self.box = Box(self)
        
        self.fact_flag = False
        self.start_flag = True
        self.good_points = 0
        self.bad_points = 0
    
    def check_collisions(self):
        with open('text.json', 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
        if self.dino.rect.colliderect(self.rat.rect) or self.dino.rect.colliderect(self.telefon.rect):
            self.post_button.draw_button()
            self.fact_check_button.draw_button()
            self.box.blitme()
            if self.start_flag:
                if self.dino.rect.colliderect(self.rat.rect):
                    self.text = Text(self, data.get('rat_start'))
                else:
                    self.text = Text(self, data.get("phone_start"))
            if self.fact_flag:    
                if self.dino.rect.colliderect(self.rat.rect):
                    self.text = Text(self,data.get('rat_factcheck'))
                elif self.dino.rect.colliderect(self.telefon.rect):
                    self.text = Text(self,data.get("phone_factcheck"))
            self.text.blitme()
          
    def change_flag(self):
        if self.dino.moving_left or self.dino.moving_right:
            self.start_flag = True 
            self.fact_flag = False
        
    def add_points(self):
        if self.dino.rect.colliderect(self.rat.rect):
            self.bad_points += random.randint(50, 1000)
        elif self.dino.rect.colliderect(self.telefon.rect):
            self.good_points += random.randint(50,1000)
    
    def display_points(self):
        self.font = pygame.font.Font(None, 25)
        self.text_color = (255, 255, 255)
        self.good_score = self.font.render(f"Известени читатели: {self.good_points}", True, self.text_color)
        self.good_score_rect = self.good_score.get_rect()
        self.good_score_rect.x = 45
        self.good_score_rect.y = 50
        
        self.font = pygame.font.Font(None, 25)
        self.text_color = (255, 255, 255)
        self.bad_score = self.font.render(f"Излажани читатели: {self.bad_points}", True, self.text_color)
        self.bad_score_rect = self.bad_score.get_rect()
        self.bad_score_rect.x = 45
        self.bad_score_rect.y = 72
        
        self.screen.blit(self.good_score, self.good_score_rect)
        self.screen.blit(self.bad_score, self.bad_score_rect)
                               
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.post_button.rect.collidepoint(mouse_pos):
                    self.add_points()
                elif self.fact_check_button.rect.collidepoint(mouse_pos):
                    self.fact_flag = True

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
            self.change_flag()
            self.dino.update()
            self.screen.blit(self.background, (0, 0))
            self.display_points()   
            self.rat.blitme()
            self.telefon.blitme()
            self.dino.blitme()
            self.check_collisions()
            self._check_events()
            pygame.display.flip()
            
game = MediumskaNepismenost()
game.game_loop()