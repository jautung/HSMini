class ActionError:
    def __init__(self) -> None:
        self.error_message = "Error"

class NotEnoughMana(ActionError):
    def __init__(self) -> None:
        super().__init__()
        self.error_message = "I don't have enough Mana"
