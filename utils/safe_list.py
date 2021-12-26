from typing import List, Optional, SupportsIndex, TypeVar

T = TypeVar("T") # pylint: disable=invalid-name
class SafeList(List[T]):
    def get(self, index: SupportsIndex, default: Optional[T] = None) -> Optional[T]:
        try:
            return super().__getitem__(index)
        except IndexError:
            return default
