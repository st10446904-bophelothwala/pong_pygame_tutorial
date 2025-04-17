import pygame
import sys
import time
from Game import *
from Game.Properties.properties import WINDOW, BACKGROUND, PLAYER_WIDTH, ICON
from Game.Properties.players import Players
from Game.Properties.ball import Ball
from Fonts.fonts import font


playerOne = Players(0, HEIGHT // 2 - 75, PLAYER_VEL)
ai = Players(WIDTH - 30, HEIGHT // 2 - 75, PLAYER_VEL)
ball = Ball(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_VEL)

player_score = 0
ai_score = 0
points_x = 50
points_y = 50
FPS = 60
#def draw(WINDOW, playerOne):
    #WINDOW.fill((0, 0, 0)) # keeps screen clean to redraw character
    #WINDOW.blit(BACKGROUND, (0, 0))
    # draw player object
    #pygame.draw.rect(WINDOW, WHITE, playerOne)
    #pygame.display.update()

def ai_movement():
    # AI Movement
        if ball.rect.y < ai.rect.y + ai.rect.height // 2:
            if ai.rect.y > 0:
                ai.rect.y -= PLAYER_VEL // 2
        elif ball.rect.y > ai.rect.y + ai.rect.height // 2:
            if ai.rect.y < HEIGHT - ai.rect.height:
                ai.rect.y += PLAYER_VEL // 2

def draw_player_points(surface, player_text, x, y, color):
    text_surface = font.render(str(player_text), True, color)
    text_rect = text_surface.get_rect(topleft=(x, y))

    # Blit the text onto the surface
    surface.blit(text_surface, text_rect)

def draw_ai_points(surface, ai_text,x, y, color):
    text_surface = font.render(str(ai_text), True, color)
    text_rect = text_surface.get_rect(topleft=(x, y))

    # Blit the text onto the surface
    surface.blit(text_surface, text_rect)


def single_player_game():
    global player_score
    global ai_score
    keys = pygame.key.get_pressed()
    playerOne.p1_move(keys, HEIGHT)

    ai_movement()

    score_result = ball.ball_move()
    if score_result == 1:
        player_score += 1
        time.sleep(3)
    elif score_result == -1:
        ai_score += 1
        time.sleep(3)
        
    # check for collisions
    ball.collision_check(playerOne)
    ball.collision_check(ai)

    WINDOW.fill(BLACK)

    WINDOW.blit(BACKGROUND, (0, 0))

    pygame.draw.rect(WINDOW, WHITE, playerOne.rect)
    pygame.draw.rect(WINDOW, WHITE, ai.rect)
    pygame.draw.rect(WINDOW, WHITE, ball.rect)



    #draw(WINDOW, playerOne)

    #points = str(int(points_str) + 1)

    draw_player_points(WINDOW, player_score, 350, 50, WHITE)

    draw_ai_points(WINDOW, ai_score, 640, 50, WHITE)

    pygame.display.update()

    return
        

