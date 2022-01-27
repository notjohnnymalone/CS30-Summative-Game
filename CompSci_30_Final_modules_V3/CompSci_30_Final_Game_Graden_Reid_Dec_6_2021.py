##########
#Pygame_Final_Project
#Graden_Rusk_and_Reid_Martin
#Dec_3_2021-Jan_2022
##########
#Import the needed features
import time
import pygame
import random
from os import path
from CompSci_30_Final_Modules import Mobs_Code_dec_31_2021
from CompSci_30_Final_Modules import Levels_code_jan_1_2022
from CompSci_30_Final_Modules import Settings_Code_dec_31_2021


#tells what format to print in
def draw_lives(surf, x, y, img):# draws the five lives in the top right.
    lives = sum(Settings_Code_dec_31_2021.player_lives_number)
    for i in range(lives):# prints out number of lives total
        img_rect = img.get_rect()
        img_rect.x = x + 35 * i
        img_rect.y = y
        surf.blit(img, img_rect)#puts it on the screen
        
def draw_text(surf, text, size, x, y):#draws our text to the screen
    font = pygame.font.Font(Settings_Code_dec_31_2021.font_name, size)#imports the size and the desired font
    text_surface = font.render(text, True, Settings_Code_dec_31_2021.FOREST_GREEN)#makes the text green
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)#adds it to the screen

def show_go_screen():#our starting screen
    background_color = (sum(Settings_Code_dec_31_2021.R), sum(Settings_Code_dec_31_2021.G), sum(Settings_Code_dec_31_2021.B))
    Settings_Code_dec_31_2021.screen.fill(background_color)#I added this to make the start and end screen match the background color
#    Settings_Code_dec_31_2021.screen.fill(Settings_Code_dec_31_2021.background_color)#I added this to make the start and end screen match the background color
    draw_text(Settings_Code_dec_31_2021.screen, "Regular Computer Classmates 2: Return Of Browser", 40,#changes the name.
              Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT / 3)
    draw_text(Settings_Code_dec_31_2021.screen, "Use The Arrow Keys To Play", 18,
              Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT * 5 / 8)
    draw_text(Settings_Code_dec_31_2021.screen, "Hit All of The Levers To Pass The Level", 25,
              Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT / 2)
    draw_text(Settings_Code_dec_31_2021.screen, "Press any key to begin", 18, Settings_Code_dec_31_2021.WIDTH / 2,
              Settings_Code_dec_31_2021.HEIGHT * 3 / 4)#all of the code above gets printed to the screen
    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    waiting = True
    while waiting:#causes it to repeat so you can actually see the opening screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False#checks for anything to get pressed and closes out of the loop

def end_screen():#this is the big ending screen
    if sum(Settings_Code_dec_31_2021.R) <= 0:
        background_color = (0, 0, 0)
    else:
        background_color = (sum(Settings_Code_dec_31_2021.R), sum(Settings_Code_dec_31_2021.G), sum(Settings_Code_dec_31_2021.B))
#     print(background_color)
    Settings_Code_dec_31_2021.screen.fill(background_color)
    reading = open('Game_save.txt', 'r')
    working = reading.readlines()#opens the file to a list
    if "4" in working:
        Settings_Code_dec_31_2021.screen.fill(background_color)
        draw_text(Settings_Code_dec_31_2021.screen, "You Win!", 64, Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT / 4)
        draw_text(Settings_Code_dec_31_2021.screen, f"Thanks for playing", 35,#calls the draw text function
              Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT / 2)
    elif "3" in working:#all of these check for their corresponding number in the list.
        death_level = 3
    elif "2" in working:
        death_level = 2
    else:
        death_level = 1
    if "4" not in working:
        draw_text(Settings_Code_dec_31_2021.screen, "You Died!", 64, Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT / 4)
        draw_text(Settings_Code_dec_31_2021.screen, f"You made it to Level {death_level}.", 35,#calls the draw text function
                  Settings_Code_dec_31_2021.WIDTH / 2, Settings_Code_dec_31_2021.HEIGHT / 2)
    new_file = 'Game_save' + '.txt'
    level = Levels_code_jan_1_2022.level
    writing = open(new_file, 'w')
    writing.write('1')#changes the level to one by chaging the save file
    writing.close()
    pygame.display.flip()
    Settings_Code_dec_31_2021.Main_run.clear()
    run = True
    while run:  
        for e in pygame.event.get():#chacks for the player leaving the game
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
#     time.sleep(10)#closes the program after ten seconds
#     pygame.quit()

