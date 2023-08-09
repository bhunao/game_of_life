from typing import List, Tuple

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
            #objct.color = Colors.rainbow_color_from_x_y(self.screen.get_size(), self.cell_size, objct.x)
            pass
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

    def _render(self):
        # self._render_grid()
        pass

    def render_objets(self, objcts: List[ObjectModel]):
        if not objcts:
            return

        for objct in objcts:
            self.render_rect(objct)


