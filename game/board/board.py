from enum import Enum
import logging
from typing import SupportsIndex
from game.board.minion import Minion
from game.player.face import Face
from utils.safe_list import SafeList

class BoardSide(Enum):
    PLAYER = 1
    OPPONENT = 2

class Board:
    def __init__(self, player_face: Face, opponent_face: Face) -> None:
        self._player_face = player_face
        self._opponent_face = opponent_face
        self._player_minions: SafeList[Minion] = SafeList()
        self._opponent_minions: SafeList[Minion] = SafeList()

    def add_minion(self, minion: Minion, board_side: BoardSide) -> None:
        self._minions_on_side(board_side).append(minion)

    def minion_attack_minion(
        self,
        attacker_index: SupportsIndex,
        target_index: SupportsIndex,
        attacker_side: BoardSide
    ) -> None:
        attacker = self._minions_on_side(attacker_side).get(attacker_index)
        target = self._minions_on_opposing_side(attacker_side).get(target_index)
        if attacker is None or target is None:
            logging.error("Either the attacker or target minion indices are out of range")
            return

        attacker.take_damage(target.get_attack())
        target.take_damage(attacker.get_attack())
        if attacker.is_dead():
            self._minions_on_side(attacker_side).pop(attacker_index)
        if target.is_dead():
            self._minions_on_opposing_side(attacker_side).pop(target_index)

    def minion_attack_face(
        self,
        attacker_index: SupportsIndex,
        attacker_side: BoardSide
    ) -> None:
        attacker = self._minions_on_side(attacker_side).get(attacker_index)
        if attacker is None:
            logging.error("The attacker minion index is out of range")
            return

        self._face_on_opposing_side(attacker_side).take_damage(attacker.get_attack())

    def switch_players(self) -> None:
        self._player_minions, self._opponent_minions = self._opponent_minions, self._player_minions

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

    def _face_on_side(self, board_side: BoardSide) -> Face:
        match board_side:
            case BoardSide.PLAYER:
                return self._player_face
            case BoardSide.OPPONENT:
                return self._opponent_face
            case _:
                logging.error("Board side of unknown type")

    def _face_on_opposing_side(self, board_side: BoardSide) -> Face:
        match board_side:
            case BoardSide.PLAYER:
                return self._opponent_face
            case BoardSide.OPPONENT:
                return self._player_face
            case _:
                logging.error("Board side of unknown type")
