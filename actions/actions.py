import random

import pygame

from models.base_models import ObjectModel


def key_down(game_cls, game_event, objct, config):
    if game_event.type == pygame.KEYDOWN:
        if game_event.key == pygame.K_LEFT:
            objct.velocity_x = -1
        if game_event.key == pygame.K_RIGHT:
            objct.velocity_x = 1
        if game_event.key == pygame.K_UP:
            objct.velocity_y = -1
        if game_event.key == pygame.K_DOWN:
            objct.velocity_y = 1


def respawn(object: ObjectModel, max_x, max_y):
    object.x = random.randint(0, max_x)
    object.y = random.randint(0, max_y)
