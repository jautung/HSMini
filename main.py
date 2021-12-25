from game.cards.minion_card import MinionCard
from game.deck import Deck
from game.game import Game

if __name__ == "__main__":
    test_game = Game(Deck([MinionCard(1, 1, 1)]), Deck([MinionCard(1, 1, 1)]))
    test_game.start_turn()
    test_game.start_turn()
