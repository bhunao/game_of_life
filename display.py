from typing import List
import pygame
from basic_model import BasicModel


class Display:
    def __init__(self, width=800, height=600, fps=60):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

    def _draw_rect(self, object: BasicModel):
        pygame.draw.rect(self.screen, object.color, (object.x+100, object.y+100, object.width, object.height))
        pygame.draw.rect(self.screen, (255, 255, 255), (object.x+100, object.y+100, object.width, object.height), 5)

    def _render_object(self, objcts: List[BasicModel]):
        if not objcts:
            return

        for objct in objcts:
            object_surface = pygame.Surface((objct.width, objct.height))
            object_surface.fill(objct.color)
            self.screen.blit(object_surface, (objct.x, objct.y))
            print(f"rendered object: [{objct.name}|{objct.id}][{objct.x}, {objct.y}, {objct.width}, {objct.height}]")
        return True

    def render_frame(self, objects: List[BasicModel] = None):
        self.clock.tick(self.fps)
        self.screen.fill((0, 0, 0))
        self._render_object(objects)
        self._draw_rect(objects[0])


        pygame.display.update()

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


