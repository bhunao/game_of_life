from pydantic import BaseModel
from typing import Tuple, Optional

__all__ = ["BasicModel", "Sprite"]


class Sprite(BaseModel):
    value: str


class BasicModel(BaseModel):
    id: Optional[int] = None
    name: str
    sprite: Sprite
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


example_model = BasicModel(
    name="example",
    sprite=Sprite(value="example"),
    color=(0, 255, 0),
)
