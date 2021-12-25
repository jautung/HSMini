from game.cards.drawn_object import DrawnObject

class FatigueCard(DrawnObject):
    def __init__(self, fatigue_damage: int) -> None:
        super().__init__()
        self._fatigue_damage = fatigue_damage

    def get_fatigue_damage(self) -> int:
        return self._fatigue_damage
