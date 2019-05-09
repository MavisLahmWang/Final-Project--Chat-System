#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:39:29 2019

@author: lahmwang
"""

import pygame
from pygame.locals import *
import os
import time
import random

screen_width = 400
screen_height = 500
spacecraft_width = 57
spacecraft_height = 56
enemy_height = 45
enemy_width = 47
bullet_width = 4
bullet_height = 20
paused = True

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (220, 220, 0)
violet = (138, 43, 226)
darkersteelblue = (30, 144, 255)
bright_red = (210, 0, 0)
bright_green = (0, 210, 0)
bright_blue = (0, 0, 210)
bright_yellow = (255, 255, 0)
purple = (160, 32, 240)
steelblue = (99, 184, 255)
skyblue = (135, 206, 250)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Air Battle")
photo = pygame.image.load("spacecraft.png")
clock = pygame.time.Clock()
x = 170
y = 400

# spacecraft's image
def spacecraft(x, y):
    screen.blit(photo, (x, y))
    
# the class of enemies
class Enemy:
    # initialize every enemy
    def restart(self):
        self.x = random.randrange(0, 360)
        self.y = - 5
        self.speed = random.uniform(0.7, 1.5)
        self.active = True
    def __init__(self):
        self.restart()
        self.active = False
        self.image = pygame.image.load("enemy.png").convert_alpha()
    def move(self):
        if self.y <= 510:
            self.y += self.speed
        else:
            self.active = False

# create a list to make several enemies appear simutaneously
enemy = []

# the class of bullets
class Bullet:
    def __init__(self):
        self.x = 0
        self.y = - 100
        self.speed = 7
        self.image = pygame.image.load("bullettt.png").convert_alpha()
        self.active = False
    def shoot(self):
        if self.y < 15:
            self.active = False
        else:
            self.y -= self.speed
    def restart(self):
        self.active = True
        self.x = x + spacecraft_width / 2
        self.y = y

# create a list to store the bullets to shoot
bullet = []
        
# the main menu of the game
def intro_menu():
    intro = True
    while intro:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
        # background
        screen.fill(black)
        message_display("Air Battle", 200, 120, 90, white)
        # button set
        button_fun("Start !", 80, 200, 240, 50, green, bright_green, 35, blue, "start")
        button_fun("Help", 80, 260, 240, 50, bright_yellow, yellow, 35, black, "help")
        button_fun("Credits", 80, 320, 240, 50, purple, violet, 35, black, "credit")
        button_fun("Quit", 80, 380, 240, 50, red, bright_red, 35, bright_blue, "quit")
        
        pygame.display.update()
        clock.tick(10)
        
# the pause menu of the game
def pause():
    while paused:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)

        screen.fill(black)
        message_display("Paused", 200, 170, 90, red)
        # button set
        button_fun("Continue Playing", 80, 250, 240, 50, bright_green, green, 35, blue, "continue")
        button_fun("Back to Main Menu", 80, 330, 240, 50, bright_red, red, 35, blue, "menu")
        
        pygame.display.update()
        clock.tick(10)
        
# unpause the game
def unpause():
    global paused
    paused = False

# a countdown function
def countdown():
    while True:
        screen.fill(black)
        message_display("3", screen_width / 2, screen_height / 2, 100, white)
        pygame.display.update()
        time.sleep(1)
        break
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
        screen.fill(black)
        message_display("2", screen_width / 2, screen_height / 2, 100, white)
        pygame.display.update()
        time.sleep(1)
        break
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
        screen.fill(black)
        message_display("1", screen_width / 2, screen_height / 2, 100, white)
        pygame.display.update()
        time.sleep(1)
        break
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
        time.sleep(1)
        break


# a button form function
def button_fun(msg, x_coor, y_coor, width, height, active_color, inactive_color, text_size, text_color, act = None):
    global enemy, interval_enemy, bullet, index_enemy, interval_bullet, index_bullet, x, y
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if mouse[0] > x_coor and mouse[0] < x_coor + width and mouse[1] > y_coor and mouse[1] < y_coor + height:
        pygame.draw.rect(screen, active_color, (x_coor, y_coor, width, height))
        if click[0] == 1 and act != None:
            # start mechanism
            if act == "start":
                x = 170
                y = 400
                spacecraft(x, y)
                pygame.display.update()
                # initialize the enemy list
                enemy = []
                for i in range(10):
                    enemy.append(Enemy())
                interval_enemy = 15
                index_enemy = 0
                # initialize the bullet list
                bullet = []
                for m in range(7):
                    bullet.append(Bullet())
                interval_bullet = 3
                index_bullet = 0
                game_loop()
            elif act == "quit":
                pygame.quit()
                os._exit(0)
            elif act == "continue":
                countdown()
                unpause()
            elif act == "menu":
                intro_menu()
            elif act == "help":
                game_help()
            elif act == "credit":
                credit()
    else:
        pygame.draw.rect(screen, inactive_color, (x_coor, y_coor, width, height))
    message_display(msg, (x_coor + width / 2), (y_coor + height / 2), text_size, text_color)
    
# the help of the game
def game_help():
    helped = True
    while helped:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
        screen.fill(black)
        message_display("AirBattle -- Help", 164, 45, 50, white)
        message_display("Welcome to the game Air Battle!", 190, 90, 30, yellow)
        message_display("Try to hit your enemies,", 148, 130, 30, steelblue)
        message_display("while avoid crashing into them!", 188, 170, 30, steelblue)
        message_display("Use Arrow Keys:", 112, 210, 30, green)
        message_display("Left, Right, Up and Down", 153, 250, 30, green)
        message_display("to control your Spacecraft", 160, 290, 30, green)
        message_display("Use Keyboard 'p' to pause the game", 205, 330, 30, red)
        message_display("Have fun!", 98, 370, 40, white)
        button_fun("Back to Main Menu", 80, 400, 240, 50, steelblue, darkersteelblue, 35, blue, "menu")
        pygame.display.update()
        clock.tick(10)

# display the list of credits
def credit():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
        screen.fill(black)
        message_display("AirBattle -- Credits", 175, 45, 50, white)
        message_display("Game Version:", 200, 100, 40, green)
        message_display("1.0.0", 200, 140, 50, green)
        message_display("Graphic Editor: Jiaxin Bu", 190, 200, 40, skyblue)
        message_display("Designer: Xinran Wang", 177, 250, 40, skyblue)
        message_display("Programmer: Xinran Wang", 200, 300, 40, skyblue)
        message_display("2019.5", 200, 355, 45, white)
        button_fun("Back to Main Menu", 80, 400, 240, 50, steelblue, darkersteelblue, 35, blue, "menu")
        pygame.display.update()
        clock.tick(10)

# display the score on the screen
def display_count(count):
    count_font = pygame.font.Font(None, 40)
    text = count_font.render("Score: " + str(count), True, red)
    screen.blit(text, (10, 10))

# after crash
def crash(count):
   
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)

        screen.fill(black)
        message_display("Game Over!", 200, 120, 80, red)
        message_display("Your Score is: " + str(count), 200, 190, 60, red)
        
        button_fun("Play Again", 80, 250, 240, 50, bright_green, green, 35, blue, "start")
        button_fun("Main Menu", 80, 330, 240, 50, bright_red, red, 35, blue, "menu")
        
        pygame.display.update()
        
# a function checking whether the bullet hits enemy
def hit(enemy, bullet):
    if enemy.x < bullet.x and bullet.x + bullet_width < enemy.x + enemy_width:
        if enemy.y < bullet.y and bullet.y < enemy.y + enemy_height - 5:
            enemy.active = False
            bullet.active = False
            return True
    else:
        return False
    
# a function dealing with fonts
def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

# a function sending messages
def message_display(text, position_x, position_y, fontsize, color):
    # set the font and size
    large_text = pygame.font.Font(None, fontsize)
    TextSurf, TextRect = text_objects(text, large_text, color)
    # the position of the text
    TextRect.center = (position_x, position_y)
    # update the display
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# the main loop of the game
def game_loop():
    global paused, interval_enemy, index_enemy, interval_bullet, index_bullet, x, y
    
    x_change = 0
    y_change = 0
    count = 0

    Exit = False
    
    while not Exit:
        
        for e in pygame.event.get():
            
            # decide whether to quit
            if e.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
    
            # keyboard control
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    x_change = - 6
                elif e.key == pygame.K_RIGHT:
                    x_change = 6
                elif e.key == pygame.K_UP:
                    y_change = - 6
                elif e.key == pygame.K_DOWN:
                    y_change = 6
                elif e.key == pygame.K_p:
                    paused = True
                    pause()
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    x_change = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    y_change = 0
        
        # update the position of x and y
        x += x_change
        y += y_change
        
        # background
        screen.fill(black)
        spacecraft(x, y)
        display_count(count)
        
        # shoot bullets
        interval_bullet -= 1
        if interval_bullet <= 0:
            interval_bullet = 13
            bullet[index_bullet].restart()
            index_bullet = (index_bullet + 1) % 7
        
        # the enemies appear
        interval_enemy -= 1
        if interval_enemy <= 0:
            interval_enemy = 8
            enemy[index_enemy].restart()
            index_enemy = (index_enemy + 1) % 10
            
        for b in bullet:
            if b.active:
                b.shoot()
                screen.blit(b.image, (b.x, b.y))
            for e in enemy:
                if e.active:
                    e.move()
                    screen.blit(e.image, (e.x, e.y))
                    # sucessfully shoot the enemy
                    if e.active == True:
                        outcome = hit(e, b)
                        if outcome == True:
                            count += 1
                    # crashed!
                    if y < e.y + enemy_height - 8 and y + spacecraft_height > e.y:
                        if x + spacecraft_width - 4 > e.x and x < enemy_width + e.x - 4:
                            time.sleep(0.5)
                            crash(count)
            

        
        # if the spacecraft is to cross the boarder, make it stay still
        if x < 0:
            x = 0
        if x > screen_width - spacecraft_width:
            x = screen_width - spacecraft_width
        if y < 0:
            y = 0
        if y > screen_height - spacecraft_height:
            y = screen_height - spacecraft_height
    
        # update the display
        pygame.display.update()
        clock.tick(60)

def main():
    intro_menu()
    # quit the loop and quit the game
    pygame.quit()
    os._exit(0)

if __name__ == "__main__": 
    main()
