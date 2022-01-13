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
from CompSci_30_Final_Modules import Levels_code_jan_1_2022
from CompSci_30_Final_Modules import Settings_Code_dec_31_2021
    
class Player_block(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((16, 35))
        self.image.fill(Settings_Code_dec_31_2021.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.rect.y = 50

class Player(Player_block):
    def __init__(self, platforms, mobs, pos, *groups):
        super().__init__(Settings_Code_dec_31_2021.WHITE, pos)
        self.vel = pygame.Vector2((0, 0))
        self.on_ground = False
        self.platforms = platforms
        self.mobs = mobs
        self.levers = Settings_Code_dec_31_2021.Levers
        self.levers_2 = Settings_Code_dec_31_2021.Levers_2
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
        print(self.rect.x)
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms, self.levers, self.levers_2, mobs)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming that were in the air
        self.on_ground = False
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms, self.levers, self.levers_2, mobs)
        #weird stuff
        if self.rect.y >= 615 and self.rect.x >= 940:
            Settings_Code_dec_31_2021.Level.append(3)
            main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)# r, g, b)
        if self.rect.y >= 635 and self.rect.x <= 80:
            print("you win")
            new_file = 'Game_save' + '.txt'
            writing = open(new_file, 'w')
            writing.write('1')
            writing.close()

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
            
        for L in Settings_Code_dec_31_2021.Levers:
            if pygame.sprite.collide_rect(self, L):
                Settings_Code_dec_31_2021.Levers_color.append("BLUE")
                if "BLUE" in Settings_Code_dec_31_2021.Levers_color:
                    if 'GREEN' in Settings_Code_dec_31_2021.Levers_color:
                        Settings_Code_dec_31_2021.Level.append(2)
                        Settings_Code_dec_31_2021.Levers_color.clear()
                        Settings_Code_dec_31_2021.Levers_color.clear()
                        main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)# r, g, b)
                    
        for R in Settings_Code_dec_31_2021.Levers_2:
            if pygame.sprite.collide_rect(self, R):
                Settings_Code_dec_31_2021.Levers_color.append("GREEN")
                if "BLUE" in Settings_Code_dec_31_2021.Levers_color:
                    if 'GREEN' in Settings_Code_dec_31_2021.Levers_color:
                        Settings_Code_dec_31_2021.Level.append(2)
                        Settings_Code_dec_31_2021.Levers_color.clear()
                        Settings_Code_dec_31_2021.Levers_color.clear()
                        main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)# r, g, b)
          
