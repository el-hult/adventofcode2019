import dataclasses
import itertools
import math
from dataclasses import dataclass
from typing import List


@dataclass
class ParticleState:
    x: int
    y: int
    z: int
    velx: int
    vely: int
    velz: int

    def __str__(self):
        return f"pos=<x={self.x:3d}, y={self.y:3d}, z={self.z:3d}>, vel=<x={self.velx:3d}, y={self.vely:3d}, z={self.velz:3d}>"


def apply_gravity(ps: List[ParticleState]):
    for p1, p2 in itertools.combinations(ps, 2):
        # calculate the pull on p1
        diffx = my_sign(p2.x - p1.x)
        diffy = my_sign(p2.y - p1.y)
        diffz = my_sign(p2.z - p1.z)
        p1.velx += diffx
        p1.vely += diffy
        p1.velz += diffz
        p2.velx -= diffx
        p2.vely -= diffy
        p2.velz -= diffz


def travel_with_velocity(ps: List[ParticleState]):
    for p in ps:
        p.x += p.velx
        p.y += p.vely
        p.z += p.velz


def get_energy(ps: List[ParticleState]):
    tot_energy = 0
    for p in ps:
        potential_energy = abs(p.x) + abs(p.y) + abs(p.z)
        kinetic_energy = abs(p.velx) + abs(p.vely) + abs(p.velz)
        particle_energy = potential_energy* kinetic_energy
        tot_energy += particle_energy
    return  tot_energy


def my_sign(i: int) -> int:
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0


def parse_particles(f:str):
    particles = []
    for l in f.splitlines():
        xyz = map(lambda s: int(s[2:]), l[1:-1].split(", "))
        initial_state = ParticleState(*xyz, 0, 0, 0)
        particles.append(initial_state)
    return particles


def ps_to_str(ps: List[ParticleState]):
    s = str(ps[0])
    for p in ps[1:]:
        s += "\n" + str(p)
    return s


def naive_recurrence_check(ps):
    """A stupid implementation that works for 10 seconds roughly"""
    k = 200_000
    old_states = set(tuple(dataclasses.astuple(p) for p in ps))
    for i in range(k):
        apply_gravity(ps)
        travel_with_velocity(ps)
        tup = tuple(dataclasses.astuple(p) for p in ps)
        if tup in old_states:
            return i
        else:
            old_states.add(tup)
    raise ValueError(f"No loop found within {k} iterations")


def better_recurrence_check(ps):
    """A stupid implementation that works for 10 seconds roughly"""
    k = 1_000_000
    old_x_states = set()
    old_y_states = set()
    old_z_states = set()
    old_x_states.add(tuple(((p.x, p.velx) for p in ps), ))
    old_y_states.add(tuple(((p.y, p.vely) for p in ps), ))
    old_z_states.add(tuple(((p.z, p.velz) for p in ps), ))
    x_cycle_length = None
    y_cycle_length = None
    z_cycle_length = None
    for i in range(1,k+1):
        apply_gravity(ps)
        travel_with_velocity(ps)
        x_tup = tuple((p.x, p.velx) for p in ps)
        y_tup = tuple((p.y, p.vely) for p in ps)
        z_tup = tuple((p.z, p.velz) for p in ps)

        if x_cycle_length is not None:
            pass
        elif x_tup in old_x_states:
            x_cycle_length = i
        elif x_cycle_length not in old_x_states:
            old_x_states.add(x_tup)
        if y_cycle_length is not None:
            pass
        elif y_tup in old_y_states:
            y_cycle_length = i
        elif y_cycle_length not in old_y_states:
            old_y_states.add(y_tup)
        if z_cycle_length is not None:
            pass
        elif z_tup in old_z_states:
            z_cycle_length = i
        elif z_cycle_length not in old_z_states:
            old_z_states.add(x_tup)

        if all([x_cycle_length, y_cycle_length, z_cycle_length]):
            lcm = lambda a, b: a * b // math.gcd(a, b)
            return lcm(x_cycle_length, lcm(y_cycle_length, z_cycle_length))

    raise ValueError(f"No loop found within {k} iterations")