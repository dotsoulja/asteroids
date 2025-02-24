import sys
import pygame # Import the pygame library to allow us access to its code
from constants import * # Import for access to constants
from circleshape import * # Import the circleshape class
from player import Player # Import the player class
from asteroid import * # Import the asteroid class
from asteroidfield import * # Import the asteroidfield class
from shot import Shot # Import the shot class
import game_over
def main():
    #introduction to game
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init() # Initialize the pygame library
    clock = pygame.time.Clock() # Create a clock object to control the frame rate
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the screen
    
    updatable = pygame.sprite.Group() # Create a group for all the updatable objects
    drawable = pygame.sprite.Group() # Create a group for all the drawable objects
    asteroids = pygame.sprite.Group() # Create a group for all the asteroids
    shot_group = pygame.sprite.Group() # Create a group for all the shots
    #this is for optional game over text on screen
    game_over_text, game_over_rect = game_over.init_game_over_text(SCREEN_WIDTH, SCREEN_HEIGHT)


    Player.containers = (updatable, drawable) # Set the containers for the player
    Asteroid.containers = (asteroids, updatable, drawable) # Set the containers for the asteroid
    AsteroidField.containers = updatable # Set the containers for the asteroid field
    Shot.containers = (shot_group, updatable, drawable) # Set the containers for the shot

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create the player object
    asteroid_field = AsteroidField() # Create the asteroid field object


    while True:
        dt = clock.tick(60) / 1000 # Set the delta time to 0

        for event in pygame.event.get(): # Get all the events that have happened
            if event.type == pygame.QUIT: # If the event is a quit event, then quit the game
                return # Exit the game
        
        updatable.update(dt) # Update all the updatable objects
        
        for asteroid in asteroids: # For each asteroid
            if player.collides_with(asteroid): #if the player collides with the asteroid
                print("Game over")
                game_over.show_game_over(screen, game_over_text, game_over_rect) #show game over text
                pygame.quit() #quit the game
                sys.exit() #exit the game
        
        for asteroid in asteroids: #iterates over the asteroids group
            for shot in shot_group: #iterates over the shot group
                if asteroid.collides_with(shot): #if the asteroid collides with the shot
                    asteroid.kill() #kill the asteroid
                    shot.kill() #kill the shot
                    break #break the loop
                

        screen.fill((0, 0, 0)) # Fill the screen with a color
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip() # Update the display
        
if __name__ == "__main__":
    main() # Call the main when program starts