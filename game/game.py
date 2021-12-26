from game.board.board import Board
from game.player.deck import Deck
from game.player.player import Player

class Game:
    def __init__(self, player_deck: Deck, opponent_deck: Deck) -> None:
        self._player = Player("1", player_deck)
        self._opponent = Player("2", opponent_deck)
        self._board = Board(self._player.get_face(), self._opponent.get_face())

    def start_player_turn(self) -> None:
        self._player.start_turn()

    def switch_players(self) -> None:
        self._board.switch_players()
        self._player, self._opponent = self._opponent, self._player

    def __str__(self) -> str:
        return f"\n{self._player}\n{self._opponent}\n"
