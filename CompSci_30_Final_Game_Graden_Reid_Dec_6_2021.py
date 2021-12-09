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

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Get Pygame all set to use.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Regular Computer Classmates 2: Return Of Browser")
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

#player Class
class Player(pygame.sprite.Sprite):#stes attributes for the 2nd player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.speedy = -8
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
player = Player()
sprites.add(player)
running = True
game_over = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.blit(background, background_rect)
    sprites.update()
    screen.fill(RED)
    sprites.draw(screen)
    pygame.display.flip()
pygame.quit()