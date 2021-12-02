import arcade
from game.configuration import Configuration


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)
        # Set up the empty sprite lists
        self.all_sprites = None
        # Set up the player. All sprites in arcade have a specific size and position in the window.
        self.player = None
        self.soccer_goal = None
        self.enemy_team = None
        self.score = 0
        self.ambience = None
        self.input_service = None
        self.paused = None
        self.conf = None
        self.setup()

    def setup(self):
        """Get the game ready to play
        """
        self.conf = Configuration(self.width, self.height)
        self.enemy_team = self.conf.get_enemy_team()
        self.all_sprites = self.conf.get_sprite_list()
        self.player = self.all_sprites[0]
        self.soccer_goal = self.all_sprites[1]
        self.input_service = self.conf.get_input_service()

    # This method must be in the window class. If the name is changed, it doesn't work.
    # self.paused is used to store the condition when the user presses the P key.
    def on_key_press(self, symbol, modifiers):
        self.paused = self.input_service.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        self.input_service.on_key_release(symbol, modifiers)

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing
        Arguments:
            delta_time {float} -- Time since the last update
        """
        # If paused, don't update anything
        if self.paused:
            return

        self.enemy_team.follow_sprite(self.player)

        # Did you hit anything? If so, end the game
        # if self.player.collides_with_list(self.enemies_list):
        if self.player.collides_with_list(self.enemy_team.get_enemies_list()):
            arcade.play_sound(self.conf.get_sound().get_collision())
            arcade.pause(6)
            arcade.close_window()

        if arcade.check_for_collision(self.player, self.soccer_goal):
            arcade.stop_sound(self.conf.get_ambience_object())
            arcade.play_sound(self.conf.get_sound().get_goal())
            self.score += 1
            arcade.pause(6)
            self.setup()

        self.all_sprites.update()

        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height

        if self.player.right > self.width:
            self.player.right = self.width

        if self.player.bottom < 0:
            self.player.bottom = 0

        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """Draw all game objects
        """
        arcade.start_render()
        self.all_sprites.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)
