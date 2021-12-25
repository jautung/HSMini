from game.cards.drawn_object import DrawnObject

class Card(DrawnObject):
    def __init__(self, mana: int) -> None:
        super().__init__()
        self._mana = mana

    def get_mana(self) -> int:
        return self._mana
