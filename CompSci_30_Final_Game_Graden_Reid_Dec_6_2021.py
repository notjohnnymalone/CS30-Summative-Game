##########
#Pygame_Final_Project
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########

#Import the needed features
import pygame
import random
from os import path

#Load image/sound files up
img_dir = path.join(path.dirname(__file__), 'Final_img')#Reid we have to make the same file on our respective computers.
snd_dir = path.join(path.dirname(__file__), 'Final_snd')

#Set Screen info
WIDTH = 480#we can change this later.
HEIGHT = 600
FPS = 60

#Get Pygame all set to use.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Regular Computer Classmates 2: Return Of Browser")
clock = pygame.time.Clock()

#player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image = 
        self.rect = self.image.get_rect()
        