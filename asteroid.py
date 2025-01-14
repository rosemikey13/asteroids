from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, new_size)
        smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, new_size)
        smaller_asteroid_1.velocity = vector1 * 1.2
        smaller_asteroid_2.velocity = vector2 * 1.2
