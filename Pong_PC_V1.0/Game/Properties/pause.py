import pygame
from Game.Properties.properties import WIDTH, HEIGHT, WHITE
from Fonts.fonts import  font_large, font_medium
from Game.Properties.button import Button
from menu import GAME, PAUSED, MENU

class Pause:
    def __init__(self):
        # create semi-transparent overlay
        self.overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 128))

        self.title = font_large.render("PAUSED!", True, WHITE)
        self.title_rect = self.title.get_rect(center=(WIDTH // 2, HEIGHT // 3))

        # pause buttons
        button_width = 200
        button_height = 60
        button_x = WIDTH // 2 - button_width // 2

        self.resume_button = Button(
            button_x, HEIGHT // 2 - 30,
            button_width, button_height,
            "Resume Game", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

        self.main_menu_button = Button(
            button_x, HEIGHT // 2 + 50,
            button_width, button_height,
            "Main Menu", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

    def draw(self, surface):
        # semi-transparent overlay
        surface.blit(self.overlay, (0, 0))
        
        # draw title
        surface.blit(self.title, self.title_rect)

        # draw buttons
        self.resume_button(surface)
        self.main_menu_button(surface)

    def handle_input(self, mouse_pos, mouse_clicked):
        # check for button interactions
        self.resume_button.check_hover(mouse_pos)
        self.main_menu_button.check_hover(mouse_pos)

        if self.resume_button.check_clicked(mouse_pos, mouse_clicked):
            return 2
        elif self.main_menu_button.check_clicked(mouse_pos, mouse_clicked):
            return 1
        else:
            return None
