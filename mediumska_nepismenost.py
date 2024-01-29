import pygame
from button import Button

class MediumskaNepismenost:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 450))
        self.bg_color = (0,0,0)
        self.running = False
        pygame.display.set_caption("MIK")
        self.background = pygame.image.load('./images/2210_w026_n002_2557b_p1_2557.jpg')
        
        self.button = Button(self)
    
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
game = MediumskaNepismenost()
game.game_loop()