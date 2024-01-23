#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:31:25 2024

@author: jameslloyd 
"""

from configuration import * 
from weapons import *
import pygame
import random
import math
from sprites import *


class Enemy_plant(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.healthbar = Enemy_Healthbar(game, self, x, y)
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.image = self.game.plant_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.numberSteps = random.choice([30, 40, 50, 60, 70])
        self.stallSteps = 20
        self.currentSteps = 0
        self.state = "moving"
        self.animationCounter = 1
        self.health = ENEMY_HEALTH #HP of the enemy 

    def move(self):
        if self.state == "moving":
            if self.direction == "left":
                self.x_change = self.x_change - ENEMY_STEPS
                self.currentSteps += 1
            elif self.direction == "right":
                self.x_change = self.x_change + ENEMY_STEPS
                self.currentSteps += 1
            elif self.direction == "up":
                self.y_change = self.y_change - ENEMY_STEPS
                self.currentSteps += 1
            elif self.direction == "down":
                self.y_change = self.y_change + ENEMY_STEPS
                self.currentSteps += 1
        elif self.state == "stalling":
            self.currentSteps += 1
            if self.currentSteps == self.stallSteps:
                self.state = "moving"
                self.currentSteps = 0
                self.direction = random.choice(['left', 'right', 'up', 'down'])

    def update(self):
        self.move()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
        self.x_change = 0
        self.y_change = 0
        if self.currentSteps == self.numberSteps:
            if self.state != "stalling":
                self.currentSteps = 0
            self.state = "stalling"
        self.collide_block()
        self.collide_Player()

    def collide_block(self):
        collideBlocks = pygame.sprite.spritecollide(self, self.game.blocks, False)
        collideWater = pygame.sprite.spritecollide(self, self.game.water, False)
        if collideBlocks or collideWater:
            if self.direction == "left":
                self.rect.x += PLAYER_STEPS
                self.direction = "right"
            elif self.direction == "right":
                self.rect.x -= PLAYER_STEPS
                self.direction = "left"
            elif self.direction == "up":
                self.rect.y += PLAYER_STEPS
                self.direction = "down"
            elif self.direction == "down":
                self.rect.y -= PLAYER_STEPS
                self.direction = "up"

    def collide_Player(self):
        collide =  pygame.sprite.spritecollide(self, self.game.mainPlayer, True)
        if collide:
            self.game.running = False

    def damage(self, amount):
        self.health = self.health - amount
        self.healthbar.damage(ENEMY_HEALTH, self.health)
        if self.health <= 0:
            self.kill()
            self.healthbar.kill()