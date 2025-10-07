from typing import List, TypeVar

T = TypeVar('T', bound='SupportsComparison')

def below_threshold(l: List[T], t: T) -> bool:
    return all(e < t for e in l)

from typing import Protocol
class SupportsComparison(Protocol):
    def __lt__(self, __other: object) -> bool: ...