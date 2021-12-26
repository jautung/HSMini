import logging
from game.board import Board
from game.cards.card import Card
from game.cards.fatigue_card import FatigueCard
from game.deck import Deck
from game.face import Face
from game.hand import Hand
from game.mana_bin import ManaBin

class Game:
    def __init__(self, player_deck: Deck, opponent_deck: Deck) -> None:
        self._board = Board()
        self._player_deck = player_deck
        self._player_deck.shuffle()
        self._opponent_deck = opponent_deck
        self._opponent_deck.shuffle()
        self._player_hand = Hand()
        self._opponent_hand = Hand()
        self._player_face = Face()
        self._opponent_face = Face()
        self._player_mana_bin = ManaBin()
        self._opponent_mana_bin = ManaBin()

    def start_player_turn(self) -> None:
        self._player_mana_bin.increment_mana()
        drawn_object = self._player_deck.draw_top_card()
        if isinstance(drawn_object, FatigueCard):
            self._player_face.take_damage(drawn_object.get_fatigue_damage())
            logging.debug("Player takes %s fatigue damage", drawn_object.get_fatigue_damage())
        elif isinstance(drawn_object, Card):
            self._player_hand.add_card(drawn_object)
            logging.debug("Player draws card '%s'", drawn_object)
        else:
            logging.error("Drawn object of unknown type")

    def switch_players(self) -> None:
        self._board.switch_players()
        self._player_deck, self._opponent_deck = self._opponent_deck, self._player_deck
        self._player_hand, self._opponent_hand = self._opponent_hand, self._player_hand
        self._player_face, self._opponent_face = self._opponent_face, self._player_face
        self._player_mana_bin, self._opponent_mana_bin =\
            self._opponent_mana_bin, self._player_mana_bin

    def __str__(self) -> str:
        return f"\nPlayer is at {self._player_face.get_current_health()} health, "\
            f"opponent is at {self._opponent_face.get_current_health()} health.\n"\
            f"Player has {self._player_hand.get_size()} card(s) in hand, "\
            f"{self._player_deck.get_size()} card(s) in deck.\n"\
            f"Opponent has {self._opponent_hand.get_size()} card(s) in hand, "\
            f"{self._opponent_deck.get_size()} card(s) in deck.\n"\
            f"Player has {self._player_mana_bin.get_mana()} mana, "\
            f"opponent has {self._opponent_mana_bin.get_mana()} mana.\n"
