from asyncio import futures
from pickle import FALSE
from turtle import Turtle
import constants
from game.directing.handle_collision import Handle_collision
from game.shared.point import Point


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self.hc = Handle_collision(cast)
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)


    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        self.hc.execute(cast)
        
        no_move = False
        # Get player position and see where they will move
        players_position = player.get_position()
        player_future_pos = players_position.add(player.get_velocity())

        for i in cast.get_actors("stones"):
            if  player_future_pos.equals(i.get_position()): 
                no_move = True

        # Check to see if player move is out of bounds
        if not player_future_pos.get_y() < constants.START_LINE-15 and not player_future_pos.get_y() > max_y-15:
            if not player_future_pos.get_x() < 0 and not player_future_pos.get_x() > max_x-15:
                if not no_move:
                    player.move_next()
        
        # Get players new position
        player_pos = player.get_position()
        
        # Check to see if stone will move to dirt position
        for stone in cast.get_actors("stones"):
            stone_pos = stone.get_position()
            stone_future_pos = stone_pos.add(stone.get_velocity())

            # Keep moving the rock down until it hits dirt
            stone_move = True
            for dirt in cast.get_actors("dirt"):
                dirt_pos = dirt.get_position()
                stone_pos = stone.get_position()
                stone_future_pos = stone_pos.add(stone.get_velocity())
                if stone_future_pos.equals(dirt_pos):
                    stone_move = False
                    break
            if stone_move:
                stone.move_next()

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()