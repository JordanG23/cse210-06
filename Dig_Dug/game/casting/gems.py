
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast


class Gems(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):                             
        "Constructs a Gem."
        super().__init__()
       

    def place_gem(self, levelcast): 
        dirt = levelcast.get_actors('dirt')[random.randint(100, len(levelcast.get_actors('dirt')))]
        self.set_position(dirt.get_position())
        levelcast.remove_actor('dirt', dirt)
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        self.set_color(Color(r,g,b))
        self.set_text("*")