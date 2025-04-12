from random import randrange
import numpy as np


class Particle:

    def __init__(self, position=(0,0), velocity=(0,0), radius=2):
        self.pos_x = float(position[0])
        self.pos_y = float(position[1])
        self.vel_x = float(velocity[0])
        self.vel_y = float(velocity[1])
        self.radius = radius

    def update(self, gravity):
        self.vel_y -= gravity
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def __str__(self):
        return f"Particle in position {(self.pos_x, self.pos_y)} with velocity {(self.vel_x, self.vel_y)}"

class Volume:

    def __init__(self, num_particles=1, gravity=0, width=100, height=100, max_init_velocity = 50, radius=10):
        self.particles = []
        self.gravity = gravity
        self.width = width
        self.height = height
        self.radius = radius

        for particle in range(num_particles):
            pos_x = randrange(radius, self.width - radius)
            pos_y = randrange(radius, self.height - radius)
            vel_x = randrange(max_init_velocity)
            vel_y = randrange(max_init_velocity)
            self.particles.append(Particle((pos_x, pos_y), (vel_x, vel_y), self.radius))

    def update(self):
        for particle in self.particles:
            particle.update(self.gravity)
            self.collide_borders(particle)
        self.collide_particles()

    def collide_particles(self):
        for idx, particle1 in enumerate(self.particles):
            for particle2 in self.particles[idx + 1:]:
                vel1, vel2 = self.elastic_collision_equal_mass_2d(particle1, particle2)
                particle1.vel_x, particle1.vel_y = float(vel1[0]), float(vel1[1])
                particle2.vel_x, particle2.vel_y = float(vel2[0]), float(vel2[1])
                pass


    def elastic_collision_equal_mass_2d(self, particle1, particle2):
        # Convert to numpy arrays
        posA = np.array((particle1.pos_x, particle1.pos_y), dtype=float)
        velA = np.array((particle1.vel_x, particle1.vel_y), dtype=float)
        posB = np.array((particle2.pos_x, particle2.pos_y), dtype=float)
        velB = np.array((particle2.vel_x, particle2.vel_y), dtype=float)

        # Relative position and velocity
        r = posB - posA
        r_norm = np.linalg.norm(r)
        if r_norm >= particle1.radius + particle2.radius:
            return velA, velB  # no collision
        if r_norm == 0:
            return velA, velB  # avoid divide by zero (overlapping particles)

        # Unit normal vector (collision axis)
        n = r / r_norm

        # Velocity components along the normal
        vA_n = np.dot(velA, n)
        vB_n = np.dot(velB, n)

        # Swap normal components
        velA_new = velA + (vB_n - vA_n) * n
        velB_new = velB + (vA_n - vB_n) * n

        return velA_new, velB_new


























    def collide_borders(self, particle):
        margin_x_left = particle.pos_x - particle.radius
        margin_x_right = self.width - particle.pos_x - particle.radius
        margin_y_down = particle.pos_y - particle.radius
        margin_y_up = self.height - particle.pos_y - particle.radius

        if margin_x_left < 0:
            particle.pos_x = particle.radius - margin_x_left
            particle.vel_x = -particle.vel_x
        elif margin_x_right < 0:
            particle.pos_x = self.width - particle.radius - margin_x_right
            particle.vel_x = -particle.vel_x

        if margin_y_down < 0:
            particle.pos_y = particle.radius - margin_y_down
            particle.vel_y = -particle.vel_y
        elif margin_y_up < 0:
            particle.pos_y = self.height - particle.radius - margin_y_up
            particle.vel_y = -particle.vel_y

    def __str__(self):
        str = ""
        for particle in self.particles:
            str += f"{particle}"
        return str


if __name__ == '__main__':
    num_particles = 3
    gravity = 1
    num_steps = 4
    volume = Volume(num_particles, gravity)

    for _ in range(num_steps):
        volume.update()
        print(volume)
