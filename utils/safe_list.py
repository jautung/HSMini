from typing import List

class SafeList(List):
    def __getitem__(self, index, default = None):
        try:
            return super().__getitem__(index)
        except IndexError:
            return default
