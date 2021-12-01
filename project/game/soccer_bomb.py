import arcade
from game import constants
from game.enemy_team import EnemyTeam
from game.input_service import InputService
from game.player import Player


class SoccerBomb(arcade.Window):
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
        self.music = None
        self.input_service = None
        self.paused = None

        # Load your background music and sound effects
        self.background_music = arcade.load_sound("game/sound_effects/ambience_sound.wav")
        self.collision_sound = arcade.load_sound("game/sound_effects/scream_explosion.wav")
        self.goal_sound = arcade.load_sound("game/sound_effects/goal_reaction.wav")
        self.fatigue_sound = arcade.load_sound("game/sound_effects/walking_breath.wav")

        self.setup()

    def setup(self):
        """Get the game ready to play
        """
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Play your background music
        self.music = arcade.play_sound(self.background_music, True)

        # self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.player = Player(self.width, self.height)
        self.player = self.player.get_his_sprite()

        self.enemy_team = EnemyTeam(self.width, self.height)

        # self.player = arcade.Sprite("game/images/player.png", constants.SCALING)
        self.soccer_goal = arcade.Sprite("game/images/soccer_goal.png", constants.SCALING)

        # The soccer field image author is from “Vecteezy.com”.
        # This resource is used under the Free Licenser

        self.soccer_goal.center_y = self.height / 2
        self.soccer_goal.right = constants.SCREEN_WIDTH

        self.all_sprites.append(self.player)  # Check this
        self.all_sprites.append(self.soccer_goal)

        for enemy in self.enemy_team.get_enemies_list():
            self.all_sprites.append(enemy)

        self.input_service = InputService(self.player, self.fatigue_sound)

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
            arcade.play_sound(self.collision_sound)
            arcade.pause(6)
            arcade.close_window()

        if arcade.check_for_collision(self.player, self.soccer_goal):
            arcade.stop_sound(self.music)
            arcade.play_sound(self.goal_sound)
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
