import pygame
import time
import math
import random
import Enemy
import Player

pygame.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
done = False
font_obj = pygame.font.SysFont("Courier New", 16)
clock = pygame.time.Clock()
paused = False
player_bullet_list = []
enemy_bullet_list = []
enemy_list = []
num_enemies_in_wave = 5
wave_number = 0

p = Player.player()
e = Enemy.enemy
while not done:
    # Updates
    delta_time = clock.tick() / 1000
    event = pygame.event.poll()

    p.handle_input(win_width, event, delta_time, paused)
    e.update_enemies(None, enemy_list, enemy_bullet_list, delta_time, win_height)
    p.update_bullets(delta_time, win_height)
    if len(enemy_list) == 0:
        num_enemies_in_wave += 5
        wave_number += 1
        enemy_list = Enemy.enemy.spawn_enemies(None, num_enemies_in_wave, win_width)
        # putting drawing code here is kind of gross, but it is simple...
        temps = font_obj.render("Wave #" + str(wave_number), False, (255,0,0), (0,0,0))
        win.blit(temps, (win_width / 2 - temps.get_width() / 2, win_height / 2 - temps.get_height() / 2))
        pygame.display.flip()
        time.sleep(2)

    # Inputs


    if event.type == pygame.QUIT:
        done = True

    # Draw
    win.fill((0,0,0))
    e.draw_enemies(None, win, enemy_list)
    win.blit(font_obj.render("Enemies Left: " + str(len(enemy_list)), False, (255, 255, 0)), (400, 0))
    p.draw_player(win)


    pygame.display.flip()
pygame.quit()