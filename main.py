#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:13:32 2024

@author: jameslloyd
"""
#I used the following YouTube tutorial to get this project started (https://www.youtube.com/watch?v=G_LXB5C-r20) and I am very grateful to its creator (YouTube: @Pythondude, Twitter: MouhammadHamsho). 
from configuration import * 
from weapons import *
import sys
import pygame
from sprites import *
from enemy_plant import *
#print(pygame.display.list_modes())


class Spritesheet: 
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()

    def get_image(self, x, y, width, hight):
        sprite = pygame.Surface([width, hight])
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, hight))
        sprite.set_colorkey(BLACK)
        return sprite

class Game:
    def __init__(self):
        #self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), flags = pygame.RESIZABLE) #Trying to scale up the screen. 
        #self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), flags = pygame.RESIZABLE | pygame.SCALED) #Trying to scale up the screen. 
        self.clock = pygame.time.Clock()
        self.floor_spritesheet = Spritesheet('Sci_sprites/Lab_floor2.bmp')
        self.wall_spritesheet = Spritesheet('Sci_sprites/Lab_wall.bmp')
        self.water_spritesheet = Spritesheet('Sci_sprites/Water_lab_spill2.bmp')
        self.player_spritesheet = Spritesheet('Sci_sprites/Sprite_Scientist.bmp')
        self.enemy_spritesheet = Spritesheet('Sci_sprites/Tube.bmp')
        self.weapon_spritesheet = Spritesheet('Sci_sprites/Pipette.bmp')
        self.bullet_spritesheet = Spritesheet('Sci_sprites/Water_Drop.bmp')
        self.bench_spritesheet = Spritesheet('Sci_sprites/Lab_bench.bmp')
        self.chamber_spritesheet = Spritesheet('Sci_sprites/Growth_chamber.bmp')
        self.plant_spritesheet = Spritesheet('Sci_sprites/Plant.bmp')
        self.running = True 
        self.enemy_collided = False
        self.block_collided = False

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'B':
                    Block(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "R":
                    Water(self, j, i)
                if column == "W":
                    Weapon(self, j, i)
                if column == "T":
                    Bench(self, j, i)
                if column == "C":
                    Chamber(self, j, i)
                if column == "A":
                    Enemy_plant(self, j, i)

    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates() #this allows us to look for collisions 
        self.water = pygame.sprite.LayeredUpdates() #this allows us to look for collision 
        self.enemies = pygame.sprite.LayeredUpdates() #this allows us to look for collisions 
        self.mainPlayer = pygame.sprite.LayeredUpdates() #allows the player to die 
        self.weapons = pygame.sprite.LayeredUpdates() #adds weapons to the game 
        self.bullets = pygame.sprite.LayeredUpdates() #adds bullets to the game 
        self.healthbar = pygame.sprite.LayeredUpdates() #add healthbars to the game 
        self.bench = pygame.sprite.LayeredUpdates() #add bench to the game 
        self.chamber = pygame.sprite.LayeredUpdates() #add bench to the game 
        self.enemy_plant = pygame.sprite.LayeredUpdates() #adds a second type of enemy to avoid 
        self.createTileMap()

    def update(self):
        self.all_sprites.update()

    def events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if event.type == pygame.VIDEORESIZE:
            #     print("resized") #Debugging 
            #     screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            #     print(self.screen)
            #     self.draw()

    def draw(self):
        #print(self.screen)
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def camera(self): #Moves the camera with the player's sprite 
        if self.enemy_collided == False and self.block_collided == False: #Stops the camera moving if your player collides #updated version 
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x += PLAYER_STEPS
            elif pressed[pygame.K_RIGHT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x -= PLAYER_STEPS
            elif pressed[pygame.K_UP]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y += PLAYER_STEPS
            elif pressed[pygame.K_DOWN]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y -= PLAYER_STEPS

    def main(self):
        while self.running:
            self.events()
            self.camera()
            self.update()
            self.draw()


game = Game()
game.create()

while game.running:
    game.main()


pygame.quit()
sys.exit()

