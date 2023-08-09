from typing import List
import pygame

from configs import logging
from models.base_models import ObjectModel
from models.colors import Colors


class Display:
    def __init__(self, width=800, height=600, fps=30):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.background_color = Colors.WHITE
        self.running = True
        self.tick = 0

    def _render(self):
        # used for rendering child classes methods
        pass

    def render_rect(self, objct: ObjectModel):
        logging.debug(f'Rendering rect: {objct.name}')
        pygame.draw.rect(self.screen, objct.color, (objct.x + 100, objct.y + 100, objct.width, objct.height))
        pygame.draw.rect(self.screen, (255, 255, 255), (objct.x + 100, objct.y + 100, objct.width, objct.height), 5)
        logging.debug(f'rect rendered: {objct.name}')

    def render_objets(self, objcts: List[ObjectModel]):
        if not objcts:
            return

        for objct in objcts:
            self.render_rect(objct)

    def _render_surface(self, objct):
        object_surface = pygame.Surface((objct.width, objct.height))
        object_surface.fill(objct.color)
        self.screen.blit(object_surface, (objct.x, objct.y))

    def render_frame(self, objects: List[ObjectModel] = None):
        print(f'Rendering frame: {self.tick}')
        self.tick += 1
        self.screen.fill(self.background_color)
        self._render()
        self.render_objets(objects)

        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.fps)
        # pygame.time.delay(10)

    def get_screen(self):
        return self.screen

    def get_clock(self):
        return self.clock

    def get_fps(self):
        return self.fps

    def get_running(self):
        return self.running

    def set_screen(self, screen):
        self.screen = screen

    def set_clock(self, clock):
        self.clock = clock

    def set_fps(self, fps):
        self.fps = fps

    def set_running(self, running):
        self.running = running

    def set_screen_size(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    def set_screen_size_fullscreen(self):
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

    def set_screen_size_windowed(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

    def set_screen_size_windowed_fullscreen(self):
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

    def set_screen_size_windowed_fullscreen_borderless(self):
        self.screen = pygame.display.set_mode(
            (self.width, self.height), pygame.FULLSCREEN | pygame.NOFRAME)


