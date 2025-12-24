from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (200, 200, 200), 
            (int(self.position.x), int(self.position.y)), 
            self.radius,
            LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        # Wrap around screen edges (assuming SCREEN_WIDTH and SCREEN_HEIGHT are defined)
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT