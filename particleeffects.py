from circleshape import *
from constants import *
from asteroid import *


class Particle(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.kill_time = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.kill_time += dt
        if self.kill_time >= PARTICLE_EFFECT_LENGTH:
            self.kill()

