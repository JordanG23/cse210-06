""" Testing for the Cycle class of Cycle
    Author: Kendra Anderson
    Comments: 
    CSE210
"""
import pytest
import constants
from game.casting.level import Level


def test_add_dirt():

    level = Level()
    level.add_dirt()
    assert level._text == "#"
    assert level._color == constants.BROWN


def test_add_grass():

    level = Level()
    level.add_grass()
    assert level._text == "%"
    assert level._color == constants.GREEN


def test_add_stones():

    level = Level()
    level.add_stones()
    assert level._text == "0"
    assert level._color == constants.gray
 

def test_add_gems():

    level = Level()
    level.add_gems()
    assert level._text =="*"


pytest.main(["-v", "--tb=line", "-rN", __file__])