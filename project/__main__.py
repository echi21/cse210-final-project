import arcade
from game import constants
from game.soccer_bomb import SoccerBomb


def main():
    app = SoccerBomb(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    app.center_window()
    arcade.run()


# Main code entry point
if __name__ == "__main__":
    main()
