from circleshape import *
from main import *
from particleeffects import *
import random

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
            self.boom(0)
            return
        else:
            angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.boom(angle)
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = velocity_1 * 1.2
            asteroid_2.velocity = velocity_2 * 1.2

    
    def boom(self, angle):
        particle_1 = Particle(self.position.x, self.position.y)
        particle_2 = Particle(self.position.x, self.position.y)
        particle_3 = Particle(self.position.x, self.position.y)
        particle_4 = Particle(self.position.x, self.position.y)
        particle_5 = Particle(self.position.x, self.position.y)
        particle_6 = Particle(self.position.x, self.position.y)
        particle_1.velocity = self.velocity.rotate(angle + 30) * 2.6
        particle_2.velocity = self.velocity.rotate(angle + 90) * 2.6
        particle_3.velocity = self.velocity.rotate(angle + 150) * 2.6
        particle_4.velocity = self.velocity.rotate(angle + 210) * 2.6
        particle_5.velocity = self.velocity.rotate(angle + 270) * 2.6
        particle_6.velocity = self.velocity.rotate(angle + 330) * 2.6