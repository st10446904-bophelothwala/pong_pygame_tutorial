import pygame
from Game.Properties.properties import HEIGHT, PLAYER_VEL,  PLAYER_WIDTH, PLAYER_HEIGHT, WHITE

class Players:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vel = vel

    def p1_move(self, keys, screen_height):
        # Player Movement and movement boundaries 
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= PLAYER_VEL

        if keys[pygame.K_DOWN] and self.rect.y < screen_height - PLAYER_HEIGHT:
            self.rect.y += PLAYER_VEL
        
        #if keys[pygame.K_LEFT] and self.rect.x > 0:
            #self.rect.x -= PLAYER_VEL

        #if keys[pygame.K_RIGHT] and self.rect.x < screen_width - PLAYER_WIDTH:
            #self.rect.x += PLAYER_VEL 
        
    
        # jumping
        #if keys[pygame.K_SPACE]
        # x -= vel (left), x += vel (right)
        
        # y -= vel (up), y += vel (down)

    def p2_move(self, keys, screen_height):
        # Player Movement and movement boundaries 
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= PLAYER_VEL

        if keys[pygame.K_s] and self.rect.y < screen_height - PLAYER_HEIGHT:
            self.rect.y += PLAYER_VEL
        
        #if keys[pygame.K_LEFT] and self.rect.x > 0:
            #self.rect.x -= PLAYER_VEL

        #if keys[pygame.K_RIGHT] and self.rect.x < screen_width - PLAYER_WIDTH:
            #self.rect.x += PLAYER_VEL 
        
    
        # jumping
        #if keys[pygame.K_SPACE]
        # x -= vel (left), x += vel (right)
        
        # y -= vel (up), y += vel (down)


    #def draw(self, window):
        # draws player
        #pygame.draw.rect(window, WHITE, self.rect)   
