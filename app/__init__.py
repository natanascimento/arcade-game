import arcade

from app.core.config import settings
from app.delivery import StartView


def main():
    window = arcade.Window(int(settings.SCREEN_WIDTH * settings.SCALING),
                           int(settings.SCREEN_HEIGHT * settings.SCALING),
                           settings.SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()
