import math
import arcade
import random
import constants


class Enemy(arcade.Sprite):

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            self.change_x = math.cos(angle) * constants.ENEMIES_SPEED
            self.change_y = math.sin(angle) * constants.ENEMIES_SPEED


class SoccerBomb(arcade.Window):

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        # Set up the empty sprite lists
        self.enemies_list = None
        self.all_sprites = None

        # Set up the player. All sprites in arcade have a specific size and position in the window.
        self.player = None
        self.soccer_goal = None
        self.score = 0
        self.music = None

        # Load your background music and sound effects
        self.background_music = arcade.load_sound("sound_effects/ambience_sound.wav")
        self.collision_sound = arcade.load_sound("sound_effects/scream_explosion.wav")
        self.goal_sound = arcade.load_sound("sound_effects/goal_reaction.wav")
        self.fatigue_sound = arcade.load_sound("sound_effects/walking_breath.wav")

        self.paused = None
        self.setup()

    def setup(self):
        """Get the game ready to play
        """
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Play your background music
        self.music = arcade.play_sound(self.background_music, True)

        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.player = arcade.Sprite("images/player.png", constants.SCALING)
        self.soccer_goal = arcade.Sprite("images/soccer_goal.png", constants.SCALING)

        # The soccer field image author is from “Vecteezy.com”.
        # This resource is used under the Free Licenser

        # Set up the player. All sprites in arcade have a specific size and position in the window.
        self.player.center_y = self.height / 2
        self.player.left = 0

        self.soccer_goal.center_y = self.height / 2
        self.soccer_goal.right = constants.SCREEN_WIDTH

        self.all_sprites.append(self.player)
        self.all_sprites.append(self.soccer_goal)

        # Create the enemy_players
        for i in range(constants.ENEMIES_QUANTITY):
            enemy = Enemy("images/enemy_player.png", constants.SCALING)

            # Position the enemy_players
            enemy.center_x = random.randint(self.width, self.width + 80)
            enemy.center_y = random.randint(10, self.height - 10)

            self.enemies_list.append(enemy)
            self.all_sprites.append(enemy)

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        # Quit immediately
        if symbol == arcade.key.Q:
            # Here I should create something to confirm finishing the game
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -1 * constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -1 * constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = constants.PLAYER_SPEED
            arcade.play_sound(self.fatigue_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (symbol == arcade.key.I
                or symbol == arcade.key.K
                or symbol == arcade.key.UP
                or symbol == arcade.key.DOWN):
            self.player.change_y = 0

        if (symbol == arcade.key.J
                or symbol == arcade.key.L
                or symbol == arcade.key.LEFT
                or symbol == arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing
        Arguments:
            delta_time {float} -- Time since the last update
        """

        # If paused, don't update anything
        if self.paused:
            return

        for sprite in self.enemies_list:
            sprite.follow_sprite(self.player)

        # Did you hit anything? If so, end the game
        if self.player.collides_with_list(self.enemies_list):
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


# Main code entry point
if __name__ == "__main__":
    app = SoccerBomb(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    app.center_window()
    arcade.run()