class Player_block(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        # Sets images for the player, rect, and coordinates
        self.images = Settings_Code_dec_31_2021.player_sprite
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.rect.y = 50#sets the coordinates for the sprite to be at.
class Player(Player_block):
    def __init__(self, platforms, mobs, pos, *groups):
        super().__init__(Settings_Code_dec_31_2021.WHITE, pos)#calls the player_block class
        self.vel = pygame.Vector2((0, 0))
        self.on_ground = False
        self.platforms = platforms
        self.mobs = mobs
        self.levers = Settings_Code_dec_31_2021.Levers#imports the levers lists
        self.levers_2 = Settings_Code_dec_31_2021.Levers_2
        #speeds and jump, lives atributes
        self.speed = 8
        self.jump_strength = 8
        self.lives = 3
        self.index = 0
        #time update
        self.last_update = pygame.time.get_ticks()

    def update(self, levers_color, yvel, platforms, mobs):
        #sets attributes to make this easier
        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_UP]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        running = pressed[pygame.K_SPACE]
        
        #sets player sprite to standing
        self.index = 0
        
        if up:#checks for the up arrow
            # only jump if on the ground
            if self.on_ground:
                self.vel.y = -self.jump_strength
                Settings_Code_dec_31_2021.jump_sound.play()
        if left:#checks for the left arrow
            self.vel.x = -self.speed
            self.index = 5 #sprite left
        if right:#checks for the right arrow
            self.vel.x = self.speed
            self.index = 3 #sprite right
        if running:
            self.vel.x *= 1.5
        if not self.on_ground:
            # only accelerate with gravity if in the air
            self.vel.y += .3
            # max falling speed
            if self.vel.y > 100: self.vel.y = 100
        if not(left or right):
            self.vel.x = 0
            self.index = 0 #sprite front
        self.image = self.images[self.index] #allows the index to set the image
        # increment in x direction
        self.rect.left += self.vel.x
#         print(self.rect.x)
#         print(self.rect.y)
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms, self.levers, self.levers_2, mobs)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming that were in the air
        self.on_ground = False
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms, self.levers, self.levers_2, mobs)
    def collide(self, xvel, yvel, platforms, levers, levers_2, mobs):#our collisions fu
        for p in platforms:#it checks for collisions on any platform
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))#checks to see if you exited out of the program
                #all below make sure you cannot phase through blocks
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
        #checks for collisions with mobs, if you do you lose a life and respawn
        if pygame.sprite.spritecollide(self, mobs, False):
            self.rect.x = 45
            self.rect.y = 50
            #lowers your life
            Settings_Code_dec_31_2021.player_lives_number.append(-1)
            Settings_Code_dec_31_2021.death_sound.play()
            
        for L in Settings_Code_dec_31_2021.Levers:#checks for collisions witht one of the levers
            if pygame.sprite.collide_rect(self, L):
                Settings_Code_dec_31_2021.Levers_color.append("BLUE")#adds blue to the list of colors for the levers, it was made like this
                #because of what the levers looked like before actuall levers, blue and green.
                if "BLUE" in Settings_Code_dec_31_2021.Levers_color:#checks for Blue in the list
                    if 'GREEN' in Settings_Code_dec_31_2021.Levers_color:#checks for green in the list
                        #the next two if's ask for 3 or 2 in the level list, to decide what to append to the list.
                        if 3 in Settings_Code_dec_31_2021.Level:
                            Settings_Code_dec_31_2021.Level.append(4)
                        if 2 in Settings_Code_dec_31_2021.Level:
                            Settings_Code_dec_31_2021.Level.append(3)
                        else:
                            Settings_Code_dec_31_2021.Level.append(2)
                        Settings_Code_dec_31_2021.Levers_color.clear()#clears the color list for the start of the next levels
                        #Settings_Code_dec_31_2021.Levers_color.clear()
                        main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)# r, g, b)
         
        #This does the exact same thing as the "For L in" code above, but with different colors being added to the list and
        #then checks for the other color in the list. and clears them both again.
        for R in Settings_Code_dec_31_2021.Levers_2:
            if pygame.sprite.collide_rect(self, R):
                Settings_Code_dec_31_2021.Levers_color.append("GREEN")
                if "BLUE" in Settings_Code_dec_31_2021.Levers_color:
                    if 'GREEN' in Settings_Code_dec_31_2021.Levers_color:
                        if 3 in Settings_Code_dec_31_2021.Level:
                            Settings_Code_dec_31_2021.Level.append(4)
                        if 2 in Settings_Code_dec_31_2021.Level:
                            Settings_Code_dec_31_2021.Level.append(3)
                        else:
                            Settings_Code_dec_31_2021.Level.append(2)
                        Settings_Code_dec_31_2021.Levers_color.clear()
                        Settings_Code_dec_31_2021.Levers_color.clear()
                        main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)# r, g, b)
          
