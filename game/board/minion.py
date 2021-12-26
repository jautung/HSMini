from game.utils.has_health_mixin import HasHealthMixin

class Minion(HasHealthMixin):
    def __init__(self, attack: int, max_health: int) -> None:
        self._attack = attack
        self.init_with_max_health(max_health)

    def get_attack(self) -> int:
        return self._attack

    def set_attack(self, new_attack: int) -> None:
        self._attack = new_attack
