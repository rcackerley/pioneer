import pygame
from pygame.locals import * 
import random

class Hero():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def render(self, screen):
        hero_image = pygame.image.load('images/Vikings/Viking3/Stand/0.png').convert_alpha()
        scaled_hero = pygame.transform.scale(hero_image, (75, 75))
        screen.blit(scaled_hero, (self.x, self.y))

class Texture(Rect):
    def __init__(self, image, id):
        self.image = image
        self.id = id
        self.x = 0
        self.y = 0

class item(Rect):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
    def render(self, screen):
        log_item = pygame.image.load('images/textures/log.png').convert_alpha()
        screen.blit(log_item, (self.x, self.y))

def main():
    width = 15
    height = 15
    TILESIZE = 40

    dirt = Texture(pygame.image.load('images/textures/dirt.jpg'), 0)
    grass = Texture(pygame.image.load('images/textures/grass.jpg'), 1)
    water = Texture(pygame.image.load('images/textures/water.jpg'), 2)
    snow = Texture(pygame.image.load('images/textures/snow.jpg'), 3)
    sand = Texture(pygame.image.load('images/textures/sand.jpg'), 4)
    mountain = Texture(pygame.image.load('images/textures/mountain.jpg'), 5)
    
    
    
    tilemap = [
        [mountain.image,mountain.image,water.image,water.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image],
        [mountain.image,mountain.image,water.image,water.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image,mountain.image],
        [snow.image,snow.image,water.image,water.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image],
        [snow.image,snow.image,water.image,water.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image],
        [snow.image,snow.image,water.image,water.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image,snow.image],
        [water.image,water.image,water.image,water.image,grass.image,grass.image,grass.image,snow.image,mountain.image,mountain.image,mountain.image,snow.image,grass.image,grass.image,grass.image],
        [water.image,water.image,water.image,water.image,grass.image,grass.image,grass.image,snow.image,mountain.image,mountain.image,mountain.image,snow.image,grass.image,grass.image,grass.image],
        [water.image,sand.image,sand.image,water.image,grass.image,grass.image,grass.image,grass.image,snow.image,snow.image,snow.image,snow.image,snow.image,grass.image,grass.image],
        [water.image,water.image,water.image,water.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image],
        [water.image,water.image,water.image,water.image,grass.image,grass.image,grass.image,grass.image,water.image,water.image,sand.image,grass.image,grass.image,dirt.image,dirt.image],
        [water.image,water.image,water.image,water.image,grass.image,grass.image,grass.image,grass.image,water.image,water.image,sand.image,grass.image,grass.image,grass.image,grass.image],
        [sand.image,sand.image,sand.image,sand.image,sand.image,grass.image,dirt.image,grass.image,grass.image,water.image,sand.image,sand.image,grass.image,grass.image,grass.image],
        [sand.image,sand.image,sand.image,sand.image,sand.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image],
        [dirt.image,dirt.image,dirt.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image],
        [dirt.image,dirt.image,dirt.image,grass.image,grass.image,grass.image,grass.image,grass.image,dirt.image,grass.image,grass.image,grass.image,grass.image,grass.image,grass.image],
    ]
    
    BLACK = (0, 0, 0)

    pygame.init()
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 15)
    label = font_renderer.render('INVENTORY', 1, (255, 255,255))
    screen = pygame.display.set_mode((width * TILESIZE, height * TILESIZE + 65))
    pygame.display.set_caption('Pioneer')
    clock = pygame.time.Clock()

    # for rw in range(height):
    #     for cl in range(width):
    #         randomNumber = random.randint(0,15)
    #         if randomNumber == 0:
    #             tile = MOUNTAIN
    #         elif randomNumber == 1 or randomNumber == 2:
    #             tile = WATER
    #         elif randomNumber >= 3 and randomNumber <= 7:
    #             tile = GRASS
    #         elif randomNumber == 8 or randomNumber == 9:
    #             tile = DIRT
    #         elif randomNumber >= 10 or randomNumber <= 13:
    #             tile = SNOW
    #         else:
    #             tile = SAND
    #         tilemap[rw][cl] = tile

    # Game initialization
    hero = Hero(100, 500)
    hero_rect = Rect(100,500, 75,75)
    log = item(300,175) 
    log2 = item(245,455) 
    log3 = item(400,150)
    log4 = item(185,400)
    log5 = item(300,440)
    log_icon = item(width * TILESIZE - 450,height * TILESIZE + 20)
    rect_x = 0
    rect_y = 0

    stop_game = False

    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
            
            #### Hero Movement
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.speed_x = -3
                    rect_x = -3
                    print hero.x, hero.y
                    print hero_rect.x, hero_rect.y
                    
                    for hill in mountains:
                        if hero_rect.colliderect(hill):
                            hero.speed_x = 1
                            rect_x = 1
                            print 'collision'
                            print hill.x
                            print hill.y
                            print hero.x, hero.y
                            print hero_rect.x, hero_rect.y
                            break
                    for watery in waters:
                        if hero_rect.colliderect(watery):
                            hero.speed_x = 1
                            rect_x = 1
                            break
                    
                        
                elif event.key == pygame.K_RIGHT:
                    hero.speed_x = 3
                    rect_x = 3
                    for hill in mountains:
                        if hero_rect.colliderect(hill):
                            hero.speed_x = -1
                            rect_x = -1
                            print 'collision'
                            break
                    for watery in waters:
                        if hero_rect.colliderect(watery):
                            hero.speed_x = -1
                            rect_x = -1
                            break

                elif event.key == pygame.K_UP:
                    hero.speed_y = -3
                    rect_y = -3
                    for hill in mountains:
                        if hero_rect.colliderect(hill):
                            hero.speed_y = 1
                            rect_y = 1
                            print 'collision'
                            break
                    for watery in waters:
                        if hero_rect.colliderect(watery):
                            hero.speed_y = 1
                            rect_y = 1
                            break

                elif event.key == pygame.K_DOWN:
                    hero.speed_y = 3
                    rect_y = 3
                    for hill in mountains:
                        if hero_rect.colliderect(hill):
                            hero.speed_y = -1
                            rect_y = -1
                            print 'collision'
                            break
                    for watery in waters:
                        if hero_rect.colliderect(watery):
                            hero.speed_y = -1
                            rect_y = -1
                            break
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    hero.speed_x = 0
                    rect_x = 0
                elif event.key == pygame.K_RIGHT:
                    hero.speed_x = 0
                    rect_x = 0
                elif event.key == pygame.K_UP:
                    hero.speed_y = 0
                    rect_y = 0
                elif event.key == pygame.K_DOWN:
                    hero.speed_y = 0
                    rect_y = 0
            #################

        # Game logic
        hero.update()
        hero_rect.x += rect_x
        hero_rect.y += rect_y
        # Draw background
        screen.fill(BLACK)
        #loop through each row
        mountains = []
        waters = []
        for row in range(height):
            for column in range(width):
                screen.blit(tilemap[row][column], (column*TILESIZE,row*TILESIZE))
                if tilemap[row][column] == mountain.image:
                    mountains.append(Rect(column * TILESIZE, row * TILESIZE, 40, 40))
                elif tilemap[row][column] == water.image:
                    waters.append(Rect(column * TILESIZE, row * TILESIZE, 40, 40))
                    
        screen.blit(label, (width * TILESIZE - 575,height * TILESIZE + 28))
        
        # Game display
        if hero_rect.colliderect(log):
            log.collected = True
            print 'collected'
            log.x = width * TILESIZE - 450
            log.y = height * TILESIZE + 10
        if hero_rect.colliderect(log2):
            log2.collected = True
            print 'collected'
            log2.x = width * TILESIZE - 400
            log2.y = height * TILESIZE + 10
        if hero_rect.colliderect(log3):
            log3.collected = True
            print 'collected'
            log3.x = width * TILESIZE - 350
            log3.y = height * TILESIZE + 10
        if hero_rect.colliderect(log4):
            log4.collected = True
            print 'collected'
            log4.x = width * TILESIZE - 300
            log4.y = height * TILESIZE + 10
        if hero_rect.colliderect(log5):
            log5.collected = True
            print 'collected'
            log5.x = width * TILESIZE - 250
            log5.y = height * TILESIZE + 10
        
        log.render(screen)
        log2.render(screen)
        log3.render(screen)
        log4.render(screen)
        log5.render(screen)
        hero.render(screen)
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()
