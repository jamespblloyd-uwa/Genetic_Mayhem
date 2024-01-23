#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:16:36 2024

@author: jameslloyd 
"""

from configuration import * 
from weapons import *
import pygame
import random
import math

#To write text 
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 90)
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.wall_spritesheet.get_image(0, 0, self.width, self.height)
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Bench(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.bench_spritesheet.get_image(0, 0, self.width, self.height)
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Chamber(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        #self.image = self.game.chamber_spritesheet.get_image(0, 0, self.width, self.height)
        self.image = random.choice([self.game.chamber_spritesheet.get_image(0, 0, self.width, self.height), 
                                    self.game.chamber_spritesheet.get_image(32, 0, self.width, self.height), 
                                    self.game.chamber_spritesheet.get_image(64, 0, self.width, self.height)])
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        # self.x = x*TILESIZE2
        # self.y = y*TILESIZE2
        # self.width = TILESIZE2
        # self.height = TILESIZE2
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.floor_spritesheet.get_image(0, 0, self.width, self.height)
        #self.image = pygame.transform.scale(self.image, (64, 64)) #Experiment with scaling 
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.water
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.water_spritesheet.get_image(0, 0, self.width, self.height)
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.animationCounter = 1

    def animation(self): #Giving water movement 
        animate = [self.game.water_spritesheet.get_image(0, 0, self.width, self.height),
                   self.game.water_spritesheet.get_image(32, 0, self.width, self.height),
                   self.game.water_spritesheet.get_image(64, 0, self.width, self.height),]
        self.image = animate[math.floor(self.animationCounter)] 
        self.animationCounter += 0.01
        if self.animationCounter >= 3:
                    self.animationCounter = 0

    def update(self):
        self.animation()


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer=PLAYER_LAYER
        self.healthbar = Player_Healthbar(game, x, y)
        self.groups = self.game.all_sprites, self.game.mainPlayer
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0
        self.animationCounter = 1
        self.image = self.game.player_spritesheet.get_image(0, 0, self.width, self.height)
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = "right"
        self.swordEqipped = False
        self.counter = 0
        self.waitTime = 10 #15 #Tutorial had it at 10 but I think that is too fast so 15 or 20 would be better I think
        self.shootState = "shoot"
        self.health = PLAYER_HEALTH

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.x_change = self.x_change - PLAYER_STEPS
            self.direction = "left"
        elif pressed[pygame.K_RIGHT]:
            self.x_change = self.x_change + PLAYER_STEPS
            self.direction = "right"
        elif pressed[pygame.K_UP]:
            self.y_change = self.y_change - PLAYER_STEPS
            self.direction = "up"
        elif pressed[pygame.K_DOWN]:
            self.y_change = self.y_change + PLAYER_STEPS
            self.direction = "down"

    def update(self):
        self.move()
        self.animation()
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
        self.collide_block() #helps to look for collisions
        self.collide_enemy() #helps to look for collisions
        self.collide_weapon() #helps to look for collisions (with weapon)
        self.shoot_sword() #Lets the sword shoot like a gun 
        self.waitAfterShoot()
        self.x_change = 0
        self.y_change = 0

    def animation(self): #how we make the player look like they are moving/walking
        downAnimation = [self.game.player_spritesheet.get_image(0, 0, self.width, self.height),
                         self.game.player_spritesheet.get_image(32, 0, self.width, self.height),
                         self.game.player_spritesheet.get_image(64, 0, self.width, self.height),]
        
        leftAnimation = [self.game.player_spritesheet.get_image(0,32,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,32,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,32,self.width, self.height),]
        
        rightAnimation = [self.game.player_spritesheet.get_image(0,64,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,64,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,64,self.width, self.height),]

        upAnimation = [self.game.player_spritesheet.get_image(0,96,self.width, self.height),
                         self.game.player_spritesheet.get_image(32,96,self.width, self.height),
                         self.game.player_spritesheet.get_image(64,96,self.width, self.height),]
        if self.direction == "down": 
            if self.y_change == 0:
                self.image = self.game.player_spritesheet.get_image(0, 0, self.width, self.height)
                #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
            else:
                self.image = downAnimation[math.floor(self.animationCounter)]
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0
        if self.direction =="up":
            if self.y_change == 0:
                self.image = self.game.player_spritesheet.get_image(32, 96, self.width, self.height)
                #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
            
            else:
                self.image = upAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter=0
        if self.direction =="left":
            if self.x_change == 0:
                self.image = self.game.player_spritesheet.get_image(32, 32, self.width, self.height)
                #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
            else:
                self.image = leftAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0
        if self.direction =="right":
            if self.x_change == 0:
                self.image = self.game.player_spritesheet.get_image(32, 64, self.width, self.height)
                #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
            else:
                self.image = rightAnimation[math.floor(self.animationCounter)] 
                self.animationCounter += 0.2
                if self.animationCounter >= 3:
                    self.animationCounter = 0

    def collide_block(self): #this is how we check for collisions of the player with another object (block on map)
        pressed = pygame.key.get_pressed()
        collideBlock = pygame.sprite.spritecollide(self, self.game.blocks, False, pygame.sprite.collide_rect_ratio(0.85)) #Flase means that if there is a collision, do not make the block disappear
        collideWater = pygame.sprite.spritecollide(self, self.game.water, False, pygame.sprite.collide_rect_ratio(0.85)) #Flase means that if there is a collision, do not make the block disappear
        if collideBlock or collideWater:
            self.game.block_collided = True #Stops the camera moving if the player's sprite collides with another object
            if pressed [pygame.K_LEFT]:
                self.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS
        else:
            self.game.block_collided = False #helps with camera moving when not collided. 

    def collide_enemy(self): #this is how we check for collisions of the player with another object (enemy on map)
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self, self.game.enemies, False, pygame.sprite.collide_rect_ratio(0.85)) #False in this function means that if there is a collision, do not make the block disappear
        if collide: 
            #self.game.collided = True #Stops the camera moving if the player's sprite collides with another object
            self.game.enemy_collided = True #Stops the camera moving if the player's sprite collides with another object #updated
            if pressed [pygame.K_LEFT]:
                self.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                self.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= PLAYER_STEPS
            else: 
                self.game.enemy_collided = False #Alt way to state if player has collided with the enemy, but without issue from below's version
        #else: 
            #self.game.collided = False #helps with camera moving when not collided. #I removed it as it seemed to be overridding the camera stall from the collide block/water 

    def collide_weapon(self):
        collide = pygame.sprite.spritecollide(self, self.game.weapons, True)
        if collide:
            self.swordEqipped = True

    def shoot_sword(self):
        pressed = pygame.key.get_pressed()
        if self.shootState == "shoot":
            if self.swordEqipped:
                if pressed[pygame.K_z] or pressed[pygame.K_SPACE]:
                    Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState = "wait"

    def waitAfterShoot(self):
        if self.shootState == "wait":
            self.counter += 1
            if self.counter >= self.waitTime:
                self.counter = 0
                self.shootState = "shoot"

    def damage(self, amount):
        self.health = self.health - amount
        self.healthbar.damage()
        if self.health <= 0:
            self.kill()
            self.healthbar.kill_healthbar()
            self.game.running = 0


class Enemy(pygame.sprite.Sprite):
    kill_count = 0
    game_state = "playing"
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
        self.image = self.game.enemy_spritesheet.get_image(0, 0, self.width, self.height)
        #self.image = pygame.transform.scale2x(self.image) #Experiment with scaling v2
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.numberSteps = random.choice([20, 30, 40, 50, 60, 70, 80])
        self.stallSteps = 80
        self.currentSteps = 0
        self.state = "moving"
        self.animationCounter = 1
        self.health = ENEMY_HEALTH #HP of the enemy 
        self.shootCounter = 0 #This is to allow the enemy to shoot one bullet at a time and random intervals between shots
        self.waitShoot = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90])
        self.shootState = "halt"

    def shoot(self): #This lets the enemy shoot the player (well, at random)
        self.shootCounter += 1
        if self.shootCounter >= self.waitShoot:
            self.shootState = "shoot"
            self.shootCounter = 0

    def move(self):
        if self.state == "moving":
            if self.direction == "left":
                self.x_change = self.x_change - ENEMY_STEPS
                self.currentSteps += 1
                if self.shootState == "shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState = "halt"
            elif self.direction == "right":
                self.x_change = self.x_change + ENEMY_STEPS
                self.currentSteps += 1
                if self.shootState=="shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState = "halt"
            elif self.direction == "up":
                self.y_change = self.y_change - ENEMY_STEPS
                self.currentSteps += 1
                if self.shootState=="shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState = "halt"
            elif self.direction == "down":
                self.y_change = self.y_change + ENEMY_STEPS
                self.currentSteps += 1
                if self.shootState == "shoot":
                    Enemy_Bullet(self.game, self.rect.x, self.rect.y)
                    self.shootState = "halt"
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
        self.shoot()
        Enemy.kill_count
        self.change_wining()
        #print(Enemy.kill_count)

    def change_wining(self): 
        if self.kill_count >= 7:
            text = font.render("You Win", True, RED, WHITE)
            text_rectangle = text.get_rect()
            text_rectangle.center = (screen.get_width() // 2, screen.get_height() // 2) #This displays the text in the middle of the screen! 
            screen.blit(text, text_rectangle) #Drawing test stating that you won after you won. 
            pygame.display.flip()
            pygame.time.delay(2000) #Pause the game so that the You Win text does not flash but seems to crash python
            self.game.running = 0 #End the game after pause. Seems to work despite previous step stalling Python 

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

    def damage(self, amount):
        self.health = self.health - amount
        self.healthbar.damage(ENEMY_HEALTH, self.health)
        if self.health <= 0:
            self.kill()
            self.healthbar.kill()
            Enemy.kill_count += 1


class Player_Healthbar(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.healthbar
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = 40
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y - TILESIZE/2

    def move(self):
        self.rect.x = self.game.player.rect.x
        self.rect.y = self.game.player.rect.y - TILESIZE/2

    def kill_healthbar(self):
        self.kill()

    def damage(self):
        self.image.fill(RED)
        width = self.rect.width * self.game.player.health/PLAYER_HEALTH
        pygame.draw.rect(self.image, GREEN, (0, 0, width, self.height), 0)

    def update(self):
        self.move()


class Enemy_Healthbar(pygame.sprite.Sprite):
    def __init__(self, game, enemy, x, y):
        self.enemy= enemy
        self.game = game
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites, self.game.healthbar
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x*TILESIZE
        self.y = y*TILESIZE
        self.width = 40
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y - TILESIZE/2

    def move(self):
        self.rect.x = self.enemy.rect.x
        self.rect.y = self.enemy.rect.y - TILESIZE/2

    def damage(self, totalHealth, health):
        self.image.fill(RED)
        width = self.rect.width * health/totalHealth #Gives us a bar that reduces in length as the health decreases 
        pygame.draw.rect(self.image, WHITE, (0, 0, width , self.height), 0)

    def kill_bar(self):
        self.kill()

    def update(self):
        self.move()

