import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape): # Player class inherits from CircleShape
    def __init__(self, x, y): # Constructor 
        super().__init__(x, y, PLAYER_RADIUS) # Call the constructor of the parent class
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # Get the forward vector
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5 # Get the right vector
        a = self.position + forward * self.radius # Get the position of the player
        b = self.position - forward * self.radius - right # Get the position of the player
        c = self.position - forward * self.radius + right # Get the position of the player
        return [a, b, c] # Return the triangle
    
    def draw(self, screen): # Draw the player
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2) # Draw the player as a white triangle with a width of 2

