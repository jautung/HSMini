import logging
from game.cards.minion_card import MinionCard
from game.player.deck import Deck
from game.game import Game
from utils.safe_list import SafeList

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test_game = Game(Deck(SafeList([MinionCard(1, 1, 1)])), Deck(SafeList([MinionCard(1, 1, 1)])))
    test_game.start_player_turn()
    logging.debug(test_game)
    test_game.switch_players()
    test_game.start_player_turn()
    logging.debug(test_game)
