import random
import pygame.draw
import math

class enemy:
    def __init__(self):
        self.enemy_bullet_list = []

    def distance(x1, y1, x2, y2):
        """
        Gets the distance between two points
        :param x1: the x-position of the first point
        :param y1: the y-position of the first point
        :param x2: the x-position of the second point
        :param y2: the y-position of the second point
        :return: the distance between the two points (a float)
        """
        # a, b, and c are all temporary local variables. they like parameters, go away when the function is done

        a = x1 - x2
        b = y1 - y2
        c = (a ** 2 + b ** 2) ** .5
        # this return statement sends back the value held by c to the caller. A side-effect of a return statements
        return c

    def update_bullets(self, delta_time, win_height):
        for bullet in self.enemy_bullet_list:
            bullet[1] -= bullet[2] * delta_time

    def update_enemies(self, enemy_list, bullet_list, delta_time, win_height):
        # health_change, score_change
        health_change = 0
        for enemy_1 in enemy_list:
            x = math.sin(enemy_1[1] * .5) * 30 + enemy_1[0]
            enemy_1[1] += 20 * delta_time
            enemy_1[3] -= delta_time
            if enemy_1[3] <= 0:
                speed = 150
                time_to_fire = 5
                bullet1 = [x, enemy_1[1] + 25, -speed, enemy_1[3]]
                bullet_list.append(bullet1)
                enemy_1[3] = 5
            if enemy_1[1] > 800 + 15:
                health_change += 5
                enemy_list.remove(enemy_1)

    def spawn_enemies(self, num_enemies_in_wave, win_width):
        #enemy_list
        enemies = []
        y1 =- 15
        win_width -= 20
        for i in range(num_enemies_in_wave):
            x1 = random.randint(20, win_width)
            speed = 50
            time_to_fire = 5
            enemy1 = [x1, y1, speed, time_to_fire]
            enemies.append(enemy1)
            y1 -= 75
        return enemies

    def draw_bullets(self, win):
        for bullet in self.enemy_bullet_list:
            pygame.draw.circle(win, (0, 0, 255), (bullet[0], bullet[1]), 5)

    def draw_enemies(self, win, enemy_list):
        for enemy_1 in enemy_list:
            x = math.sin(enemy_1[1] * .5) * 30 + enemy_1[0]
            pygame.draw.circle(win, (255, 255, 255), (x, enemy_1[1]), 15)