from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (200, 200, 200), 
            (int(self.position.x), int(self.position.y)), 
            self.radius,
            LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt