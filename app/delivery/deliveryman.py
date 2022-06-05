import random

import arcade

from app.core.config import settings
from app.game import GameDifficultyParameters,CarSprite, RewardSprite


class Deliveryman(arcade.View):

    def __init__(self, level: str):
        self.__parameters = GameDifficultyParameters(level=level)
        self.__scaling = settings.SCALING
        self.__screen_width = int(settings.SCREEN_WIDTH * self.__scaling)
        self.__screen_height = int(settings.SCREEN_HEIGHT * self.__scaling)
        self.__screen_title = settings.SCREEN_TITLE
        super().__init__()
        self.score = 0
        self.vehicles_list = arcade.SpriteList()
        self.rewards = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        self.background = arcade.load_texture(settings.HIGHWAY_IMAGE)
        self.game_over_overlay = arcade.load_texture(settings.GAMEOVER_IMAGE)

        self.player = arcade.Sprite(settings.DELIVERYMAN_IMAGE, self.__scaling)
        self.player.center_y = self.__screen_height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)

        arcade.schedule(self.add_vehicles, self.__parameters.spawn_time)

        self.background_music = arcade.load_sound(settings.BACKGROUND_SOUND)
        self.collision_sound = arcade.load_sound(settings.BLOCK_HIT_SOUND)
        self.move_sound = arcade.load_sound(settings.JUMP_SOUND)
        self.paused_sound = arcade.load_sound(settings.PAUSED_SOUND)

        self.current_background_music = arcade.play_sound(self.background_music)

        self.paused = False
        self.collided = False
        self.collision_timer = 0.0

    def add_vehicles(self, delta_time: float):
        vehicles = CarSprite(settings.CAR_IMAGE, self.__scaling)
        vehicles.left = random.randint(self.__screen_width, self.__screen_width + 10)
        vehicles.top = random.randint(10, self.__screen_height - 10)
        vehicles.velocity = (random.randint(self.__parameters.min_velocity,
                                            self.__parameters.max_velocity), 0)

        self.vehicles_list.append(vehicles)
        self.add_reward(vehicles.left, vehicles.top, vehicles.velocity)
        self.all_sprites.append(vehicles)

    def add_reward(self, left, top, velocity):
        reward = RewardSprite(settings.CAR_IMAGE, self.__scaling)
        reward.left = left
        reward.top = top
        reward.velocity = velocity

        self.rewards.append(reward)
        self.all_sprites.append(reward)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused
            arcade.play_sound(self.paused_sound)
            arcade.stop_sound(self.current_background_music)
            if not self.paused:
                self.current_background_music = arcade.play_sound(self.background_music)

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.change_y = 250
            arcade.play_sound(self.move_sound)

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player.change_y = -250
            arcade.play_sound(self.move_sound)

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_x = -250

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.change_x = 250

    def on_key_release(self, symbol: int, modifiers: int):
        if (
                symbol == arcade.key.W
                or symbol == arcade.key.S
                or symbol == arcade.key.UP
                or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if (
                symbol == arcade.key.A
                or symbol == arcade.key.D
                or symbol == arcade.key.LEFT
                or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):

        if self.collided:
            arcade.stop_sound(self.current_background_music)
            self.collision_timer += delta_time
            if self.collision_timer > 5.0:
                arcade.close_window()
            return

        if self.paused:
            return

        if self.player.collides_with_list(self.vehicles_list):
            self.collided = True
            self.collision_timer = 0.0
            arcade.play_sound(self.collision_sound)

        for reward in self.rewards:
            if reward.center_x < self.player.center_x:
                self.score += 1
                reward.remove_from_sprite_lists()

        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )

        if self.player.top > self.__screen_height:
            self.player.top = self.__screen_height
        if self.player.right > self.__screen_width:
            self.player.right = self.__screen_width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        self.clear()

        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.__screen_width, self.__screen_height,
                                            self.background)

        self.all_sprites.draw()

        score_text = f"Score: {self.score}"
        arcade.draw_text(
            text=score_text,
            start_x=int(self.__screen_height/2 + 50),
            start_y=5,
            font_size=14,
            color=arcade.csscolor.BLACK,
            bold=True
        )

        if self.collided:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                self.__screen_width, self.__screen_height,
                                                self.game_over_overlay)
            arcade.draw_text("Press Q to quit or wait ...", self.__screen_width / 3, self.__screen_height / 5,
                             arcade.color.BLACK, font_size=25, bold=True, anchor_x="center")
