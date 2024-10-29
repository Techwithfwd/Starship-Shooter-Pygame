import pygame
import os
# 
WIDTH = 800
HEIGHT = 800
FPS = 60
RED =(255,0,0)
SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('images','spaceship.png')),(50,50))
SPACESHIP = pygame.transform.rotate(SPACESHIP_IMAGE, 180)
SPACE = pygame.image.load(os.path.join('images','space.png'))
SPEED = 10
BULLET_SPEED = 10
# 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
