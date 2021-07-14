# Galaga Main V 0.0.1
# Kevin & Blake
# 7/14/21 9:43

import pygame

win_width = 600
win_height = 800
pygame.init()
win = pygame.display.set_mode((win_width, win_height))
done = False
clock = pygame.time.Clock()
font_obj = pygame.font.SysFont("Courier New", 16)
paused = False


while not done:
    # @@@@@@@@@@@
    # @ Updates @
    # @@@@@@@@@@@

    # @@@@@@@@@
    # @ Input @
    # @@@@@@@@@
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True

    # @@@@@@@@@@@
    # @ Drawing @
    # @@@@@@@@@@@
    pygame.display.flip()

pygame.quit()
