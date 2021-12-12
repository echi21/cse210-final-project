import pathlib
import arcade
import game.fading_view
import game.instruction_view
import game.sound_library


class IntroductionView(game.fading_view.FadingView):
    """ Class that manages the 'introduction' view. """
    def __init__(self):
        super().__init__()

    def on_show(self):
        """ Called when switching to this view"""
        # Set the background color
        field_image = (pathlib.Path(__file__).parent / "images/intro.png")
        self.background = arcade.load_texture(field_image.__str__())
        self.window.music = arcade.play_sound(game.sound_library.SoundLibrary().get_intro(), 1, -1, True)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        """ Handle key presses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if self.fade_out is None and key == arcade.key.SPACE or key == arcade.key.ENTER:
            self.fade_out = 0

    def on_update(self, delta_time: float):

        self.update_fade(next_view=game.instruction_view.InstructionView)
        self.time_counter += delta_time * 1
        self.introduction_timed()

    def introduction_timed(self):
        if self.fade_out is None and self.time_counter > 40:
            self.fade_out = 0
