import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *

class Player(CircleShape): # Player class inherits from CircleShape
    def __init__(self, x, y): # Constructor 
        super().__init__(x, y, PLAYER_RADIUS) # Call the constructor of the parent class
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # Get the forward vector
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5 # Get the right vector
        a = self.position + forward * self.radius # Get the position of the player
        b = self.position - forward * self.radius - right # Get the position of the player
        c = self.position - forward * self.radius + right # Get the position of the player
        return [a, b, c] # Return the triangle
    
    def draw(self, screen): # Draw the player
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2) # Draw the player as a white triangle with a width of 2

    def rotate(self, dt):       
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            position = self.position + forward * self.radius
            velocity = forward * PLAYER_SHOOT_SPEED 
        
            shot = Shot(position.x, position.y, SHOT_RADIUS)
            shot.velocity = velocity

            self.timer = PLAYER_SHOOT_COOLDOWN

        
        
    def update(self, dt): # Update the player
        self.timer -= dt
        keys = pygame.key.get_pressed() # Get the keys that are pressed
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # If the key is a
            self.rotate(-dt) # Rotate the player to the left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt) # Rotate the player to the right
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()