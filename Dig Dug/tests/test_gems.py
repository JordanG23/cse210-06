""" Testing for the Gem class of Dig Dug
    Author: Kendra Anderson
    Comments: Jordan Greenwood
    CSE210
"""
import pytest
from game.casting.gems import Gems
from game.casting.cast import Cast
from game.casting.level import Level

def test_place_gem():
    """Testing for the placement of the gems in the game."""
    gem = Gems()
    Level.levelCast = Cast()

    gem.place_gem(Level.levelCast)

    assert gem._text == "*"

pytest.main(["-v", "--tb=line", "-rN", __file__])