import arcade
import game.constants
# from game.fog_lib import FogLib


class FadingView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background = None
        self.time_counter = 0
        self.intro_music = None
        # self.fog = FogLib()
        # self.fog_paths_list = self.fog.get_fog_list()
        # self.texture_list = []

        self.fade_out = None
        self.fade_in = 255

    def update_fade(self, next_view=None):

        if self.fade_out is not None:
            self.fade_out += game.constants.FADE_RATE
            if self.fade_out is not None and self.fade_out > 255 and next_view is not None:
                game_view = next_view()
                self.window.show_view(game_view)

        if self.fade_in is not None:
            self.fade_in -= game.constants.FADE_RATE
            if self.fade_in <= 0:
                self.fade_in = None

    def draw_fading(self):

        if self.fade_out is not None:
            arcade.draw_rectangle_filled(self.window.width / 2, self.window.height / 2,
                                         self.window.width, self.window.height,
                                         (0, 0, 0, self.fade_out))

        if self.fade_in is not None:
            arcade.draw_rectangle_filled(self.window.width / 2, self.window.height / 2,
                                         self.window.width, self.window.height,
                                         (0, 0, 0, self.fade_in))
