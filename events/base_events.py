from actions.actions import key_down, respawn, brain
from events.event import Event, EventProperties

RESPAW_ON_DEATH = Event(
    name="respawn_on_death",
    type="on_death",
    properties=EventProperties(
        target_objects=["food"],
        value="respawn",
    ),
    action=respawn
)
ARROW_KEYS = Event(
    name="arrow_keys",
    type="key_down",
    properties=EventProperties(
        target_objects=["player"],
        value=1
    ),
    action=key_down
)
BRAIN = Event(
    name="brain",
    type="brain",
    properties=EventProperties(
        target_objects=["player", "food"],
        value=1
    ),
    action=brain
)
