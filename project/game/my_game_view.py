import arcade
import game.configuration
import game.game_over_view


class MyGameView(arcade.View):
    def __init__(self):
        """Initialize the game
        """
        super().__init__()

        self.score = 0
        self.conf = None

    def on_show(self):
        """Get the game ready to play
        """
        self.conf = game.configuration.Configuration(self.window.width, self.window.height)

    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.conf.get_background())
        self.conf.get_sprite_list().draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, self.window.width / 2, self.window.height - 20, arcade.color.WHITE, 16)

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

        if self.conf.get_handle_collision().get_enemy_flag():
            go_view = game.game_over_view.GameOverView()
            # This line is to retrieve and sent the ambience object to the game_over_view class
            go_view.receive_ambience_object(self.retieve_ambience_obj())
            self.window.show_view(go_view)

        if self.conf.get_handle_collision().get_score_flag():
            self.on_show()
            self.score += 1

    def retieve_ambience_obj(self):
        return self.conf.get_ambience_object()
