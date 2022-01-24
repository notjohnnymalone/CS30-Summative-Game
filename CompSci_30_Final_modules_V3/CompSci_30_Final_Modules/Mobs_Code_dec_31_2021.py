##########
#Pygame_Final_Project
#Mobs_Code_dec_31_2021
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########

#Import the needed features
from itertools import repeat#makes it so we can repeat stuff
import pygame
import random
from os import path
from CompSci_30_Final_Modules import Settings_Code_dec_31_2021
img_dir = path.join(path.dirname(__file__), 'Final_img')

#
#BLACK = (0, 0, 0)
Mob_x = {'mob_speedx' : -2}
Mob_2_x = {'mob_speedx' : -2}
Mob_3_x = {'mob_speedx' : -2}
Mob_4_x = {'mob_speedx' : -2}


class Mobs(pygame.sprite.Sprite):#the mobs function
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []#makes a list for the animated images
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))#sets the photo for each update of the code
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:#makes the code ignore the balck on the sprite photos for everything in the list
            frame.set_colorkey(Settings_Code_dec_31_2021.BLACK)#ignores all black colors
        self.index = 0
        self.image = self.images[self.index]#idk
        self.rect = self.image.get_rect()
        self.rect.x = 805#stes the x and y values here and below
        self.rect.y = 290
        self.on_ground = False#sets self on ground to false incase we were to add a  jump feature
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    def update(self, xvel, yvel, platforms, mobs):#the update for the mob code
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_x.get('mob_speedx')#changes thespeed of the mob based off whats in the list
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]#all above changes the code for the images, it will only call one image, and 
        
        for c in platforms:#calls this function for any platfrom touched
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:#if you are going right the code will make you go right untill the next collision
                    Settings_Code_dec_31_2021.Mob_x.clear()#clears the code for the x spee
                    Settings_Code_dec_31_2021.Mob_x['mob_speedx'] = (-2)#makes the x speed - to make the mob move left
                if new_Mob_speedx < 0:#does the exact same as the above code but going the other way
                    Settings_Code_dec_31_2021.Mob_x.clear()
                    Settings_Code_dec_31_2021.Mob_x['mob_speedx'] = (2)
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_x.get('mob_speedx')#appends the code to the mob to make it actually move
        self.rect.x = self.rect.x + new_Mob_speedx#makes the mob actually move
#for any information on the below code please refer to the code above, it is the same all through all of this.    
class Mobs_2(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 162
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_2_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Settings_Code_dec_31_2021.Mob_2_x.clear()
                    Settings_Code_dec_31_2021.Mob_2_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Settings_Code_dec_31_2021.Mob_2_x.clear()
                    Settings_Code_dec_31_2021.Mob_2_x['mob_speedx'] = (2)
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_2_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx

class Mobs_3(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 228
        self.rect.y = 386
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_3_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Settings_Code_dec_31_2021.Mob_3_x.clear()
                    Settings_Code_dec_31_2021.Mob_3_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Settings_Code_dec_31_2021.Mob_3_x.clear()
                    Settings_Code_dec_31_2021.Mob_3_x['mob_speedx'] = (2)
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_3_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx
        
class Mobs_4(pygame.sprite.Sprite):
    def __init__(self, platforms, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_1.png')).convert(), 40))
        self.images.extend(repeat(pygame.image.load(path.join(img_dir,'goomboo_2.png')).convert(), 40))
        for frame in self.images:
            frame.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 642
        self.on_ground = False
        self.vel = pygame.Vector2((0, 0))
        self.platforms = platforms
        
    def update(self, xvel, yvel, platforms, mobs):
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_4_x.get('mob_speedx')
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        for c in platforms:
            if pygame.sprite.collide_rect(self, c):
                if new_Mob_speedx > 0:
                    Settings_Code_dec_31_2021.Mob_4_x.clear()
                    Settings_Code_dec_31_2021.Mob_4_x['mob_speedx'] = (-2)
                if new_Mob_speedx < 0:
                    Settings_Code_dec_31_2021.Mob_4_x.clear()
                    Settings_Code_dec_31_2021.Mob_4_x['mob_speedx'] = (2)
        new_Mob_speedx = Settings_Code_dec_31_2021.Mob_4_x.get('mob_speedx')
        self.rect.x = self.rect.x + new_Mob_speedx

if __name__ == "__main__":
    print("Wrong file.")#tells you that you are on the wrong file...obviously.