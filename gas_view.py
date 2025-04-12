import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Volume_renderer:

    def __init__(self, width=600, height=600):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Gas Particle Sim")

    def draw_particle(self, particle):
        pygame.draw.circle(self.window, WHITE, (particle.pos_x, particle.pos_y), particle.radius)

    def render(self, volume):
        self.window.fill(BLACK)

        for particle in volume.particles:
            self.draw_particle(particle)

        pygame.display.flip()
