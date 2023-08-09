from models.base_models import ObjectModel, Sprite
from models.colors import Colors


self_avoiding_walker = ObjectModel(
    name="self-avoiding walker",
    sprite=Sprite(value="self-avoiding walker"),
    color=Colors.DARK_CYAN,
    x=5,
    y=5
)
