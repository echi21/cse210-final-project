import pathlib
import arcade
import game.my_game_view


class GameOverView(arcade.View):
    """ Manage the 'game' view for our program. """
    def __init__(self):
        super().__init__()
        self.background = None
        self.ambience_object = None

    def on_show(self):
        """ Called when switching to this view"""
        field_image = (pathlib.Path(__file__).parent / "images/game_over.png")
        self.background = arcade.load_texture(field_image.__str__())

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.ENTER:
            # This line is to receive the ambience object in order to stop the sound before the game
            # starts again, to avoid the sound overlap
            arcade.stop_sound(self.ambience_object)
            my_new_game_view = game.my_game_view.MyGameView()
            self.window.show_view(my_new_game_view)

        if key == arcade.key.ESCAPE:
            arcade.exit()

    def receive_ambience_object(self, ambience_object):
        self.ambience_object = ambience_object
