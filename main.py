
from core.app import App

DEFAULT_SCREEN_WIDTH = 1280
DEFAULT_SCREEN_HEIGHT = 720


def import_configuration(filename):
    pass


if __name__ == '__main__':
    main = App(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
    main.execute()
