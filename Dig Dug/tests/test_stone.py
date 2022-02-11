""" Testing for the Cycle class of Cycle
    Author: Kendra Anderson
    Comments: 
    CSE210
"""
import pytest
import constants
from game.casting.stone import Stone


def test_place_stone():
    stone = Stone()
    stone.place_stone()
    assert stone._text == "O"
    assert stone._color == constants.gray


pytest.main(["-v", "--tb=line", "-rN", __file__])