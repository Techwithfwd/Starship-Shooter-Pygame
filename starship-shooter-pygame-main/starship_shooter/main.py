import pygame
import sys
from variables import *
from draw import *
from movement import *
from fire_gun import *
pygame.init()
sys.setrecursionlimit(10000)
# 
pygame.display.set_caption('SHOOTER GAME')
# 
def main():
    ship = pygame.Rect((WIDTH//2-25),700,50,50)
    bullets  = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(ship.x + ship.height//2-2,ship.y,5,15)
                    bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        ship_move(keys_pressed,ship)
        fire_bullets(bullets)
        draw_window(ship, bullets)
    pygame.display.update()
    main()

if __name__ in '__main__':
    main()

