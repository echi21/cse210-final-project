import pathlib
import arcade
import game.fading_view
import game.my_game_view


class MenuView(game.fading_view.FadingView):
    """ Manage the 'game' view for our program. """
    def __init__(self):
        super().__init__()

    def on_show(self):
        """ Called when switching to this view"""
        field_image = (pathlib.Path(__file__).parent / "images/menu.png")
        self.background = arcade.load_texture(field_image.__str__())

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.ENTER:
            self.fade_out = 0
            arcade.stop_sound(self.window.music)

        if key == arcade.key.ESCAPE:
            arcade.exit()

    def on_update(self, dt):
        self.update_fade(next_view=game.my_game_view.MyGameView)
