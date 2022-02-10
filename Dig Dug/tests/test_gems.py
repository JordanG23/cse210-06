""" Testing for the Cycle class of Cycle
    Author: Kendra Anderson
    Comments: 
    CSE210
"""
import pytest
from game.casting.gems import Gems
from game.casting.cast import Cast
from game.casting.level import Level

def test_place_gem():
    """Comment"""
    gem = Gems()
    Level.levelCast = Cast()

    gem.place_gem(Level.levelCast)

    assert gem._text == "*"

pytest.main(["-v", "--tb=line", "-rN", __file__])