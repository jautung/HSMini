from game.utils.has_health_mixin import HasHealthMixin

class Face(HasHealthMixin):
    HERO_STARTING_HEALTH: int = 30

    def __init__(self) -> None:
        self.init_with_max_health(Face.HERO_STARTING_HEALTH)
