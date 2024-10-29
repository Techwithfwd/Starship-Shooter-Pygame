from variables import *
# 
def fire_bullets(bullets):
    for bullet in bullets:
        bullet.y -= BULLET_SPEED