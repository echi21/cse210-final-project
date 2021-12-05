import arcade
from game.sound_library import SoundLibrary


class HandleCollision:

    def __init__(self, width, height, player, soccer_goal, enemy_team,
                 all_sprites, ambience_object, scream_object):
        self.width = width
        self.height = height
        self.player = player
        self.soccer_goal = soccer_goal
        self.enemy_team = enemy_team
        self.all_sprites = all_sprites
        self.ambience_obj = ambience_object
        self.scream_obj = scream_object
        self.paused = None
        self.flag = False
        self.sound = SoundLibrary()

    def preparing_update(self, delta_time):

        self.enemy_team.follow_sprite(self.player)
        self.handle_player_enemy_collision()
        self.handle_player_soccer_bomb_collision()
        self.all_sprites.update()
        self.handle_player_on_screen_collision()

    # Did you hit anything? If so, end the game
    def handle_player_enemy_collision(self):
        """"""
        if self.player.collides_with_list(self.enemy_team.get_enemies_list()):
            arcade.stop_sound(self.scream_obj)
            arcade.play_sound(self.sound.get_collision())
            arcade.pause(6)
            arcade.exit()

    def handle_player_soccer_bomb_collision(self):
        """"""
        if arcade.check_for_collision(self.player, self.soccer_goal):
            arcade.stop_sound(self.ambience_obj)
            arcade.stop_sound(self.scream_obj)
            arcade.play_sound(self.sound.get_goal())
            arcade.pause(6)
            self.flag = True

    def handle_player_on_screen_collision(self):
        # Keep the player on screen
        if self.player.top > self.height:
            self.player.top = self.height

        if self.player.right > self.width:
            self.player.right = self.width

        if self.player.bottom < 0:
            self.player.bottom = 0

        if self.player.left < 0:
            self.player.left = 0

    def get_flag(self):
        return self.flag
