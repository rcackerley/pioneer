import pygame
from pygame.locals import * 
import random

class Hero():
    def __init__(self, x, y):
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

class Texture():
    def __init__(self, image, id):
        self.image = image
        self.id = id


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
    
    # DIRT = 0
    # GRASS = 1
    # WATER = 2
    # SNOW = 3 
    # SAND = 4
    # MOUNTAIN = 5
    # tiles = [DIRT, GRASS, WATER, SNOW, SAND, MOUNTAIN]

    # tilemap = [
    #     [DIRT for w in range(width)] for h in range(height)
    # ]
    
    
    # tilemap = [
    #     [snow.image, mountain.image],[dirt.image, snow.image]
    # ]
    
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

    # textures = {
    #     DIRT: pygame.transform.scale(pygame.image.load('images/textures/dirt.jpg'), (60,60)),
    #     GRASS: pygame.transform.scale(pygame.image.load('images/textures/grass.jpg'), (60,60)),
    #     WATER: pygame.transform.scale(pygame.image.load('images/textures/water.jpg'), (60,60)),
    #     SNOW: pygame.transform.scale(pygame.image.load('images/textures/snow.jpg'), (60,60)),
    #     MOUNTAIN: pygame.image.load('images/textures/mountain.jpg'),
    #     SAND: pygame.transform.scale(pygame.image.load('images/textures/sand.jpg'), (60,60)),
    # }

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
    hero = Hero(250, 250)
    stop_game = False

    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
            
            #### Hero Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    hero.speed_x = 5
                elif event.key == pygame.K_UP:
                    hero.speed_y = -5
                elif event.key == pygame.K_DOWN:
                    hero.speed_y = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    hero.speed_x = 0
                elif event.key == pygame.K_RIGHT:
                    hero.speed_x = 0
                elif event.key == pygame.K_UP:
                    hero.speed_y = 0
                elif event.key == pygame.K_DOWN:
                    hero.speed_y = 0
            #################

        # Game logic
        hero.update()

        # Draw background
        screen.fill(BLACK)
        #loop through each row
        for row in range(height):
            for column in range(width):
                screen.blit(tilemap[row][column], (column*TILESIZE,row*TILESIZE))
        
        screen.blit(label, (width * TILESIZE - 100,height * TILESIZE + 35))
        # Game display
        hero.render(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
