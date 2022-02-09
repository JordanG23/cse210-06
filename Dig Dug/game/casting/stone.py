
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
        

    def fall(self, levelcast):
        for i in levelcast.get_all_actors():
            if Point(self.actor._position.get_x, self.actor._position.get_y-1) != i.get_position():
                self.set_velocity(Point(0,1))
                self.move_next()
                self.set_velocity(Point(0,0))
            

    def place_stone(self, levelcast): 
        dirt = levelcast.get_actors('dirt')[random.randint(0, len(levelcast.get_actors('dirt')))]
        self.set_position(dirt.get_position())
        levelcast.remove_actor('dirt', dirt)
        self.set_color(constants.gray)
        self.set_text("O")
