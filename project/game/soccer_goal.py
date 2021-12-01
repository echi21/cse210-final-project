import arcade
from game import constants
from game.actor import Actor


class SoccerGoal(Actor):

    def __init__(self, width, height):
        super().__init__(width, height)


    # Create the Actors
    #def _create_soccer_goal(self):
        self._soccer_goal = arcade.Sprite("game/images/soccer_goal.png", constants.SCALING)

    #def _position_the_player(self):
        # Position the actor
        self._soccer_goal.center_y = self._height / 2
        self._soccer_goal.right = constants.SCREEN_WIDTH

    #def get_his_sprite(self):
        return self._soccer_goal
