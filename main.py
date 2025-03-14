import pygame
from constants import *
from player import Player

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

    # Set these groups as containers for the player class
    Player.containers = (updatables, drawables)

    # Create an instance of the player class after setting the containers
    # This makes sure they are automatically added to both groups
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    # Game loop, each iteration is one frame of the game
    running = True
    while running:
       
        # Checking for event to quit the game, if the event == quit, break loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Fill the screen with black to clear previous frame
        screen.fill((0, 0, 0))

        # Updates all objects in the updatables group with the time delta
        updatables.update(dt)

        # For each drawable in drawables, draw it to the screen
        for drawable in drawables:
            drawable.draw(screen)

        # Display everything and calculate the time delta for the next frame
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    pygame.quit()

if __name__ == "__main__":
    main()
