import random
import re
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast
from game.casting.stone import Stone
from game.casting.gems import Gems


class Level(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):                              
        "Constructs a level."
        super().__init__()
        self.levelCast = Cast()
        self.add_grass()
        self.add_dirt()
        self.add_stones()
        self.add_gems()

        
        ## Create dirt
    def add_dirt(self): 
        numx = 0
        numy = 15
        for x in range(constants.MAX_X*(constants.MAX_Y-constants.START_LINE)):
            actor = Actor()
            actor.set_text("#")
            actor.set_color(constants.BROWN)
            actor.set_position(Point(0+numx, constants.START_LINE+numy)) 
            numx += 15
            self.levelCast.add_actor('dirt', actor)
            if numx >= constants.MAX_X:
                numy += 15
                numx = 0
            if numy > constants.MAX_Y:
                break 
            
    def add_grass(self): 
        numx = 0
        for x in range(constants.MAX_X):
           actor = Actor()
           actor.set_text("%")
           actor.set_color(constants.GREEN)
           actor.set_position(Point(0+numx, constants.START_LINE)) 
           numx += 15
           self.levelCast.add_actor('grass', actor)


    def add_stones(self): 
        for x in range(constants.STONES):
            stone = Stone()
            stone.place_stone(self.levelCast)
            self.levelCast.add_actor('stones', stone)

    def add_gems(self):   
        for x in range(constants.GEMS):
            gem = Gems()
            gem.place_gem(self.levelCast)
            self.levelCast.add_actor('gems', gem)

    
        
    
        
