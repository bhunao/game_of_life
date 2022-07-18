import numpy as np

from display import GridDisplay
from display.special_render import SpecialRender
from models.base_models import ObjectModel
from models.colors import Colors


class GameOfLife(GridDisplay):
    celular_automata = None

    def _render(self):
        self.render_celular_automata()

    def render_celular_automata(self):
        self.start_life()

        next_generation = self.celular_automata.copy()
        for x in range(0, self.width//self.cell_size):
            for y in range(0, self.height//self.cell_size):
                # count the number of neighbors
                neighbors = self.celular_automata[x - 1: x + 2, y - 1: y + 2].sum() - self.celular_automata[x, y]
                # apply the rules of the game
                if self.celular_automata[x, y] == 1:
                    if neighbors < 2 or neighbors > 3:
                        next_generation[x, y] = 0
                else:
                    if neighbors == 3:
                        next_generation[x, y] = 1

                        rainbow = Colors.rainbow_color_from_x_y(self.screen.get_size(), self.cell_size, x)
                        objct = ObjectModel(
                            name="cell",
                            x=x,
                            y=y,
                            width=self.cell_size,
                            height=self.cell_size,
                            color=rainbow
                        )
                        self.render_rect(objct)

                # SpecialRender(self.screen, self.cell_size).render_t(objct)
                self.celular_automata = next_generation

    def start_life(self):
        if self.celular_automata is None:
            print(f"{self.__class__.__name__} celular_automata is None")
            self.celular_automata = np.zeros((self.rows, self.columns))
            self.create_random_live_cells()

    def create_random_live_cells(self):
        # create random live cells
        for _ in range(120):
            x = np.random.randint(0, self.columns)
            y = np.random.randint(0, self.rows)
            self.celular_automata[x, y] = 1
