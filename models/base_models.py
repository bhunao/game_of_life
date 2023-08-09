from typing import Optional, Tuple, List

from pydantic import BaseModel
from models.colors import Colors


class Sprite(BaseModel):
    value: str


class ObjectModel(BaseModel):
    id: Optional[int] = None
    name: str
    sprite: Sprite = Sprite(value="none")
    x: int = 0
    y: int = 0
    width: int = 32
    height: int = 32
    color: Tuple[int, int, int] = (255, 255, 255)
    velocity_x: int = 0
    velocity_y: int = 0
    angle: float = 0
    type: str = "basic"
    addittional_properties: dict = {}
    draw: bool = True
    update: bool = True


EXAMPLE_MODEL = ObjectModel(
    name="example",
    sprite=Sprite(value="example"),
    color=(0, 255, 0),
)
PLAYER = ObjectModel(
    name="player",
    sprite=Sprite(value="player"),
    color=(255, 0, 0),
    x=15,
    y=15,
    width=32,
    height=32,
    angle=0,
    type="basic"
)
FOOD = ObjectModel(
    name="food",
    sprite=Sprite(value="food"),
    color=Colors.RED,
    x=9,
    y=9,
    width=32,
    height=32
)
