from enum import Enum
import logging
from game.minion import Minion
from utils.safe_list import SafeList

class BoardSide(Enum):
    PLAYER = 1
    OPPONENT = 2

class Board:
    def __init__(self) -> None:
        self._player_minions: SafeList[Minion] = []
        self._opponent_minions: SafeList[Minion] = []

    def add_minion(self, minion: Minion, board_side: BoardSide) -> None:
        self._minions_on_side(board_side).append(minion)

    def run_minion_attack(
        self,
        attacker_index: Minion,
        target_index: Minion,
        attacker_side: BoardSide) -> None:
        attacker = self._minions_on_side(attacker_side)[attacker_index] # pylint: disable=unsubscriptable-object
        target = self._minions_on_opposing_side(attacker_side)[target_index] # pylint: disable=unsubscriptable-object

        if attacker is None or target is None:
            logging.error("Either the attacker or target minion indices are out of range")
            return

        attacker.takeDamage(target.getAttack())
        target.takeDamage(attacker.getAttack())

        if attacker.isDead():
            self._minions_on_side(attacker_side).pop(attacker_index)
        if target.isDead():
            self._minions_on_opposing_side(attacker_side).pop(target_index)

    def _minions_on_side(self, board_side: BoardSide) -> SafeList[Minion]:
        match board_side:
            case BoardSide.PLAYER:
                return self._player_minions
            case BoardSide.OPPONENT:
                return self._opponent_minions
            case _:
                logging.error("Board side of unknown type")

    def _minions_on_opposing_side(self, board_side: BoardSide) -> SafeList[Minion]:
        match board_side:
            case BoardSide.PLAYER:
                return self._opponent_minions
            case BoardSide.OPPONENT:
                return self._player_minions
            case _:
                logging.error("Board side of unknown type")
