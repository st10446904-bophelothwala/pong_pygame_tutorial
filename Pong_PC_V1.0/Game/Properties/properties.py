import pygame
import os

try:
    WIDTH, HEIGHT = 1000, 800
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG!")
    print("\nGame started!")
except pygame.error as e:
    print("\nGame failed to start!")

try:
    ICON = pygame.image.load("Images/Logo/Pong_logo.png")
    pygame.display.set_icon(ICON)
    print("\nIcon loaded: True")
except pygame.error as e:
    print("\nIcon loaded: False")

# colors of the player
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

try:
    BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("Images", "Background","pong_background.png")), (WIDTH, HEIGHT)
    )
    print("\nBackground loaded: True")
except pygame.error as e:
    print("\nBackground loaded: False")
    print("\nEither due to a bug or components missing")

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 150
PLAYER_VEL = 5

BALL_WIDTH = 50
BALL_HEIGHT = 50
BALL_VEL = 6
