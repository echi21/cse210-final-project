import arcade
from game import constants


class Player:

    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self._height = height
        self._player = None
        self._create_player()
        self._position_the_player()

    # Create the Actors
    def _create_player(self):
        self._player = arcade.Sprite("game/images/player.png", constants.SCALING)

    def _position_the_player(self):
        # Position the actor
        self._player.center_y = self._height / 2
        self._player.left = 0

    def get_his_sprite(self):
        return self._player
