# FRAMEWORK
# Create class for simulation environment
#  [ ] Initialize - Height, Width (with assumed zero padding)
#  [ ] Attributes - Count of alive neighbors, current status (0, 1)
#  [ ] Methods - Seed Environment, Check Condition, Update Step


# RULES
#  [ ] Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#  [ ] Any live cell with two or three live neighbours lives on to the next generation.
#  [ ] Any live cell with more than three live neighbours dies, as if by overpopulation.
#  [ ] Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
#  [ ] Any live cell with two or three live neighbours survives.
#  [ ] Any dead cell with three live neighbours becomes a live cell.
#  [ ] All other live cells die in the next generation. Similarly, all other dead cells stay dead.

import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation


class Conway:
    def __init__(self, size, seed_pct):
        self.size = size
        self.seed_pct = seed_pct

    def seed_env(self):
        env = random(self.size ** 2)
        env = env < self.seed_pct
        env = np.reshape(env, (self.size, self.size))
        self.env = env.astype('int')

    def step_frame(self):
        for i in range(self.size):
            for j in range(self.size):
                cell_state = self.env[i, j]
                i_start = i - 1
                j_start = j - 1
                i_end = i + 2
                j_end = j + 2
                if i_start < 0:
                    i_start = 0
                if j_start < 0:
                    j_start = 0
                if i_end < 0:
                    i_end = 0
                if j_end < 0:
                    j_end = 0
                region = self.env[i_start:i_end, j_start:j_end]
                alive_neighbors = region.sum() - cell_state
                if (cell_state == 1) & (alive_neighbors in [2, 3]):
                    self.env[i, j] = 1
                elif (cell_state == 0) & (alive_neighbors == 3):
                    self.env[i, j] = 1
                else:
                    self.env[i, j] = 0

    def simulate(self, steps=100):
        i = 0
        while i < steps:
            self.step_frame()
            i += 1

