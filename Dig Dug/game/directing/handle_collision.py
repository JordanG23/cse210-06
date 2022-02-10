import constants

class Handle_collision:

    def __init__(self, cast):
        self.player =  cast.get_first_actor("players")
        self.lives = 3
        self.socore = 0 
        self._is_game_over = False


        
    def execute(self, cast):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            
        """
        if not self._is_game_over:
                self._handle_gem_collision(cast)
                self._handle_grass_collision(cast)
                self._handle_dirt_collision(cast)
                self._handle_enemy_collision(cast)
                self._handle_stone_collision(cast)
                ##self._handle_game_over(cast)


    def _handle_gem_collision(self, cast):
        for i in cast.get_actors("gems"):
            if self.player.get_position().equals(i.get_position()):
                self.socore += 100
                cast.remove_actor("gems", i)
            if self.lives <= 0:
                cast.remove_actor("gems", i)


    def _handle_grass_collision(self, cast):
         for i in cast.get_actors("grass"):
            if self.player.get_position().equals(i.get_position()):
                cast.remove_actor("grass", i)
            if self.lives <= 0:
                cast.remove_actor("grass", i)

    def _handle_dirt_collision(self, cast):
         for i in cast.get_actors("dirt"):
            if self.player.get_position().equals(i.get_position()):
                 cast.remove_actor("dirt", i)
            if self.lives <= 0:
                cast.remove_actor("dirt", i)

    def _handle_enemy_collision(self, cast):                     ## ------------------------- Needs work----------------------------------
         for i in cast.get_actors("enemy"):
            if self.player.get_position().equals(i.get_position()):
                self.lives -= 1
                self.player.set_position(constants.START_POSITION)
                cast.remove_actor("enemy", i)
            if self.lives <= 0:
                cast.remove_actor("enemy", i)

    def _handle_stone_collision(self, cast):                   ## ------------------------- Needs work----------------------------------
         for i in cast.get_actors("stone"):
            if self.player.get_position().equals(i.get_position()):
                self.lives -= 1
                self.player.set_position(constants.START_POSITION)
            if self.lives <= 0:
                cast.remove_actor("stone", i)

    ##def _handle_game_over(self, cast):
       ## if self.lives <= 0:

            


            
