class HasHealthMixin:
    def init_with_max_health(self, max_health: int) -> None:
        self._max_health = max_health
        self._current_health = max_health

    def set_max_health(self, new_max_health: int) -> None:
        self._max_health = new_max_health
        self._current_health = min(self._current_health, new_max_health)

    def set_and_set_to_max_health(self, new_max_health: int) -> None:
        self.set_max_health(new_max_health)
        self.heal_to_full()

    def get_current_health(self) -> int:
        return self._current_health

    def set_current_health(self, new_current_health: int) -> None:
        self._current_health = new_current_health

    def take_damage(self, damage: int) -> None:
        self._current_health -= damage

    def heal_to_full(self) -> None:
        self._current_health = self._max_health

    def heal(self, healing: int) -> None:
        self._current_health += healing
        self._current_health = min(self._current_health, self._max_health)

    def is_dead(self) -> bool:
        return self._current_health <= 0
