import random
from typing import List

import numpy as np

from display import Display
from models.base_models import ObjectModel, Sprite
from models.colors import Colors


def self_avoiding_walk(game_cls, game_event, objct: ObjectModel, config: dict):
    for propertie in objct.addittional_properties:
        pass

def game_of_life(display: Display, game_event, config: dict) -> List[ObjectModel]:
    # inner function to give 2d array of 0s and 1s
    def create_grid(grid_size):
        return np.zeros(grid_size)

    # inner function to give random starting point
    def random_starting_point(grid_size):
        return random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)

    grid_size = 25, 25
    grid = create_grid(grid_size)
    next_generation = grid.copy()

    for _ in range(25):
        rand_pos = random_starting_point(grid_size)
        grid[rand_pos] = 1

    # iterate over all grid elements
    cell_value = 0
    cells = []
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # count the number of neighbors
            neighbors = grid[i - 1: i + 2, j - 1: j + 2].sum() - grid[i, j]
            # apply the rules of the game
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    cell_value = 0
                    next_generation[i, j] = 0
            else:
                if neighbors == 3:
                    cell_value = 1
                    next_generation[i, j] = 1

            objct = ObjectModel(
                name="cell",
                x=i,
                y=j,
                width=25,
                height=25,
                color=Colors.LIGHT_RED if cell_value == 1 else Colors.LIGHT_BLUE
            )
            cells.append(objct)

    return cells
