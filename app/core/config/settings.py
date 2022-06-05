from os.path import abspath, dirname, join


class Settings:

    # CONSTANTS
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 300
    SCREEN_TITLE = "Deliveryman Life's"
    RADIUS = 150
    SCALING = 2.0

    # PATHS
    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))
    ASSETS_PATH = join(ROOT_PATH, "assets")

    # IMAGES
    IMAGES_PATH = join(ASSETS_PATH, "images")

    VEHICLES_PATH = join(IMAGES_PATH, "vehicles")
    DELIVERYMAN_IMAGE = join(VEHICLES_PATH, "entregador.png")
    CAR_IMAGE = join(VEHICLES_PATH, "ferrari.png")

    HIGHWAY_PATH = join(IMAGES_PATH, "highway")
    HIGHWAY_IMAGE = join(HIGHWAY_PATH, "highway.png")

    # SOUNDS
    SOUNDS_PATH = join(ASSETS_PATH, "sounds")

    BACKGROUND_SOUND = join(SOUNDS_PATH, "background.wav")
    JUMP_SOUND = join(SOUNDS_PATH, "jump.wav")
    PAUSED_SOUND = join(SOUNDS_PATH, "paused_sound.wav")
    BLOCK_HIT_SOUND = join(SOUNDS_PATH, "retro-block-hit.wav")

    __VERSION = "0.1.0"

    def get_version(self):
        return self.__VERSION
