import logging
from game.board import Board
from game.cards.card import Card
from game.cards.fatigue_card import FatigueCard
from game.deck import Deck

class Game:
    def __init__(self, player_deck: Deck, opponent_deck: Deck) -> None:
        self._board = Board()
        self._player_deck = player_deck
        self._player_deck.shuffle()
        self._opponent_deck = opponent_deck
        self._opponent_deck.shuffle()

    def start_turn(self) -> None:
        drawn_object = self._player_deck.draw_top_card()
        if isinstance(drawn_object, FatigueCard):
            drawn_object.get_fatigue_damage()
            print("take fatigue damage", drawn_object.get_fatigue_damage())
        elif isinstance(drawn_object, Card):
            print("draw", drawn_object, drawn_object.get_mana())
        else:
            logging.error("Drawn object of unknown type")
