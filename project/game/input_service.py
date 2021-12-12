import arcade
import constants
import sound_library


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.
    Stereotype: 
        Service Provider
    """
    def __init__(self, player):
        self.paused = False
        self.player = player
        self.fatigue_sound = sound_library.SoundLibrary().get_fatigue()

    def on_key_press(self, symbol, modifiers):
        # Quit immediately
        if symbol == arcade.key.ESCAPE:
            # arcade.close_window()
            arcade.exit()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.UP:
            self.player.change_y = constants.PLAYER_SPEED
            # arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.DOWN:
            self.player.change_y = -1 * constants.PLAYER_SPEED
            # arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.LEFT:
            self.player.change_x = -1 * constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.RIGHT:
            self.player.change_x = constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.change_y = 0

        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0

    def get_paused(self):
        return self.paused
