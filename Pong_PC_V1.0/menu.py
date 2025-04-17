import pygame
import sys
from Game.Properties.properties import WIDTH,WINDOW, BACKGROUND, BLACK, WHITE, HEIGHT, PLAYER_VEL, BALL_VEL, BALL_WIDTH, BALL_HEIGHT, ICON
from Game.Properties.players import Players
from Game.Properties.ball import Ball
from Game.Properties.button import Button
from Fonts.fonts import  font_medium, font_large
from Sounds.sounds import load_game_sounds, sound_manager
from Game.Single_Player_Mode.single_player_game import single_player_game
from Game.mode_selection import Mode_Selection, mode_select

pygame.init()

# Game States
MENU = 1
GAME = 2
SINGLE = 3
CO_OP = 4
SETTINGS = 5
PAUSED = 6
QUIT = 0

FPS = 60

class Menu:
    def __init__(self):
        self.title = font_large.render("PONG", True, WHITE)
        self.title_rect = self.title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        # draw buttons
        button_width = 200
        button_height = 60
        button_x = WIDTH // 2 - button_width // 2

        self.play_button = Button(
            button_x, HEIGHT // 2 - 20,
            button_width, button_height,
            "Play Game", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

        self.settings_button = Button(
            button_x, HEIGHT // 2 + 60,
            button_width, button_height,
            "Settings", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

        self.quit_button = Button(
            button_x, HEIGHT // 2 + 140,
            button_width, button_height,
            "Quit", font_medium, WHITE, 
            (50, 50, 50), (100, 100, 100)
        )

    def draw(self, surface):
        # display title
        surface.blit(self.title, self.title_rect)

        # display buttonss
        self.play_button.draw(surface)
        self.settings_button.draw(surface)
        self.quit_button.draw(surface)

    def handle_input(self, mouse_pos, mouse_clicked):
        # check for interactions
        self.play_button.check_hover(mouse_pos)
        self.settings_button.check_hover(mouse_pos)
        self.quit_button.check_hover(mouse_pos)

        if self.play_button.check_clicked(mouse_pos, mouse_clicked):
            return GAME
        elif self.settings_button.check_clicked(mouse_pos, mouse_clicked):
            return SETTINGS
        elif self.quit_button.check_clicked(mouse_pos, mouse_clicked):
            return QUIT
        else:
            return None
    

def main():
    menu = Menu()
    clock = pygame.time.Clock()
    game_state = MENU

    run = True
    
    # load sounds before the loop
    load_game_sounds()

    #set_sound_volumes
    sound_manager.set_volume("button_hover", 0.7)
    sound_manager.set_volume("button_click", 0.7)
    
    while run:
        # Movement frame or delay player movement
        clock.tick(FPS) # or
        # pygame.time.delay()
        #
            
        # handle mouse position and clicks
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        # stop and exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
        #   
        
        
       
        WINDOW.fill(BLACK)

        WINDOW.blit(BACKGROUND, (0, 0))

        # handle game states
        if game_state == MENU:
            menu.draw(WINDOW)
            new_state = menu.handle_input(mouse_pos, mouse_clicked)

            if new_state is not None:
                game_state = new_state
        elif game_state == GAME:
            mode_select()
            #single_player_game()
            game_state == MENU
        elif game_state == SETTINGS:
            game_state == MENU
        elif game_state == QUIT:
            run = False
        

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()




