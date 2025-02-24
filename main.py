import pygame # Import the pygame library to allow us access to its code
from constants import * # Import for access to constants
from player import * # Import the player class


def main():
    #introduction to game
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init() # Initialize the pygame library
    clock = pygame.time.Clock() # Create a clock object to control the frame rate
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create the player object
    
    while True:
        dt = clock.tick(60) / 1000 # Set the delta time to 0

        for event in pygame.event.get(): # Get all the events that have happened
            if event.type == pygame.QUIT: # If the event is a quit event, then quit the game
                return # Exit the game
        
        player.update(dt) # Update the player
        screen.fill((0, 0, 0)) # Fill the screen with a color
        
        player.draw(screen) # Draw the player
        pygame.display.flip() # Update the display
        
if __name__ == "__main__":
    main() # Call the main when program starts