from variables import *

def draw_window(ship,  bullets):
    screen.blit(SPACE,(0,0))
    screen.blit(SPACESHIP,(ship.x,ship.y))
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    pygame.display.update()