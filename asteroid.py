import pygame
import random
from constants import *
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
   
        direction1 = self.velocity.rotate(random_angle) * 1.2
        direction2 = self.velocity.rotate(-random_angle) * 1.2
    
        for direction in [direction1, direction2]:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = direction
            self.containers[0].add(new_asteroid)