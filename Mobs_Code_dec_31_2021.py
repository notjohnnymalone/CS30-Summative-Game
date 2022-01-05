##########
#Pygame_Final_Project
#Mobs_Code_dec_31_2021
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########

#Import the needed features
import pygame
import random
from os import path

BLACK = (0, 0, 0)
Mob_x = {'mob_speedx' : -2}
Mob_2_x = {'mob_speedx' : -2}
Mob_3_x = {'mob_speedx' : -2}
Mob_4_x = {'mob_speedx' : -2}

class Mobs(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 805
        self.rect.y = 290
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_x.get('mob_speedx')
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
        self.image = pygame.Surface((25, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 225
        self.rect.y = 162
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_2_x.get('mob_speedx')
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
        self.image = pygame.Surface((25, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 228
        self.rect.y = 386
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_3_x.get('mob_speedx')
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
        self.image = pygame.Surface((25, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 642
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Mob_4_x.get('mob_speedx')
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
