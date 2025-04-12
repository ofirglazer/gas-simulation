import pygame
from gas_model import Volume
from gas_view import Volume_renderer

def main(num_particles=1, gravity=1, width=400, height=200, radius=10):

    model = Volume(num_particles, gravity, width, height, radius=radius)
    viewer = Volume_renderer(width, height)

    pygame.init()
    FPS = 20
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        model.update()
        viewer.render(model)
        clock.tick(FPS)


if __name__ == '__main__':
    num_particles = 20
    gravity = 0
    width = 600
    height = 400
    radius = 10
    main(num_particles=num_particles, width=width, height=height, gravity=gravity, radius=radius)
