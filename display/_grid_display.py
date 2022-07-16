from typing import List, Tuple

import numpy as np
import pygame

from models.base_models import ObjectModel
from models.colors import Colors
from ._display import Display
from .special_render import SpecialRender


class GridDisplay(Display):
    def __init__(self, cell_size, rows, columns, fps=60):
        width = columns * cell_size
        height = rows * cell_size
        super().__init__(width, height, fps)
        self.cell_size = cell_size
        self.rows = rows
        self.columns = columns
        self.grid_size = (width, height)
        self.grid_color = (255, 255, 255)
        self.grid_line_color = (0, 0, 0)
        self.grid_line_width = 1
        self.celular_automata = None

    @staticmethod
    def darken_color(color: Tuple[int, int, int]):
        return tuple(color[i]//2 for i in range(3))

    @staticmethod
    def lighten_color(color: Tuple[int, int, int]):
        return tuple(color[i]*2 if color[i]*2 < 256 else 255 for i in range(3))

    def _render_rect_color(self, objct: ObjectModel, color: Tuple[int, int, int]):
        objct.color = color
        self.render_rect(objct)

    def render_rect(self, objct: ObjectModel):
        if objct.name == "player":
            SpecialRender(self.screen, self.cell_size).rainbow_rect(objct)
            return
        elif objct.name == "cell":
            pass

        x = objct.x * self.cell_size
        y = objct.y * self.cell_size

        color2 = self.darken_color(objct.color)
        rect1 = pygame.Rect(x, y, self.cell_size * .9, self.cell_size * .9)
        rect2 = pygame.Rect(x, y, self.cell_size * .6, self.cell_size * .6)
        rect2.center = rect1.center
        pygame.draw.rect(self.screen, objct.color, rect1)
        pygame.draw.rect(self.screen, color2, rect2)

    def render_grid(self):
        color1 = Colors.DARK_GREEN
        for x in range(0, self.width//self.cell_size):
            for y in range(0, self.height//self.cell_size):
                objct = ObjectModel(
                    name="grid",
                    x=x,
                    y=y,
                    width=self.cell_size,
                    height=self.cell_size,
                    color=color1,
                )
                self.render_rect(objct)
                # SpecialRender(self.screen, self.cell_size).render_t(objct)

    def render_celular_automata(self):
        if self.celular_automata is None:
            print(f"{self.__class__.__name__} celular_automata is None")
            self.celular_automata = np.zeros((self.rows, self.columns))

            # create random live cells
            for _ in range(65):
                x = np.random.randint(0, self.columns)
                y = np.random.randint(0, self.rows)
                self.celular_automata[x, y] = 1
            self.celular_automata = self.celular_automata

        cell_value = 0
        next_generation = self.celular_automata.copy()
        for x in range(0, self.width//self.cell_size):
            for y in range(0, self.height//self.cell_size):
                cell_value = self.celular_automata[x, y]

                    # count the number of neighbors
                if True:
                    neighbors = self.celular_automata[x - 1: x + 2, y - 1: y + 2].sum() - self.celular_automata[x, y]
                    # apply the rules of the game
                    if self.celular_automata[x, y] == 1:
                        if neighbors < 2 or neighbors > 3:
                            cell_value = 0
                            next_generation[x, y] = 0
                    else:
                        if neighbors == 3:
                            cell_value = 1
                            next_generation[x, y] = 1

                if cell_value == 0:
                    continue
                rainbow = SpecialRender(self.screen, self.cell_size).rainbow_color_from_x_y(x, y)
                objct = ObjectModel(
                    name="cell",
                    x=x,
                    y=y,
                    width=self.cell_size,
                    height=self.cell_size,
                    color=rainbow if cell_value else Colors.BLACK,
                )
                self.render_rect(objct)

                # SpecialRender(self.screen, self.cell_size).render_t(objct)
                self.celular_automata = next_generation

    def _render(self):
        # self._render_grid()
        self.render_celular_automata()
        pass

    def render_objets(self, objcts: List[ObjectModel]):
        if not objcts:
            return

        for objct in objcts:
            self.render_rect(objct)


