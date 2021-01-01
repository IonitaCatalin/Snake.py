from core.app import App

DEFAULT_SCREEN_WIDTH = 1280
DEFAULT_SCREEN_HEIGHT = 890
DEFAULT_PLAYER_WIDTH = 30
DEFAULT_PLAYER_HEIGHT = 30


def import_configuration(filename):
    pass


if __name__ == '__main__':
    main = App(3, DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, DEFAULT_PLAYER_WIDTH, DEFAULT_PLAYER_HEIGHT)
    main.execute()
