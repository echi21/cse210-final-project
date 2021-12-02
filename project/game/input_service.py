import arcade
from game import constants
from game.sound_library import SoundLibrary


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.
    Stereotype: 
        Service Provider
    """
    def __init__(self, player):
        self.paused = None
        self.player = player
        self.fatigue_sound = SoundLibrary().get_fatigue()

    def on_key_press(self, symbol, modifiers):
        # Quit immediately
        if symbol == arcade.key.Q:
            # Here I should create some window to confirm finishing the game
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused
            return self.paused  # I needed this to tell the caller about the pause action.

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -1 * constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -1 * constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (symbol == arcade.key.I
                or symbol == arcade.key.K
                or symbol == arcade.key.UP
                or symbol == arcade.key.DOWN):
            self.player.change_y = 0

        if (symbol == arcade.key.J
                or symbol == arcade.key.L
                or symbol == arcade.key.LEFT
                or symbol == arcade.key.RIGHT):
            self.player.change_x = 0
