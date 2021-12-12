
import arcade
import game.constants
import game.introduction_view


def main():
    """ Startup """
    window = arcade.Window(game.constants.SCREEN_WIDTH, game.constants.SCREEN_HEIGHT, "SoccerBomb")
    # Declaring a variable to use in the introduction_view class to play the initial music and then
    # to use it in the menu_view class to stop the sound before the game starts.
    window.music = None
    window.center_window()
    intro_view = game.introduction_view.IntroductionView()
    window.show_view(intro_view)
    arcade.run()


if __name__ == "__main__":
    main()
