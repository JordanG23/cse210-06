import constants
from game.casting.actor import Actor
from game.casting.level import Level
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(constants.FONT_SIZE)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    player = Actor()
    player.set_text("@")
    player.set_font_size(constants.FONT_SIZE)
    player.set_color(constants.WHITE)
    player.set_position(constants.START_POSITION)
    cast.add_actor("players", player)


    level = Level()
    cast.add_group(level.levelCast, 'dirt')
    cast.add_group(level.levelCast, 'grass')
    cast.add_group(level.levelCast, 'gems')
    cast.add_group(level.levelCast, 'stones')
    
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()