import logging
from game.cards.card import Card
from game.cards.fatigue_card import FatigueCard
from game.player.deck import Deck
from game.player.face import Face
from game.player.hand import Hand
from game.player.mana_bin import ManaBin

class Player:
    def __init__(self, gid: str, deck: Deck) -> None:
        self._gid = gid
        self._deck = deck
        self._deck.shuffle()
        self._hand = Hand()
        self._face = Face()
        self._mana_bin = ManaBin()

    def get_face(self) -> Face:
        return self._face

    def get_hand(self) -> Hand:
        return self._hand

    def get_mana(self) -> int:
        return self._mana_bin.get_mana()

    def start_turn(self) -> None:
        self._mana_bin.increment_mana()
        drawn_object = self._deck.draw_top_card()
        if isinstance(drawn_object, FatigueCard):
            self._face.take_damage(drawn_object.get_fatigue_damage())
            logging.debug(
                "Player (%s) takes %s fatigue damage",
                self._gid,
                drawn_object.get_fatigue_damage())
        elif isinstance(drawn_object, Card):
            self._hand.add_card(drawn_object)
            logging.debug("Player (%s) draws card '%s'", self._gid, drawn_object)
        else:
            logging.error("Drawn object of unknown type")

    def __str__(self) -> str:
        return f"Player {self._gid}: "\
            f"Health ({self._face.get_current_health()}), "\
            f"Hand ({self._hand.get_size()}), "\
            f"Deck ({self._deck.get_size()}), "\
            f"Mana ({self._mana_bin.get_mana()})"
