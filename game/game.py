import logging
from typing import Optional
from game.actions.action_errors import ActionError, NotEnoughMana
from game.actions.actions import Action, EndTurn, MinionAttackFace, MinionAttackMinion, PlayMinionCard
from game.board.board import Board, BoardSide
from game.cards.minion_card import MinionCard
from game.player.deck import Deck
from game.player.player import Player
from utils.safe_list import SafeList

class Game:
    def __init__(self, player_deck: Deck, opponent_deck: Deck) -> None:
        self._player = Player("1", player_deck)
        self._opponent = Player("2", opponent_deck)
        self._board = Board(self._player.get_face(), self._opponent.get_face())

    def start_turn(self) -> None:
        self._player.start_turn()

    def legal_actions(self) -> SafeList[Action]:
        actions: SafeList[Action] = SafeList([EndTurn()])
        for index, card in enumerate(self._player.get_hand().get_cards()):
            if isinstance(card, MinionCard) and\
                self._player.get_mana() >= card.get_mana():
                actions.append(PlayMinionCard(index))
        return actions

    def take_action(self, action: Action) -> Optional[ActionError]:
        if isinstance(action, PlayMinionCard):
            minion_card = self._player.get_hand().get_cards()[action.minion_card_index]
            if not isinstance(minion_card, MinionCard):
                logging.error("PlayMinionCard used with not a MinionCard")
                return ActionError()
            if self._player.get_mana() < minion_card.get_mana():
                return NotEnoughMana()
            self._board.add_minion(minion_card.make_minion(), BoardSide.PLAYER)
            return None

        if isinstance(action, MinionAttackMinion):
            return None

        if isinstance(action, MinionAttackFace):
            return None

        logging.error("Unknown action taken")
        return ActionError()

    def switch_players(self) -> None:
        self._board.switch_players()
        self._player, self._opponent = self._opponent, self._player

    def __str__(self) -> str:
        return f"\n{self._player}\n{self._opponent}\n{self._board}"
