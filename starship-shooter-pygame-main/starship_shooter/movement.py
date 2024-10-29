import pygame
from variables import *
# 
def ship_move(keys_pressed,ship):
    if keys_pressed[pygame.K_LEFT] and ship.x >0:
        ship.x -= SPEED
    elif keys_pressed[pygame.K_RIGHT] and ship.x < 750:
        ship.x += SPEED
    elif keys_pressed[pygame.K_UP] and ship.y > 0:
        ship.y -= SPEED
    elif keys_pressed[pygame.K_DOWN] and ship.y < 750:
        ship.y += SPEED