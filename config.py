from typing import List

from pydantic import BaseSettings

from models.base_models import ObjectModel
from events.base_events import ARROW_KEYS
from models.base_models import PLAYER
from events.event import Event


class Settings(BaseSettings):
    objects: List[ObjectModel]
    events: List[Event]
    display_width: int = 800
    display_height: int = 600
    display_fps: int = 60
    display_background_color: tuple = (0, 0, 0)


DEFAULT_SETTINGS = Settings(
    objects=[PLAYER],
    events=[ARROW_KEYS],
)
