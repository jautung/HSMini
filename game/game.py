import logging
from typing import Optional
from game.actions import Action, MinionAttackFace, MinionAttackMinion, PlayMinionCard
from game.board.board import Board, BoardSide
from game.cards.minion_card import MinionCard
from game.player.deck import Deck
from game.player.player import Player

class Game:
    def __init__(self, player_deck: Deck, opponent_deck: Deck) -> None:
        self._player = Player("1", player_deck)
        self._opponent = Player("2", opponent_deck)
        self._board = Board(self._player.get_face(), self._opponent.get_face())

    def start_turn(self) -> None:
        self._player.start_turn()

    def take_action(self, action: Action) -> Optional[str]: # Optionally returns an error message
        if isinstance(action, PlayMinionCard):
            minion_card = self._player.get_hand().get_cards()[action.minion_card_index]
            if isinstance(minion_card, MinionCard):
                if self._player.get_mana() < minion_card.get_mana():
                    return "Not enough mana"
                self._board.add_minion(minion_card.make_minion(), BoardSide.PLAYER)
                return None
            else:
                logging.error("PlayMinionCard used with not a MinionCard")
        elif isinstance(action, MinionAttackMinion):
            return "Not yet implemented"
        elif isinstance(action, MinionAttackFace):
            return "Not yet implemented"
        return "Unknown action taken"

    def switch_players(self) -> None:
        self._board.switch_players()
        self._player, self._opponent = self._opponent, self._player

    def __str__(self) -> str:
        return f"\n{self._player}\n{self._opponent}\n{self._board}"
