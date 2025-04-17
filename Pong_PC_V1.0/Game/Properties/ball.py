import pygame
from Game.Properties.properties import BALL_WIDTH, BALL_HEIGHT, HEIGHT, WIDTH, WHITE

class Ball:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_HEIGHT)
        self.vel_x = vel
        self.vel_y = vel
        self.initial_x = x
        self.initial_y = y

    def ball_move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Ball bouncing logic
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vel_y = -self.vel_y
        
        # Ball resets to the center if it goes off screen
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            # if player score return 1, if ai scores return -1
            if self.rect.left <= 0:
                self.reset()
                return -1
            elif self.rect.right >= WIDTH:
                self.reset()
                return 1
        
        return 0

    def reset(self):
        # reset ball
        self.rect.x = self.initial_x
        self.rect.y = self.initial_y

        # reverse the direction
        self.vel_x = -self.vel_x

    def collision_check(self, player):
        # check for collision with player paddle
        if self.rect.colliderect(player.rect):
            # reverse horizontal direction
            self.vel_x = -self.vel_x

            # change to vertical velocity based on the collision point
            # to spice up the game
            middle_y = player.rect.y + player.rect.height / 2
            difference_in_y = middle_y - (self.rect.y + self.rect.height / 2)
            reduction_factor = (player.rect.height / 2) / 5
            self.vel_y = -difference_in_y / reduction_factor

    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.rect)
