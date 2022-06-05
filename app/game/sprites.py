from arcade import Sprite


class CarSprite(Sprite):

    def update(self):
        super().update()

        if self.right < 0:
            self.remove_from_sprite_lists()


class RewardSprite(Sprite):

    def update(self):
        super().update()

        if self.right < 0:
            self.remove_from_sprite_lists()
