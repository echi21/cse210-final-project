import arcade
import constants
import introduction_view


def main():
    """ Startup """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "SoccerBomb")
    # Declaring a variable to use in the introduction_view class to play the initial music and then
    # to use it in the menu_view class to stop the sound before the game starts.
    window.music = None
    window.center_window()
    intro_view = introduction_view.IntroductionView()
    window.show_view(intro_view)
    arcade.run()


if __name__ == "__main__":
    main()
