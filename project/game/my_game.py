
import arcade
from game.configuration import Configuration


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        self.background = None
        self.score = 0
        self.conf = None
        self.setup()

    def setup(self):
        """Get the game ready to play
        """
        self.conf = Configuration(self.width, self.height)

    # These methods must be in the window class. If their name are changed, they don't work.
    def on_key_press(self, symbol, modifiers):
        """"""
        self.conf.get_input_service().on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        """"""
        self.conf.get_input_service().on_key_release(symbol, modifiers)

    def on_update(self, delta_time: float):
        """"""
        if self.conf.get_input_service().get_paused():
            return

        self.conf.get_handle_collision().preparing_update(delta_time)

        if self.conf.get_handle_collision().get_flag():
            self.setup()
            self.score += 1

    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.conf.get_background())
        self.conf.get_sprite_list().draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)
