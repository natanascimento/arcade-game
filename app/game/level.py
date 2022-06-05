class LevelParameters:

    def __init__(self, spawn_time: float,
                 min_velocity: int,
                 max_velocity: int):
        self.__spawn_time = spawn_time
        self.__min_velocity = min_velocity
        self.__max_velocity = max_velocity

    @property
    def spawn_time(self):
        return self.__spawn_time

    @property
    def min_velocity(self):
        return self.__min_velocity

    @property
    def max_velocity(self):
        return self.__max_velocity


class GameDifficultyParameters(LevelParameters):

    def __init__(self, level: str):
        if level == "Easy":
            super().__init__(spawn_time=2,
                             min_velocity=-200,
                             max_velocity=-50)
        if level == "Medium":
            super().__init__(spawn_time=1,
                             min_velocity=-500,
                             max_velocity=-300)
        if level == "Hard":
            super().__init__(spawn_time=0.5,
                             min_velocity=-1000,
                             max_velocity=-50)
        if level == "Very Hard":
            super().__init__(spawn_time=0.3,
                             min_velocity=-2000,
                             max_velocity=-1500)
