import pygame
from button import Button

class MediumskaNepismenost:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 500))
        self.bg_color = (0,0,0)
        self.running = True
        pygame.display.set_caption("MIK")
        
        self.button = Button(self)
    
    def game_loop(self):   
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(self.bg_color)
            self.button.draw_button()
            pygame.display.flip()
            
            
            
game = MediumskaNepismenost()
game.game_loop()