import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():

    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock to track time
    clock = pygame.time.Clock()

    # Initialize delta
    dt = 0
    
    # Creates two groups, updatables and drawables
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    # Set these groups as containers for the classes
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots,)

    # Create an instance of the player class after setting the containers
    # This makes sure they are automatically added to both groups
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    # Game loop, each iteration is one frame of the game
    running = True
    while running:
       
        # Checking for event to quit the game, if the event == quit, break loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Fill the screen with black to clear previous frame
        screen.fill("black")

        # Updates all objects in the updatables group with the time delta
        updatables.update(dt)

        # For each drawable in drawables, draw it to the screen
        for drawable in drawables:
            drawable.draw(screen)

        # Iterate over asteroid objects to check for collisions
        for asteroid in asteroids:
            if(asteroid.collision_check(player)):
                print("Game over!")
                sys.exit()

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        # Display everything and calculate the time delta for the next frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    pygame.quit()

if __name__ == "__main__":
    main()
