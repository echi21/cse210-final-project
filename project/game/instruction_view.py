import pathlib
import arcade
import fading_view
import menu_view


class InstructionView(fading_view.FadingView):
    """ Manage the 'game' view for our program. """
    def __init__(self):
        super().__init__()

    def on_show(self):
        """ Called when switching to this view"""
        field_image = (pathlib.Path(__file__).parent / "images/instructions.png")
        self.background = arcade.load_texture(field_image.__str__())

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.SPACE or key == arcade.key.ENTER:
            self.fade_out = 0

    def on_update(self, delta_time: float):
        self.update_fade(next_view=menu_view.MenuView)
        self.time_counter += delta_time * 1
        self.introduction_timed()

    def introduction_timed(self):
        if self.fade_out is None and self.time_counter > 15:
            self.fade_out = 0
