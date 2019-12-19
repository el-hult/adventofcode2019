from day12_lib import *

from util import *

f = read_file('inputs/day12.txt')

particles = parse_particles(f)
print(particles)

for _ in range(1000):
    apply_gravity(particles)
    travel_with_velocity(particles)

print(get_energy(particles)) # 13399 is right!

ps = parse_particles(f)
print(better_recurrence_check(ps)) # 312992287193064 is right