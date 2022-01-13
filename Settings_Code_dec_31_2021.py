##########
#Pygame_Final_Project
#Settings_Code_dec_31_2021
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########

import pygame
import random
from os import path

#Load image/sound files up
img_dir = path.join(path.dirname(__file__), 'Final_img')#Reid we have to make the same file on our respective computers.
snd_dir = path.join(path.dirname(__file__), 'Final_snd')

#Set Screen info
TILE_SIZE = 32
WIDTH = 1024#we can change this later.
HEIGHT = 700
FPS = 240

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
color = WHITE

# Player properties
PLAYER_ACC = 0.65
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 10
SCREEN_SIZE = pygame.Rect((0, 0, WIDTH, HEIGHT))
player_lives_number = [3]

#Screen colors
r = 175
b = 195
g = 225

bg = r, g, b

#Get Pygame all set to use.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Regular Computer Classmates 2: Return Of Browser")
vec = pygame.math.Vector2
camera = vec(0, 0)
time = 0

#Lists and dictionaries
Mob_x = {'mob_speedx' : -2}
Mob_2_x = {'mob_speedx' : -2}
Mob_3_x = {'mob_speedx' : -2}
Mob_4_x = {'mob_speedx' : -2}
Mob_number = [1]
Levers_color = []
Lever_1_xy = [896, 288]
Lever_2_xy = [256, 384]
#Levers = pygame.sprite.Group()
#Levers_2 = pygame.sprite.Group()
Level = [1]
# reading = open('Game_R_save.txt', 'r')
# working = reading.readlines()
R = [175]
#print(R)
G = [225]
B = [195]
Main_run = ['run']

#Sprite Groups and Clock
clock = pygame.time.Clock()

#timer = pygame.time.Clock()
# entities = pygame.sprite.Group()
Levers = pygame.sprite.Group()
Levers_2 = pygame.sprite.Group()

#Mobs = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
mobs = pygame.sprite.Group()

#Art and sound
platform_img = pygame.image.load(path.join(img_dir, "grass_green.png")).convert()
platform_img = pygame.transform.scale(platform_img, (35, 33))
platform_b_img = pygame.image.load(path.join(img_dir, "grass_brown.png")).convert()
platform_b_img = pygame.transform.scale(platform_b_img, (35, 33))
player_lives = pygame.image.load(path.join(img_dir, "graden_stand_right.png")).convert()
player_lives = pygame.transform.scale(player_lives, (55, 45))
player_lives.set_colorkey(BLACK)
player_lives_rect = player_lives.get_rect()
lever_green = pygame.image.load(path.join(img_dir, "lever_green.png")).convert()
lever_green = pygame.transform.scale(lever_green, (35, 33))
lever_red = pygame.image.load(path.join(img_dir, "lever_red.png")).convert()
lever_red = pygame.transform.scale(lever_red, (35, 33))
lever_red_rotate = pygame.transform.rotate(lever_red, 567)

#Backgounds
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()#what the background will look like.
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()
