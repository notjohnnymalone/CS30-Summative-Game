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
WIDTH = 800#we can change this later.
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Player properties
PLAYER_ACC = 0.65
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

#Get Pygame all set to use.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Regular Computer Classmates 2: Return Of Browser")
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
vec = pygame.math.Vector2
bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
timer = 0

def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

def jump(self):
    # jump only if standing on a platform
    self.rect.y += 2
    #hits = pygame.sprite.collide_rect(player, ground)
    hits = pygame.sprite.groupcollide(sprites, platform_sprites, False, False)
    self.rect.y -= 2
    if hits:
        self.vel.y = -PLAYER_JUMP

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 50))
    
    def ground(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 25
        
    def wall(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 250
        self.rect.centery = HEIGHT / 2 + 100
        
#player Class
class Player(pygame.sprite.Sprite):#stes attributes for the 2nd player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        #self.rect.centerx = WIDTH / 2
        #self.rect.bottom = HEIGHT - 50
        self.rect.center = (40, HEIGHT - 100)
        self.pos = vec(25, HEIGHT - 50)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        #self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pygame.K_UP]:
            jump(self)

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2
        if self.pos.y >= HEIGHT - 50:
            self.pos.y = HEIGHT - 50
        self.rect.midbottom = self.pos
        
player = Player()
ground = Ground()
cliff = Ground()
ground.ground()
cliff.wall()

sprites.add(player)
platform_sprites.add(ground, cliff)
all_sprites.add(player, ground, cliff)
running = True
game_over = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.blit(background, background_rect)
    if player.vel.y > 0:
            hits = pygame.sprite.groupcollide(sprites, platform_sprites, False, False)
            if hits:
#                 lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > cliff.rect.bottom:
                        lowest = hit
                if player.pos.y == cliff.rect.bottom:
                    print('cheese')
                if player.pos.x < cliff.rect.right + 10 and \
                   player.pos.x > cliff.rect.left - 10:
                    if player.pos.y < cliff.rect.centery:
                        player.pos.y = cliff.rect.top
                        player.vel.y = 0
    #if self.pos.x < 0 - self.rect.width / 2:
    if pygame.time.get_ticks()-timer > 1000:
            timer = pygame.time.get_ticks()
            bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            
    sprites.update()
    screen.fill(bg)
    all_sprites.draw(screen)
    pygame.display.flip()
    
pygame.quit()
#So far by this first update I have made the movement work the way I want to so far by making it able to move side to side with
#acceleration and deacceleration. it also has a jump feature like a parabola
#that goes up and down at varying speeds. next I have to work on making it work on platforms other than the ground, like a cliff.
