import random

import pygame

from models.base_models import ObjectModel


def brain(object: ObjectModel, food: ObjectModel, screen_size):
    x_limits = 0, screen_size[0]
    y_limits = 0, screen_size[1]

    if object.x in x_limits or object.y in y_limits:
        object.velocity_x = 0
        object.velocity_y = 0
        return
    if object.x < food.x:
        object.velocity_x = 1
    elif object.x > food.x:
        object.velocity_x = -1
    if object.y < food.y:
        object.velocity_y = 1
    elif object.y > food.y:
        object.velocity_y = -1
    if object.x == food.x and object.y == food.y:
        # eat and respawn food
        food.x, food.y = random.randint(0, screen_size[0]), random.randint(0, screen_size[1])
        pass


def key_down(game_cls, game_events, objct, config):
    for game_event in game_events:
        if game_event.type == pygame.KEYDOWN:
            if game_event.key == pygame.K_LEFT:
                objct.velocity_x = -1
                objct.velocity_y = 0
            if game_event.key == pygame.K_RIGHT:
                objct.velocity_x = 1
                objct.velocity_y = 0
            if game_event.key == pygame.K_UP:
                objct.velocity_y = -1
                objct.velocity_x = 0
            if game_event.key == pygame.K_DOWN:
                objct.velocity_y = 1
                objct.velocity_x = 0
            if game_event.type == pygame.QUIT:
                pygame.quit()


def respawn(object: ObjectModel, max_x, max_y):
    object.x = random.randint(0, max_x)
    object.y = random.randint(0, max_y)
