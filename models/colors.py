from itertools import chain
from typing import Tuple


class Colors:
    offset = 0
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)
    BROWN = (165, 42, 42)
    LIGHT_GRAY = (211, 211, 211)
    DARK_GRAY = (169, 169, 169)
    DARK_BLUE = (0, 0, 128)
    DARK_GREEN = (0, 128, 0)
    DARK_RED = (128, 0, 0)
    DARK_PURPLE = (128, 0, 128)
    DARK_CYAN = (0, 128, 128)
    DARK_ORANGE = (255, 128, 0)
    DARK_BROWN = (128, 64, 64)
    LIGHT_BLUE = (0, 0, 255)
    LIGHT_GREEN = (0, 255, 0)
    LIGHT_RED = (255, 0, 0)
    LIGHT_PURPLE = (255, 0, 255)
    LIGHT_CYAN = (0, 255, 255)
    LIGHT_ORANGE = (255, 255, 0)
    LIGHT_BROWN = (255, 128, 128)
    DARKER_GRAY = (85, 85, 85)

    @classmethod
    def rainbow_color_from_x_y(cls, screen_size: Tuple[int, int], cell_size: int, x: int):
        rainbow = []
        for r, g, b in zip(
            chain(reversed(range(256)), [0] * 256),
            chain(range(256), reversed(range(256))),
            chain([0] * 256, range(256))):
            rainbow.append((r, g, b))


        width, height = screen_size

        mult = len(rainbow) / (width / cell_size)
        # rainbow_index = (x * mult + cls.offset) % len(rainbow)
        rainbow_index = x * mult
        color = rainbow[int(rainbow_index)]

        cls.offset += .01

        r = color[0] + cls.offset, color[1] + cls.offset, color[2] + cls.offset
        c = r[0] % 255, r[1] % 255, r[2] % 255
        return c

