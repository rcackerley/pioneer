import pygame

class Hero(object):
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
        
    
def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

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
        screen.fill(blue_color)

        # Game display
        hero.render(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
