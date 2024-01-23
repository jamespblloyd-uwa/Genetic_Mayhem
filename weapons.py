#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:04:53 2024

@author: jameslloyd 
"""

#from sprites import *
from configuration import *
import pygame
import math


class Weapon(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.weapon_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Bullet(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.bullet_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = self.game.player.direction
        self.damage = 1
        
    def move(self):
        if self.direction =="right":
            self.rect.x += BULLET_STEPS
        if self.direction =="left":
            self.rect.x -= BULLET_STEPS
        if self.direction =="up":
            self.rect.y -= BULLET_STEPS
        if self.direction =="down":
            self.rect.y += BULLET_STEPS

    def collide_block(self):
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if collide:
            self.kill()

    def collide_Enemy(self):
        collide = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if collide:
            collide[0].damage(self.damage) #This states that the enemy hit [0] is the one that has its health reduced, and it passes the amount of damage (danage is deined under bullet)
            self.kill()

    def update(self):
       self.move()
       self.collide_Enemy()
       self.collide_block()


class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x ,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.bullet_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = self.game.player.direction
        self.damage = 1

    def move(self):
        if self.direction =="right":
            self.rect.x += BULLET_STEPS
        if self.direction =="left":
            self.rect.x -= BULLET_STEPS
        if self.direction =="up":
            self.rect.y -= BULLET_STEPS
        if self.direction =="down":
            self.rect.y += BULLET_STEPS

    def collide_block(self):
         collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
         if collide:
             self.kill()

    def collide_Player(self):
         collide = pygame.sprite.spritecollide(self, self.game.mainPlayer, False)
         if collide:
             self.game.player.damage(self.damage)
             self.kill()

    def update(self):
        self.move()
        self.collide_Player()
        self.collide_block()


