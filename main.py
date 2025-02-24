import pygame # Import the pygame library to allow us access to its code
from constants import * # Import for access to constants

def main():
    pygame.init() # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the screen
    while True:
        screen.fill((0, 0, 0)) # Fill the screen with a color
        for event in pygame.event.get(): # Get all the events that have happened
            if event.type == pygame.QUIT: # If the event is a quit event, then quit the game
                return # Exit the game
        pygame.display.flip() # Update the display
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main() # Call the main when program starts