class ManaBin:
    STARTING_MANA: int = 0
    INITIAL_MAX_MANA: int = 10

    def __init__(self) -> None:
        self._mana = ManaBin.STARTING_MANA
        self._max_mana = ManaBin.INITIAL_MAX_MANA

    def get_mana(self) -> int:
        return self._mana

    def increment_mana(self) -> None:
        self._mana += 1
        self._mana = min(self._mana, self._max_mana)
