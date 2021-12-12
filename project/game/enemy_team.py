
import pathlib
import math
import random
import arcade
import constants


# With arcade we can't extend more than one class from arcade.Window. If so, the program will breack.
# I discovered that after days of changing and restarting the project.


class EnemyTeam:

    def __init__(self, width, height):
        # super().__init__(path, scale)
        self._width = width
        self._height = height
        self._enemies_list = arcade.SpriteList()
        self._create_enemies()

    def _create_enemies(self):
        enemy_image = (pathlib.Path(__file__).parent / "images/enemy_player.png")
        # Create the enemy_players
        for i in range(constants.ENEMIES_QUANTITY):
            enemy = arcade.Sprite(enemy_image.__str__(), constants.ENEMIES_SCALING)
            # Position the enemy_players
            enemy.center_x = random.randint(self._width, self._width + 80)
            enemy.center_y = random.randint(10, self._height - 10)
            self._enemies_list.append(enemy)

    def get_enemies_list(self):
        return self._enemies_list

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """
        for enemy in self._enemies_list:
            enemy.center_x += enemy.change_x
            enemy.center_y += enemy.change_y

            # Random 1 in 100 chance that we'll change from our old direction and
            # then re-aim toward the player
            if random.randrange(100) == 0:
                start_x = enemy.center_x
                start_y = enemy.center_y

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
                enemy.change_x = math.cos(angle) * constants.ENEMIES_SPEED
                enemy.change_y = math.sin(angle) * constants.ENEMIES_SPEED
