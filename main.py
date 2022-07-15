import basic_model
from display import Display
from game import Game


display = Display()
game = Game(display)
example_model = basic_model.example_model
example_model.velocity_x = 1
game.add_object(example_model, example_model)
player = basic_model.BasicModel(
    name="player",
    sprite=basic_model.Sprite(value="player"),
    color=(255, 0, 0),
    x=150,
    y=150,
    width=32,
    height=100,
    velocity_x=1,
    velocity_y=1,
    angle=0,
    type="basic"
)
game.add_object(player)
game.loop()
