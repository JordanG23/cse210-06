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
    x = int(constants.MAX_X / 2)
    y = int(constants.START_LINE-15)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(constants.FONT_SIZE)
    robot.set_color(constants.WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)


    level = Level()
    cast.add_group(level.levelCast, 'dirt')
    cast.add_group(level.levelCast, 'grass')
    cast.add_group(level.levelCast, 'gems')
    cast.add_group(level.levelCast, 'stones')
    print(cast.get_first_actor('gems'))

    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()