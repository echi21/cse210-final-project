# import os
# from pathlib import Path
import pathlib

import arcade
from game import constants
from game.enemy_team import EnemyTeam
from game.handle_collision import HandleCollision
from game.input_service import InputService
from game.sound_library import SoundLibrary


class Configuration:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background = None
        self.ambience_obj = None
        self.scream_obj = None
        self.all_sprites = None
        self.enemy_team = None
        self.player = None
        self.soccer_goal = None
        self.input_service = None
        self.handle_collision = None
        self.sound = SoundLibrary()

        self.setup()

    def setup(self):
        """Get the game ready to play
        """
        # Different ways to access the path of a file.

        # First method works using 'import os':
        # path = os.path.dirname(os.path.abspath(__file__))
        # field_image = (path + "/images/field.png")

        # Second method works using 'from pathlib import Path':
        # field_image = Path('game/images/field.png')

        # Third method works using '':
        # pathlib.Path(__file__).parent / "images/soccer_field.jpg"

        # Set the background color
        field_image = (pathlib.Path(__file__).parent / "images/soccer_field.png")
        self.background = arcade.load_texture(field_image.__str__())

        # Play your background music
        self.ambience_obj = arcade.play_sound(self.sound.get_ambience(), 1, -1, True)
        # Play over a time the scream of the monsters
        self.scream_obj = arcade.play_sound(self.sound.get_scream(), 1, -1, True)

        # arcade.schedule(self.play_scream, 8.0)

        self.all_sprites = arcade.SpriteList()

        # Creating the enemies
        self.enemy_team = EnemyTeam(self.width, self.height)

        # Creating the player
        player_image = (pathlib.Path(__file__).parent / "images/player.png")
        self.player = arcade.Sprite(player_image.__str__(), constants.PLAYER_SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 0

        # Creating the soccer goal
        soccer_g_image = (pathlib.Path(__file__).parent / "images/soccer_goal.png")
        self.soccer_goal = arcade.Sprite(soccer_g_image.__str__(), constants.SOCCER_G_SCALING)
        self.soccer_goal.center_y = self.height / 2
        self.soccer_goal.right = constants.SCREEN_WIDTH - 10

        # Apending the player, soccer goal and enemies in the all_sprites list
        self.all_sprites.append(self.player)
        self.all_sprites.append(self.soccer_goal)

        # The soccer field image author is from “Vecteezy.com”.
        # This resource is used under the Free Licenser
        for enemy in self.enemy_team.get_enemies_list():
            self.all_sprites.append(enemy)

        self.input_service = InputService(self.player)

        self.handle_collision = HandleCollision(self.width, self.height, self.player, self.soccer_goal,
                                                self.enemy_team, self.all_sprites,
                                                self.get_ambience_object(), self.get_scream_object())

    def get_background(self):
        return self.background

    def get_enemy_team(self):
        return self.enemy_team

    def get_sprite_list(self):
        return self.all_sprites

    def get_sound(self):
        return self.sound

    # It is a player object not a sound object, necessary to use the stop function for a sound.
    def get_ambience_object(self):
        return self.ambience_obj

    def get_scream_object(self):
        return self.scream_obj

    def get_input_service(self):
        return self.input_service

    def get_handle_collision(self):
        return self.handle_collision

    # Function necessary if we want to use the schedule function
    # def play_scream(self, delta_time: float):
    #    arcade.play_sound(self.sound.get_scream())
