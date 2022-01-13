##########
#Pygame_Final_Project
#Mobs_Code_dec_31_2021
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########

#Import the needed features
from itertools import repeat
import pygame
import random
from os import path
#pygame.init()
img_dir = path.join(path.dirname(__file__), 'Final_img')

BLACK = (0, 0, 0)
Mob_x = {'mob_speedx' : -2}
Mob_2_x = {'mob_speedx' : -2}
Mob_3_x = {'mob_speedx' : -2}
Mob_4_x = {'mob_speedx' : -2}


class Mobs(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 805
        self.rect.y = 290
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Mob_x.clear()
                    Mob_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Mob_x.clear()
                    Mob_x['mob_speedx'] = (2)
        new_Mob_speedx = Mob_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx
        
class Mobs_2(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 162
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_2_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Mob_2_x.clear()
                    Mob_2_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Mob_2_x.clear()
                    Mob_2_x['mob_speedx'] = (2)
        new_Mob_speedx = Mob_2_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx

class Mobs_3(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 228
        self.rect.y = 386
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_3_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Mob_3_x.clear()
                    Mob_3_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Mob_3_x.clear()
                    Mob_3_x['mob_speedx'] = (2)
        new_Mob_speedx = Mob_3_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx
        
class Mobs_4(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 642
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_4_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Mob_4_x.clear()
                    Mob_4_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Mob_4_x.clear()
                    Mob_4_x['mob_speedx'] = (2)
        new_Mob_speedx = Mob_4_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx


