from events.base_events import Event, EventProperties
from actions.algorithm_actions import self_avoiding_walk, game_of_life

self_avoiding_walk = Event(
    name="self-avoiding walk",
    type="algorithm-event",
    properties=EventProperties(
        target_objects=["self_avoiding_walker"],
        value=1,
    ),
    action=self_avoiding_walk
)

game_of_life = Event(
    name="game of life",
    type="algorithm-event",
    properties=EventProperties(
        target_objects=[],
        value=0,
    ),
    action=game_of_life
)

