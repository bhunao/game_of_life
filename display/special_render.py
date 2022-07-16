from itertools import chain
from typing import Tuple

import pygame

from models.base_models import ObjectModel

offset = 0


class SpecialRender:
    def __init__(self, screen, cell_size):
        self.cell_size = cell_size
        self.screen = screen

    def lightnen_color(self, color: Tuple[int, int, int]):
        return tuple(color[i]*1.5 % 255 for i in range(3))

    def render_curve(self, objct: ObjectModel):
        x = objct.x * self.cell_size
        y = objct.y * self.cell_size
        color2 = self.lightnen_color(objct.color)
        rect1 = pygame.Rect(x, y, self.cell_size * .9, self.cell_size * .9)
        rect2 = pygame.Rect(x, y, self.cell_size * .5, self.cell_size * .7)
        rect3 = pygame.Rect(x, y, self.cell_size * .7, self.cell_size * .5)
        rect2.center = rect1.center[0], rect2.center[1]
        rect3.center = rect3.center[0], rect1.center[1]
        pygame.draw.rect(self.screen, objct.color, rect1)
        pygame.draw.rect(self.screen, color2, rect2)
        pygame.draw.rect(self.screen, color2, rect3)

    def render_cross(self, objct: ObjectModel):
        x = objct.x * self.cell_size
        y = objct.y * self.cell_size
        color2 = self.lightnen_color(objct.color)
        rect1 = pygame.Rect(x, y, self.cell_size * .9, self.cell_size * .9)
        rect2 = pygame.Rect(x, y, self.cell_size * .5, self.cell_size * 1)
        rect3 = pygame.Rect(x, y, self.cell_size * 1, self.cell_size * .5)
        rect2.center = rect1.center[0], rect2.center[1]
        rect3.center = rect3.center[0], rect1.center[1]
        pygame.draw.rect(self.screen, objct.color, rect1)
        pygame.draw.rect(self.screen, color2, rect2)
        pygame.draw.rect(self.screen, color2, rect3)

    def render_t(self, objct: ObjectModel):
        x = objct.x * self.cell_size
        y = objct.y * self.cell_size
        color2 = self.lightnen_color(objct.color)
        rect1 = pygame.Rect(x, y, self.cell_size * .9, self.cell_size * .9)
        rect2 = pygame.Rect(x, y, self.cell_size * .5, self.cell_size * .5)
        rect3 = pygame.Rect(x, y, self.cell_size * 1, self.cell_size * .5)
        rect2.center = rect1.center[0], rect2.center[1]
        rect3.center = rect3.center[0], rect1.center[1]
        pygame.draw.rect(self.screen, objct.color, rect1)
        pygame.draw.rect(self.screen, color2, rect2)
        pygame.draw.rect(self.screen, color2, rect3)
        rotate = pygame.Surface(rect1.size, pygame.SRCALPHA, 32)
        rotate.fill((0, 0, 0, 0))
        pygame.transform.rotate(rotate, 45)

    def rainbow_rect(self, objct: ObjectModel):
        x = objct.x * self.cell_size
        y = objct.y * self.cell_size
        offset_x = x * .5 % 255
        offset_y = y * .5 % 255
        special_color = (offset_x, objct.color[1], offset_y)
        special_color2 = self.lightnen_color(special_color)
        rect1 = pygame.Rect(x, y, self.cell_size * .9, self.cell_size * .9)
        rect2 = pygame.Rect(x, y, self.cell_size * .6, self.cell_size * .6)
        rect2.center = rect1.center
        pygame.draw.rect(self.screen, special_color2, rect1)
        pygame.draw.rect(self.screen, special_color, rect2)

    def rainbow_color_from_x_y(self, x, y):
        global offset

        def ribw():
            rainbow_colors = []
            for r, g, b in zip(
                chain(reversed(range(256)), [0] * 256),
                chain(range(256), reversed(range(256))),
                chain([0] * 256, range(256))):
                rainbow_colors.append((r, g, b))


            return rainbow_colors

        width, height = self.screen.get_size()

        rainbow = ribw()
        mult = len(rainbow) / (width / self.cell_size)
        rainbow_index = x * mult
        rainbow_index = (x * mult + offset) % len(rainbow)
        color = rainbow[int(rainbow_index)]


        offset += .01

        r = color[0] + offset, color[1] + offset, color[2] + offset
        c = r[0] % 255, r[1] % 255, r[2] % 255
        return color
