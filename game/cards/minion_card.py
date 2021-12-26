from game.cards.card import Card
from game.minion import Minion

class MinionCard(Card):
    def __init__(self, mana: int, attack: int, health: int) -> None:
        super().__init__(mana)
        self._attack = attack
        self._health = health

    def make_minion(self) -> Minion:
        return Minion(self._attack, self._health)

    def __str__(self) -> str:
        return f"{self.get_mana()} Mana {self._attack}/{self._health}"
