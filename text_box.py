import pygame
import textwrap

class Text:
    def __init__(self, main, text):
        self.screen = main.screen
        self.text = text
        self.font = pygame.font.Font(None, 25)
        self.text_color = (0, 0, 0)

        self.rendered_lines = self.prerender_text()

    def prerender_text(self):
        text_wrapped = textwrap.wrap(self.text, width=50)

        rendered_lines = []
        for line in text_wrapped:
            line_image = self.font.render(line, True, self.text_color)
            rendered_lines.append(line_image)

        return rendered_lines

    def blitme(self):
        y_position = 200
        for line_image in self.rendered_lines:
            self.screen.blit(line_image, (335, y_position))
            y_position += line_image.get_height() 

class Box:
    def __init__(self, main):
        self.screen = main.screen
        self.text_box = pygame.Surface([640,480], pygame.SRCALPHA, 32)
        self.text_box = self.text_box.convert_alpha()
        self.rect = pygame.draw.rect(self.text_box, (110, 123, 204, 150), (165, 50, 460, 260))
    def blitme(self):
        self.screen.blit(self.text_box, self.rect)