def main(Levers_color, bg, time):# r, g, b):
    new_file = 'Game_save' + '.txt'
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    player = Player(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    level_width  = len(Levels_code_jan_1_2022.level[0])*Settings_Code_dec_31_2021.TILE_SIZE
    level_height = len(Levels_code_jan_1_2022.level)*Settings_Code_dec_31_2021.TILE_SIZE
    entities.add(player)
    mob = Mobs_Code_dec_31_2021.Mobs(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mob_2 = Mobs_Code_dec_31_2021.Mobs_2(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mob_3 = Mobs_Code_dec_31_2021.Mobs_3(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mob_4 = Mobs_Code_dec_31_2021.Mobs_4(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mobs.add(mob, mob_2, mob_3)
    mobs.add(mob_4)
    lever_1 = Lever(Settings_Code_dec_31_2021.Levers)
    lever_2 = Lever_2(Settings_Code_dec_31_2021.Levers)
    x = y = 0
    if 3 in Settings_Code_dec_31_2021.Level:
        level = Levels_code_jan_1_2022.level_3
        writing = open(new_file, 'w')
        writing.write('3')
        writing.close()
    elif 2 in Settings_Code_dec_31_2021.Level:
        level = Levels_code_jan_1_2022.level_2
        writing = open(new_file, 'w')
        writing.write('2')
        writing.close()
    else:
        level = Levels_code_jan_1_2022.level
        Settings_Code_dec_31_2021.Levers.add(lever_1)
        Settings_Code_dec_31_2021.Levers_2.add(lever_2)
        writing = open(new_file, 'w')
        writing.write('1')
        writing.close()
    for row in level:
        for col in row:
            if col == "P":
                Platform((x, y), platforms, entities)
#             if col == "L":
#                 Lever((x, y), Levers, entities)
            if col == "W":
                Platform_wall((x, y), platforms, entities)
#             if col == "K":
#                 print(x, y)
#                 Lever_2((x, y), Levers_2, entities)
            if col == "E":
                ExitBlock((x, y), platforms, entities)
            x += Settings_Code_dec_31_2021.TILE_SIZE
        y += Settings_Code_dec_31_2021.TILE_SIZE
        x = 0
        
    while 1:
#         for e in pygame.event.get():
#             if e.type == pygame.QUIT: 
#                 return
#             if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
#                 return
        #print(r, g, b)
        Settings_Code_dec_31_2021.screen.fill(bg)
        Settings_Code_dec_31_2021.clock.tick(Settings_Code_dec_31_2021.FPS)
        #print(Level)
        if pygame.time.get_ticks() - time > 2000:
            time = pygame.time.get_ticks()
            r = sum(Settings_Code_dec_31_2021.R)
            Settings_Code_dec_31_2021.R.append(-3)
#             new_file = 'Game_R_save' + '.txt'
#             writing = open(new_file, 'w')
#             writing.write(r)
#             writing.close()
#             print(Settings_Code_dec_31_2021.R)
            #r = r - 3
            Settings_Code_dec_31_2021.G.append(-2)
            g = sum(Settings_Code_dec_31_2021.G)
#             new_file = 'Game_G_save' + '.txt'
#             writing = open(new_file, 'w')
#             writing.write(g)
#             writing.close()
            #g = g - 2
            Settings_Code_dec_31_2021.B.append(-1.5)
            b = sum(Settings_Code_dec_31_2021.B)
#             new_file = 'Game_Time_save' + '.txt'
#             writing = open(new_file, 'w')
#             writing.write(b)
#             writing.close()
            #b = b - 1.5
        
            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0
                
            bg = r,g,b
            #print(bg)
            #pygame.display.update()
            Settings_Code_dec_31_2021.clock.tick(Settings_Code_dec_31_2021.FPS)
        entities.add(mob, mob_2, mob_3, mob_4)
        entities.update(Levers_color, mob.vel.y, mob.platforms, player.mobs)
        mobs.draw(Settings_Code_dec_31_2021.screen)
        if 2 not in Settings_Code_dec_31_2021.Level:
            Settings_Code_dec_31_2021.Levers.draw(Settings_Code_dec_31_2021.screen)
            Settings_Code_dec_31_2021.Levers_2.draw(Settings_Code_dec_31_2021.screen)
        entities.draw(Settings_Code_dec_31_2021.screen)
        pygame.display.flip()
        pygame.display.update()
        timer.tick(60)
        print(Settings_Code_dec_31_2021.Levers_color)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return
        
class Platform(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((Settings_Code_dec_31_2021.RED), pos, *groups)
        self.image = pygame.Surface((35, 32))
        self.image = Settings_Code_dec_31_2021.platform_img
        self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        self.rect = self.image.get_rect(topleft=pos)
    
class Platform_wall(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((Settings_Code_dec_31_2021.RED), pos, *groups)
        self.image = pygame.Surface((35, 32))
        self.image = Settings_Code_dec_31_2021.platform_b_img
        self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        self.rect = self.image.get_rect(topleft=pos)
        
class Lever(Player_block):
    def __init__(self, *groups):
        super().__init__((Settings_Code_dec_31_2021.BLUE), *groups)
        self.image = pygame.Surface((35, 32))
        self.image.fill(Settings_Code_dec_31_2021.BLUE)
        #self.Levers = Levers
        self.rect = self.image.get_rect()
        self.rect.x = 896
        self.rect.y = 288

class Lever_2(Player_block):
    def __init__(self, pos, *groups):
        super().__init__((Settings_Code_dec_31_2021.GREEN), pos, *groups)
        self.image = pygame.Surface((35, 32))
        self.image.fill(Settings_Code_dec_31_2021.GREEN)
        #self.Levers = Levers
        self.rect = self.image.get_rect()
        self.rect.x = 256
        self.rect.y = 384
        
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
# while running:
Settings_Code_dec_31_2021.clock.tick(Settings_Code_dec_31_2021.FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         else:
#new_file = 'Game_save' + '.txt'
try:
    reading = open('Game_save.txt', 'r')
    working = reading.readlines()
    if "3" in working:
        Settings_Code_dec_31_2021.Level.append(3)
    if "2" in working:
        Settings_Code_dec_31_2021.Level.append(2)
    main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)
except:
    main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)#, r, g, b,)
    pygame.quit()
print("doe")
