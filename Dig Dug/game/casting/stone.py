
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Stone(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):                             
        "Constructs a level."
        super().__init__()
        self.set_velocity(Point(0,15))

    def fall(self, cast):
        for i in cast.get_all_actors():
            if self._position.add(self._velocity).equals(i.get_position()):
                self.move_next()
            

    def place_stone(self, levelcast): 
        dirt = levelcast.get_actors('dirt')[random.randint(0, len(levelcast.get_actors('dirt')))]
        self.set_position(dirt.get_position())
        levelcast.remove_actor('dirt', dirt)
        self.set_color(constants.gray)
        self.set_text("O")
