import arcade
from game import constants
from game.enemy_team import EnemyTeam
from game.input_service import InputService
from game.sound_library import SoundLibrary


class Configuration:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ambience = None
        self.all_sprites = None
        self.enemy_team = None
        self.player = None
        self.soccer_goal = None
        self.input_service = None
        self.sound = None
        # self.fatigue_sound = None
        self.setup()

    def setup(self):
        """Get the game ready to play
                """
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        self.sound = SoundLibrary()

        # Play your background music
        self.ambience = arcade.play_sound(self.sound.get_ambience(), True)

        # self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        # self.player = Player(self.width, self.height)
        # self.player = self.player.get_his_sprite()

        self.enemy_team = EnemyTeam(self.width, self.height)

        self.player = arcade.Sprite("game/images/player.png", constants.SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 0

        self.soccer_goal = arcade.Sprite("game/images/soccer_goal.png", constants.SCALING)
        self.soccer_goal.center_y = self.height / 2
        self.soccer_goal.right = constants.SCREEN_WIDTH

        self.all_sprites.append(self.player)  # Check this
        self.all_sprites.append(self.soccer_goal)

        # The soccer field image author is from “Vecteezy.com”.
        # This resource is used under the Free Licenser
        for enemy in self.enemy_team.get_enemies_list():
            self.all_sprites.append(enemy)

        self.input_service = InputService(self.player)

    def get_enemy_team(self):
        return self.enemy_team

    def get_sprite_list(self):
        return self.all_sprites

    def get_input_service(self):
        return self.input_service

    def get_sound(self):
        return self.sound

    # Remember ambience is a player object not a sound object. It is necessary to stop de ambience sound
    def get_ambience_object(self):
        return self.ambience
