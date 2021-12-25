import random
from game.cards.card import Card
from game.cards.drawn_object import DrawnObject
from game.cards.fatigue_card import FatigueCard
from utils.safe_list import SafeList

class Deck:
    def __init__(self, cards: SafeList[Card]) -> None:
        self._cards = cards
        self._fatigue_counter = 0

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_top_card(self) -> DrawnObject:
        if len(self._cards) == 0:
            self._fatigue_counter += 1
            return FatigueCard(self._fatigue_counter)
        return self._cards.pop(0)

    def discard_top_card(self) -> None:
        if self._cards.count > 0:
            self._cards.pop(0)

    def shuffle_in_card(self, card: Card) -> None:
        self._cards.append(card)
        self.shuffle()