def main(Levers_color, bg, time):# r, g, b): #This is the main code for all of the game to run
    #sets attributes for the game to work, and the sprite groups
    new_file = 'Game_save' + '.txt'
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()#this and the next two start the player and mob code, and platforms code
    platforms = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    player = Player(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    level_width  = len(Levels_code_jan_1_2022.level[0])*Settings_Code_dec_31_2021.TILE_SIZE
    level_height = len(Levels_code_jan_1_2022.level)*Settings_Code_dec_31_2021.TILE_SIZE
    #Add entities to the list
    entities.add(player)
    #calls the function from the other four mobs
    mob = Mobs_Code_dec_31_2021.Mobs(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mob_2 = Mobs_Code_dec_31_2021.Mobs_2(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mob_3 = Mobs_Code_dec_31_2021.Mobs_3(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mob_4 = Mobs_Code_dec_31_2021.Mobs_4(platforms, mobs, (Settings_Code_dec_31_2021.TILE_SIZE, Settings_Code_dec_31_2021.TILE_SIZE))
    mobs.add(mob, mob_2, mob_3)
    mobs.add(mob_4)#these both add mobs to the mob sprite group, for the collisions to work
    lever_1 = Lever(Settings_Code_dec_31_2021.Levers)
    lever_2 = Lever_2(Settings_Code_dec_31_2021.Levers)
    #calls both lever code above.
    Settings_Code_dec_31_2021.Levers.add(lever_1)
    Settings_Code_dec_31_2021.Levers_2.add(lever_2)
    #appends both levers to the lever groups
    x = y = 0
    #below it checks for the level that you are on so it knows what level to load for you to play,
    #it also opens your save file and changes what level you are on there for you aswell
    if 4 in Settings_Code_dec_31_2021.Level:
        writing = open(new_file, 'w')
        writing.write('4')#clears the txt file and adds four
        writing.close()
        print("working")
        end_screen()#calls the end screen code
    if 3 in Settings_Code_dec_31_2021.Level:
        level = Levels_code_jan_1_2022.level_3#loads the platforms for the level
        writing = open(new_file, 'w')
        writing.write('3')
        writing.close()
        Settings_Code_dec_31_2021.Lever_1_xy.clear()#changes all of the x and y values for the levers for eac level so it makes sense.
        Settings_Code_dec_31_2021.Lever_1_xy.append(291)
        Settings_Code_dec_31_2021.Lever_1_xy.append(320)
        Settings_Code_dec_31_2021.Lever_2_xy.clear()
        Settings_Code_dec_31_2021.Lever_2_xy.append(35)
        Settings_Code_dec_31_2021.Lever_2_xy.append(640)
    elif 2 in Settings_Code_dec_31_2021.Level:
        level = Levels_code_jan_1_2022.level_2#loads the platforms for the level
        writing = open(new_file, 'w')
        writing.write('2')#these all clear the writing txt files and changes what t will load when you restart the game.
        writing.close()
        Settings_Code_dec_31_2021.Lever_1_xy.clear()#clears the lists
        Settings_Code_dec_31_2021.Lever_1_xy.append(35)#all of these will change all the coordinates are for the other levers that weren't changed before
        Settings_Code_dec_31_2021.Lever_1_xy.append(543)
        Settings_Code_dec_31_2021.Lever_2_xy.clear()#clears the lists
        Settings_Code_dec_31_2021.Lever_2_xy.append(768)
        Settings_Code_dec_31_2021.Lever_2_xy.append(383)
    else:
        level = Levels_code_jan_1_2022.level#makes the leve, level one
        writing = open(new_file, 'w')
        writing.write('1')
        writing.close()
    for row in level:# makes platforms for the level it's using
        for col in row:
            if col == "P":#if there is a p in the levels list it calls the platform function
                Platform((x, y), platforms, entities)
            if col == "W":#if there is a p in the levels list it calls the wall function, this was mainly used for coordinates for the mobas and levers early on
                Platform_wall((x, y), platforms, entities)
            if col == "E":#if there is an E in it it calls the exitblock function
                ExitBlock((x, y), platforms, entities)
            x += Settings_Code_dec_31_2021.TILE_SIZE
        y += Settings_Code_dec_31_2021.TILE_SIZE
        x = 0
    if sum(Settings_Code_dec_31_2021.player_lives_number) <= 0: #checks for the lives you have (the sum) and will play the end screen if your at zreo                                                                                                                           
            end_screen()
            Settings_Code_dec_31_2021.Main_run.remove('run')
        
    while 'run' in Settings_Code_dec_31_2021.Main_run:#starts the while loop for the main run
        #print(r, g, b)
        Settings_Code_dec_31_2021.screen.fill(bg)#fills the backfround color
        Settings_Code_dec_31_2021.clock.tick(Settings_Code_dec_31_2021.FPS)#refresh rate at FPS
        #print(Level)
        if pygame.time.get_ticks() - time > 2000:#below is the code for the background, after 2 seconds it will make the colors change to be darker
            time = pygame.time.get_ticks()
            r = sum(Settings_Code_dec_31_2021.R)
            Settings_Code_dec_31_2021.R.append(-3)#adds -3 to the R list to change color
            Settings_Code_dec_31_2021.G.append(-2)#adds -2 to the G list to change the color
            g = sum(Settings_Code_dec_31_2021.G)
            
            Settings_Code_dec_31_2021.B.append(-1.5)#adds -1.5 to the B list
            b = sum(Settings_Code_dec_31_2021.B)
        
            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0

            if r == 0 and g == 0 and b == 0:
                Settings_Code_dec_31_2021.player_lives_number.append(-5)
            bg = r,g,b#changes what BG is 
            Settings_Code_dec_31_2021.clock.tick(Settings_Code_dec_31_2021.FPS)
        entities.add(mob, mob_2, mob_3, mob_4)#add all the mobs to the entities to the sprite group
        entities.update(Levers_color, mob.vel.y, mob.platforms, player.mobs)
        mobs.draw(Settings_Code_dec_31_2021.screen)
        #calls the update functions, and draw to screen functions below.
        Settings_Code_dec_31_2021.Levers.update()
        Settings_Code_dec_31_2021.Levers_2.update()
        Settings_Code_dec_31_2021.Levers.draw(Settings_Code_dec_31_2021.screen)
        Settings_Code_dec_31_2021.Levers_2.draw(Settings_Code_dec_31_2021.screen)
        entities.draw(Settings_Code_dec_31_2021.screen)
        #draws the lives to the screen.
        draw_lives(Settings_Code_dec_31_2021.screen, Settings_Code_dec_31_2021.WIDTH - 180, 5, Settings_Code_dec_31_2021.player_lives)
        pygame.display.flip()#flips the screen so you can see everything placed on it
        Settings_Code_dec_31_2021.pygame.mixer.init#starts the cool jams
        pygame.display.update()#updates the display so things can actuall update
        timer.tick(60)
        if sum(Settings_Code_dec_31_2021.player_lives_number) <= 0:#chancks once again  for the number of lives 
            end_screen()#calls end screen
        #below it checks for any clicks to exit the program
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Settings_Code_dec_31_2021.Main_run.remove('run')
#                pygame.quit()
#                 return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return

class Platform(Player_block):#this is the player code that can be reused
    def __init__(self, pos, *groups):
        super().__init__((Settings_Code_dec_31_2021.RED), pos, *groups)
        self.image = pygame.Surface((35, 32))#controls the player siz
        self.image = Settings_Code_dec_31_2021.platform_img#chooses the player photo
        self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)#clears all of the black from the photo
        self.rect = self.image.get_rect(topleft=pos)#sets character position
    
class Platform_wall(Player_block):#calls the player block for more information
    def __init__(self, pos, *groups):
        super().__init__((Settings_Code_dec_31_2021.RED), pos, *groups)
        self.image = pygame.Surface((35, 32))#controls size of sprite
        self.image = Settings_Code_dec_31_2021.platform_b_img#chooses the player photo
        self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)#clears all of the black from the photo
        self.rect = self.image.get_rect(topleft=pos)#sets character position
        
class Lever(Player_block):#the lever function
    def __init__(self, *groups):
        super().__init__((Settings_Code_dec_31_2021.BLUE), *groups)
        self.image = pygame.Surface((35, 32))#lever size 
        self.image = Settings_Code_dec_31_2021.lever_red#lever photo
        self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)#clears all black from the photo
        self.rect = self.image.get_rect()
        self.rect.x = Settings_Code_dec_31_2021.Lever_1_xy[0]#checks the list for the position of x and y
        self.rect.y = Settings_Code_dec_31_2021.Lever_1_xy[1]
        
    def update(self):#levers update code
        if 'BLUE' in Settings_Code_dec_31_2021.Levers_color:#checks to see if this lever has been hit by thr player by looking for blu in the list
            self.image = Settings_Code_dec_31_2021.lever_green#changes the lever to look green and still ignore black
            self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        else:
            self.image = Settings_Code_dec_31_2021.lever_red#this stes everything back to normal looking incase anything goes wrong, shouldnt happen
            self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
            self.rect.x = Settings_Code_dec_31_2021.Lever_1_xy[0]
            self.rect.y = Settings_Code_dec_31_2021.Lever_1_xy[1]
class Lever_2(Player_block):#for information on this code please refer to the code above it
    def __init__(self, pos, *groups):
        super().__init__((Settings_Code_dec_31_2021.GREEN), pos, *groups)
        self.image = pygame.Surface((35, 32))
        self.image = Settings_Code_dec_31_2021.lever_red_rotate
        self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = Settings_Code_dec_31_2021.Lever_2_xy[0]
        self.rect.y = Settings_Code_dec_31_2021.Lever_2_xy[1]
    
    def update(self):
        if 'GREEN' in Settings_Code_dec_31_2021.Levers_color:
            self.image = Settings_Code_dec_31_2021.lever_green
            self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
        else:
            self.image = Settings_Code_dec_31_2021.lever_red
            self.image.set_colorkey(Settings_Code_dec_31_2021.BLACK)
            self.rect.x = Settings_Code_dec_31_2021.Lever_2_xy[0]
            self.rect.y = Settings_Code_dec_31_2021.Lever_2_xy[1]
            
# class Wall(Player_block):#this is all of the wall function
#     def __init__(self, pos, *groups):
#         super().__init__((RED), pos, *groups)
#         self.image = pygame.Surface((35, 32))# size of the wall
#         #self.image.fill(GREEN)#color of the wall
#         self.rect = self.image.get_rect(topleft=pos)
class ExitBlock(Player_block):
    def __init__(self, pos, *groups):#this is the exit block
        super().__init__(Color("#0033FF"), pos, *groups)
if __name__ == "__main__":#checks to make sure you are using this file and not just calling it
    running = True
    game_over = True
    Settings_Code_dec_31_2021.clock.tick(Settings_Code_dec_31_2021.FPS)
    try:#does this to mae sure nothing can go wrong with the file save function
        reading = open('Game_save.txt', 'r')#checks for the game ave file and will read it 
        working = reading.readlines()#makes all of the info into a list
        #the code below looks for the level you are on inside the working list, and will then play that level for you
        if "3" in working:
            Settings_Code_dec_31_2021.Level.append(3)
        if "2" in working:
            Settings_Code_dec_31_2021.Level.append(2)
        show_go_screen()#shows the start screen
        main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)#starts the main class
    except:
        show_go_screen()#starts the start screen
        main(Settings_Code_dec_31_2021.Levers_color, Settings_Code_dec_31_2021.bg, Settings_Code_dec_31_2021.time)#starts the main class
    for e in pygame.event.get():#chacks for the player leaving the game
        if e.type == pygame.QUIT:
            pygame.quit()
    pygame.quit()
