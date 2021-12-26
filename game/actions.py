from typing import SupportsIndex

class Action:
    pass

class PlayMinionCard(Action):
    def __init__(self, minion_card_index: SupportsIndex) -> None:
        super().__init__()
        self.minion_card_index = minion_card_index

class MinionAttackMinion(Action):
    def __init__(self, attacker_index: SupportsIndex, target_index: SupportsIndex) -> None:
        super().__init__()
        self.attacker_index = attacker_index
        self.target_index = target_index

class MinionAttackFace(Action):
    def __init__(self, attacker_index: SupportsIndex) -> None:
        super().__init__()
        self.attacker_index = attacker_index
