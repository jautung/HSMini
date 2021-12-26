import logging
from game.cards.minion_card import MinionCard
from game.player.deck import Deck
from game.game import Game
from utils.safe_list import SafeList

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test_game = Game(Deck(SafeList([MinionCard(1, 1, 1)])), Deck(SafeList([MinionCard(1, 1, 1)])))
    test_game.start_turn()
    logging.debug(test_game)
    some_legal_action = None
    for index, legal_action in enumerate(test_game.legal_actions()):
        logging.debug("legal_action %d: %s", index, legal_action)
        some_legal_action = legal_action
    if some_legal_action is not None:
        action_error = test_game.take_action(some_legal_action)
        logging.debug("taking legal action '%s'", some_legal_action)
        if action_error is not None:
            logging.debug("action_error: %s", action_error)
    logging.debug(test_game)
    test_game.switch_players()
    test_game.start_turn()
    logging.debug(test_game)
