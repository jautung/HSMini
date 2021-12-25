class Minion:
    def __init__(self, attack: int, max_health: int) -> None:
        self._attack = attack
        self._max_health = max_health
        self._current_health = max_health

    def get_attack(self) -> int:
        return self._attack

    def set_attack(self, new_attack: int) -> None:
        self._attack = new_attack

    def set_max_health(self, new_max_health: int) -> None:
        self._max_health = new_max_health
        self._current_health = min(self._current_health, new_max_health)

    def take_damage(self, damage: int) -> None:
        self._current_health -= damage

    def is_dead(self) -> bool:
        return self._current_health <= 0
