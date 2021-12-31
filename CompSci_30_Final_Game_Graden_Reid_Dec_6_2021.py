##########
#Pygame_Final_Project
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########

#Import the needed features
import pygame
import random
from os import path
from CompSci_30_Final_Modules import Mobs_Code_dec_31_2021

#Load image/sound files up
img_dir = path.join(path.dirname(__file__), 'Final_img')#Reid we have to make the same file on our respective computers.
snd_dir = path.join(path.dirname(__file__), 'Final_snd')

#Set Screen info
TILE_SIZE = 32
WIDTH = 1024#we can change this later.
HEIGHT = 720
FPS = 120

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
clock = pygame.time.Clock()
Mobs = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
vec = pygame.math.Vector2
camera = vec(0, 0)
time = 0

#Lists and other stuff
Mob_x = {'mob_speedx' : -2}
Mob_2_x = {'mob_speedx' : -2}
Mob_3_x = {'mob_speedx' : -2}
Mob_4_x = {'mob_speedx' : -2}
Mob_number = [1]
Levers_color = []
Levers = pygame.sprite.Group()
Levers_2 = pygame.sprite.Group()

class CameraAwareLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, world_size):
        super().__init__()
        self.target = target
        self.cam = pygame.Vector2(0, 0)
        self.world_size = world_size
        if self.target:
            self.add(target)

    def update(self, *args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width/2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height/2
            self.cam += (pygame.Vector2((x, y)) - self.cam) * 0.05
            self.cam.x = max(-(self.world_size.width-SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height-SCREEN_SIZE.height), min(0, self.cam.y))
    
    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty
    
class Player_block(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((16, 35))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.rect.y = 50

class Player(Player_block):
    def __init__(self, platforms, mobs, pos, *groups):
        super().__init__(WHITE, pos)
        self.vel = pygame.Vector2((0, 0))
        self.on_ground = False
        self.platforms = platforms
        self.mobs = mobs
        self.levers = Levers
        self.levers_2 = Levers_2
        self.speed = 8
        self.jump_strength = 8
        self.last_update = pygame.time.get_ticks()
        
    def update(self, levers_color, yvel, platforms, mobs):
        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_UP]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        running = pressed[pygame.K_SPACE]
        
        if up:
            # only jump if on the ground
            if self.on_ground: self.vel.y = -self.jump_strength
        if left:
            self.vel.x = -self.speed
        if right:
            self.vel.x = self.speed
        if running:
            self.vel.x *= 1.5
        if not self.on_ground:
            # only accelerate with gravity if in the air
            self.vel.y += .3
            # max falling speed
            if self.vel.y > 100: self.vel.y = 100
        if not(left or right):
            self.vel.x = 0
        # increment in x direction
        self.rect.left += self.vel.x
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms, self.levers, self.levers_2, mobs)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming that were in the air
        self.on_ground = False
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms, self.levers, self.levers_2, mobs)
        #weird stuff
        
    def collide(self, xvel, yvel, platforms, levers, levers_2, mobs):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.vel.y = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        if pygame.sprite.spritecollide(self, mobs, False):
            self.rect.x = 45
            self.rect.y = 50
            
        for L in Levers:
            if pygame.sprite.collide_rect(self, L):
                Levers_color.append("BLUE")
                if "BLUE" in Levers_color:
                    if 'GREEN' in Levers_color:
                        print("welcome to the final battle")
                        Levers_color.remove('BLUE')
                        Levers_color.remove('GREEN')
                    
        for R in Levers_2:
            if pygame.sprite.collide_rect(self, R):
                Levers_color.append("GREEN")
                if "BLUE" in Levers_color:
                    if 'GREEN' in Levers_color:
                        print("welcome to the final battle")
                        Levers_color.remove('BLUE')
                        Levers_color.remove('GREEN')
          
def main(Levers_color, bg, time, r, g, b):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()

    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                              P",
        "P                              P",
        "P                              P",
        "P                              P",
        "P P       P                    P",
        "P PPPPPPPPP                    P",
        "P            PPP               P",
        "P                              P",
        "P    PPPPPP          P         P",
        "P    P               PPPPPPPPPPP",
        "P    P                         P",
        "P    P K    P                  P",
        "P    PPPPPPPP    PP            P",
        "P                            L P",
        "P                          PPPPP",
        "P                 PPPPPP       P",
        "P                              P",
        "P         PPPPPPP              P",
        "P                              P",
        "P                     PPPPPP   P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]

    platforms = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    player = Player(platforms, mobs, (TILE_SIZE, TILE_SIZE))
    level_width  = len(level[0])*TILE_SIZE
    level_height = len(level)*TILE_SIZE
    #entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))
    entities = pygame.sprite.Group()
    entities.add(player)
    mob = Mobs_Code_dec_31_2021.Mobs(platforms, mobs, (TILE_SIZE, TILE_SIZE))
    mob_2 = Mobs_Code_dec_31_2021.Mobs_2(platforms, mobs, (TILE_SIZE, TILE_SIZE))
    mob_3 = Mobs_Code_dec_31_2021.Mobs_3(platforms, mobs, (TILE_SIZE, TILE_SIZE))
    mob_4 = Mobs_Code_dec_31_2021.Mobs_4(platforms, mobs, (TILE_SIZE, TILE_SIZE))
    mobs.add(mob, mob_2, mob_3)
    mobs.add(mob_4)
    x = y = 0
    for row in level:
        for col in row:
            if col == "P":
                Platform((x, y), platforms, entities)
            if col == "L":
                Lever((x, y), Levers, entities)
            if col == "W":
                print(x, y)
                Wall((x, y), platforms, entities)
            if col == "K":
                print(x, y)
                Lever_2((x, y), Levers_2, entities)
            if col == "E":
                ExitBlock((x, y), platforms, entities)
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0
    
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                return
        print(r, g, b)
        screen.fill(bg)
        clock.tick(FPS)
        if pygame.time.get_ticks() - time > 2000:
            time = pygame.time.get_ticks()
            r = r - 3
            g = g - 2
            b = b - 1.5
        
            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0
                
            bg = r,g,b
            #print(bg)
            #pygame.display.update()
            clock.tick(FPS)
        entities.add(mob, mob_2, mob_3, mob_4)
        entities.update(Levers_color, mob.vel.y, mob.platforms, player.mobs)
        mobs.draw(screen)
        entities.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        timer.tick(60)
        
        
class Platform(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((RED), pos, *groups)
        self.image = pygame.Surface((35, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=pos)
        
class Lever(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((BLUE), pos, *groups)
        self.image = pygame.Surface((35, 32))
        print(Levers_color)
        self.image.fill(BLUE)
        #self.Levers = Levers
        self.rect = self.image.get_rect(topleft=pos)

class Lever_2(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((GREEN), pos, *groups)
        self.image = pygame.Surface((35, 32))
        print(Levers_color)
        self.image.fill(GREEN)
        #self.Levers = Levers
        self.rect = self.image.get_rect(topleft=pos)
        
class Wall(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((RED), pos, *groups)
        self.image = pygame.Surface((35, 32))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=pos)

class ExitBlock(Player_block):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

# player =  Player(sprites, (TILE_SIZE, TILE_SIZE))
#all_sprites.add(player)
running = True
game_over = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        else:
            main(Levers_color, bg, time, r, g, b)
    
#So far by this first update I have made the movement work the way I want to so far by making it able to move side to side with
#acceleration and deacceleration. it also has a jump feature like a parabola
#that goes up and down at varying speeds. next I have to work on making it work on platforms other than the ground, like a cliff.
