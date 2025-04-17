import pygame
from Game.Properties.properties import WHITE
from Sounds.sounds import sound_manager


class Button:
    def __init__(self, x, y, width, height, text, font, text_color, background_color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.background_color = background_color
        self.hover_color = hover_color
        self.is_hovered = False
        self.clicked = False


    def draw(self, surface):
        # button background
        color = self.hover_color if self.is_hovered else self.background_color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, WHITE, self.rect, 2)

        # text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        was_hovered_before = self.is_hovered
        self.is_hovered = self.rect.collidepoint(mouse_pos)

        # play sound if cursor hovers to a button
        if self.is_hovered and not was_hovered_before:
            sound_manager.play("button_hover")
        
        return self.is_hovered

    def check_clicked(self, mouse_pos, mouse_clicked):
        if self.rect.collidepoint(mouse_pos) and mouse_clicked:
            self.clicked = True

            # play click sound
            sound_manager.play("button_click")
            return True
        return False

    
