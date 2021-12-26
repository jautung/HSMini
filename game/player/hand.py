from game.cards.card import Card
from utils.safe_list import SafeList

class Hand:
    def __init__(self) -> None:
        self._cards: SafeList[Card] = SafeList()

    def get_cards(self) -> SafeList[Card]:
        return self._cards

    def get_size(self) -> int:
        return len(self._cards)

    def add_card(self, card: Card) -> None:
        self._cards.append(card)
