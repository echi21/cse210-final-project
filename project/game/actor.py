import arcade
from game import constants


class Actor:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._actor = None
        self._create_actor()
        self._position_the_actor()

    # Create the Actors
    def _create_actor(self):
        self._actor = arcade.Sprite("", constants.SCALING)

    def _position_the_actor(self):
        # Position the actor
        self._actor.center_y = self._height / 2
        self._actor.right = constants.SCREEN_WIDTH

    def get_his_sprite(self):
        return self._actor
