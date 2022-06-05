import arcade

from app.core.config import settings
from app.delivery.deliveryman import Deliveryman


class StartView(arcade.View):

    def __init__(self,
                 window: arcade.Window = None):
        super().__init__(window)
        self.difficulty = "Easy"
        self.background = None

    def on_show_view(self):
        self.background = arcade.load_texture(settings.INSTRUCTION_IMAGE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.window.width, self.window.height,
                                            self.background)

        arcade.draw_text("Instructions Screen", self.window.width / 2.5, self.window.height / 3,
                         arcade.color.WHITE, font_size=25, bold=True, anchor_x="center")
        arcade.draw_text("Press Space to advance or key Q to exit", self.window.width / 2.5, self.window.height / 3.5,
                         arcade.color.WHITE, font_size=10, bold=True, anchor_x="center")
        arcade.draw_text(f"Difficulty: {self.difficulty}", self.window.width / 2.5, self.window.height / 4,
                         arcade.color.WHITE, font_size=10, bold=True, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            self.window.close()

        if symbol == arcade.key.KEY_1:
            self.difficulty = "Easy"
        if symbol == arcade.key.KEY_2:
            self.difficulty = "Medium"
        if symbol == arcade.key.KEY_3:
            self.difficulty = "Hard"
        if symbol == arcade.key.KEY_4:
            self.difficulty = "Very Hard"

        if symbol == arcade.key.SPACE:
            game_view = Deliveryman(level=self.difficulty)
            game_view.setup()
            self.window.show_view(game_view)
