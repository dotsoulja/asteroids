import pygame # Import the pygame library to allow us access to its code
from constants import * # Import for access to constants
from player import Player # Import the player class from player


def main():
    pygame.init() # Initialize the pygame library
    clock = pygame.time.Clock() # Create a clock object to control the frame rate
    dt = 0 # Set the delta time to 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create the player object
    while True:
        screen.fill((0, 0, 0)) # Fill the screen with a color

        for event in pygame.event.get(): # Get all the events that have happened
            if event.type == pygame.QUIT: # If the event is a quit event, then quit the game
                return # Exit the game
        player.draw(screen) # Draw the player
        pygame.display.flip() # Update the display
        clock.tick(60) # Set the frame rate to 60 frames per second
        dt = clock.tick(60) / 1000.0 # Set the delta time to the time since the last frame in seconds
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main() # Call the main when program starts