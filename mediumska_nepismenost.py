import pygame

class MediumskaNepismenost:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 500))
        self.bg_color = (255,255,255)
        self.running = True
        pygame.display.set_caption("MIK")
    
    def game_loop(self):   
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            
game = MediumskaNepismenost()
game.game_loop()