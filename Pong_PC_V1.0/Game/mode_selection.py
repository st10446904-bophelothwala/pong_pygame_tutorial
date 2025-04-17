import pygame
from Game.Properties.button import Button
from Game.Properties.properties import WIDTH,WINDOW, BACKGROUND, BLACK, WHITE, HEIGHT, PLAYER_VEL, BALL_VEL, BALL_WIDTH, BALL_HEIGHT, ICON
from Game.Single_Player_Mode import single_player_game
from Game.Two_Player_Mode import two_player_game
from Fonts.fonts import font_medium, font_large

MENU = 1
GAME = 2
SINGLE = 3
CO_OP = 4
SETTINGS = 5
PAUSED = 6
QUIT = 0

FPS = 60

class Mode_Selection:
    def __init__(self):
        self.title = font_large.render("Select Gameplay", True, WHITE)
        self.title_rect = self.title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        # draw buttons
        button_width = 200
        button_height = 60
        button_x = WIDTH // 2 - button_width // 2

        self.single_player_button = Button(
            button_x, HEIGHT // 2 - 20,
            button_width, button_height,
            "Single Player", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

        self.two_player_button = Button(
            button_x, HEIGHT // 2 + 60,
            button_width, button_height,
            "Two Player", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

        self.back_button = Button(
            10,  10, 
            button_width, button_height,
            "Go Back", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

    def draw(self, surface):
        # display title
        surface.blit(self.title, self.title_rect)

        # display buttonss
        self.single_player_button.draw(surface)
        self.two_player_button.draw(surface)
        self.back_button.draw(surface)

    def handle_input(self, mouse_pos, mouse_clicked):
        # check for interactions
        self.single_player_button.check_hover(mouse_pos)
        self.two_player_button.check_hover(mouse_pos)
        self.back_button.check_hover(mouse_pos)

        if self.single_player_button.check_clicked(mouse_pos, mouse_clicked):
            return SINGLE
        elif self.two_player_button.check_clicked(mouse_pos, mouse_clicked):
            return CO_OP
        elif self.back_button.check_clicked(mouse_pos, mouse_clicked):
            return QUIT
        else:
            return None

def mode_select():

    on_mode_select = True
    select_menu = Mode_Selection()
    mouse_clicked = False
    mouse_pos = pygame.mouse.get_pos()
    clock = pygame.time.Clock()

    while on_mode_select:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True

        WINDOW.blit(BACKGROUND, (0, 0))

        select_menu.draw(WINDOW)
        
        new_state = select_menu.handle_input(mouse_pos, mouse_clicked)

        if new_state is not None:
            # handle game states
            if new_state == SINGLE:
                single_player_game()
                return MENU
            elif new_state == CO_OP:
                two_player_game()
                return  MENU
            elif new_state == MENU:
                return MENU
            elif new_state == QUIT:
                return QUIT
        

    pygame.display.update()

    return MENU