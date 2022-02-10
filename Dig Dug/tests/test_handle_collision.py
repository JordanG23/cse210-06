""" Testing for the Cycle class of Cycle
    Author: Kendra Anderson
    Comments: 
    CSE210
"""
import pytest
from game.directing.handle_collision import Handle_collision
from game.casting.cast import Cast
from game.casting.level import Level


def test_default_class():
    collision = Handle_collision()

    assert collision.lives == 3
    assert collision.score == 0
    assert collision._is_game_over == False


def test_execute():
    collision = Handle_collision()
    cast = Cast()
    collision.execute(cast)
    
    assert collision._is_game_over == False


def test_handle_gem_collision():
    collision = Handle_collision()
    cast = Cast()
    collision.handle_gem_collision(cast)

#from here down still needs work
#
#
#
    for i in cast.get_actors("gems"):
        if self.player.get_position().equals(i.get_position()):
            self.socore += 100
            self.banner_score.set_text(f"Score: {self.socore}")
            cast.remove_actor("gems", i)
        if self.lives < 0:
            cast.remove_actor("gems", i)


def _handle_grass_collision(self, cast):

    for i in cast.get_actors("grass"):
        if self.player.get_position().equals(i.get_position()):
            cast.remove_actor("grass", i)
        if self.lives < 0:
            cast.remove_actor("grass", i)


def _handle_dirt_collision(self, cast):
    for i in cast.get_actors("dirt"):
        if self.player.get_position().equals(i.get_position()):
            cast.remove_actor("dirt", i)
        if self.lives < 0:
            cast.remove_actor("dirt", i)


# ------------------------- Needs work----------------------------------
def _handle_enemy_collision(self, cast):
    for i in cast.get_actors("enemy"):
        if self.player.get_position().equals(i.get_position()):
            self.lives -= 1
            self.player.set_position(constants.START_POSITION)
            cast.remove_actor("enemy", i)
        if self.lives < 0:
            cast.remove_actor("enemy", i)


def _handle_stone_collision(self, cast):
    for i in cast.get_actors("stones"):

        if self.player.get_position().equals(i.get_position()):
            self.lives -= 1
            self.player.set_position(constants.START_POSITION)
            if self.lives == 2:
                self.banner_lives.set_text(f"Lives Q Q")
            elif self.lives == 1:
                self.banner_lives.set_text(f"Lives Q ")
            elif self.lives == 0:
                self.banner_lives.set_text(f"Lives  ")
        if self.lives < 0:
            cast.remove_actor("stones", i)


def _handle_game_over(self, cast):
    if self.lives < 0:
        banner_gameover = cast.get_actors("banners")[2]
        banner_gameover.set_text("Game Over")


pytest.main(["-v", "--tb=line", "-rN", __file__])
