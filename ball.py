import pygame

class Ball:
    def __init__(self, x, y, radius, color, vel):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = vel

    def move(self):
        self.x += self.vel[0]
        self.y += self.vel[1]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)