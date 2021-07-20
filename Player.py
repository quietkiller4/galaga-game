import random
import pygame.draw
import math

class player:
    def __init__(self):
        self.color = (0,0,255)
        self.circle_x = 400
        self.circle_y = 550
        self.circle_radius = 15
        self.speed = 15
        self.time_to_fire = 5
        self.player_img = pygame.image.load("..\\images\\simple_ship.png")
        self.player_bullet_list = []


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
        for bullet in self.player_bullet_list:
            bullet[1] -= bullet[2] * delta_time

    def handle_input(self, win_width, event, delta_time, paused):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.circle_x += .1
            if self.circle_x > 799:
                print("hit right wall")
                self.circle_x = 799
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.circle_x -= .1
            if self.circle_x < 1:
                self.circle_x = 1
        #if keys[pygame.K_UP] or keys[pygame.K_w]:
            #self.circle_y -= .1
            #if self.circle_y < 1:
                #self.circle_y = 1
        #if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #self.circle_y += .1
            #if self.circle_y > 599:
                #self.circle_y = 599

        y = 550
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("I left clicked")
            speed = 150
            time_to_fire = 5
            bullet1 = [self.circle_x, y, speed, time_to_fire]
            self.player_bullet_list.append(bullet1)
            y -= 5

    def draw_bullets(self, win):
        for bullet in self.player_bullet_list:
            pygame.draw.circle(win, (0, 0, 255), (bullet[0], bullet[1]), 5)

    def draw_player(self, win):
        pygame.draw.circle(win, (255,0,0), (self.circle_x, self.circle_y), self.circle_radius)
        win.blit(self.player_img, (self.circle_x - 90, self.circle_y - 115))
        self.draw_bullets(win)