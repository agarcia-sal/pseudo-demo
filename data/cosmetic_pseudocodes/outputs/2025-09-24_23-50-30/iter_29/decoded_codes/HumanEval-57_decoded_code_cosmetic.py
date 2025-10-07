from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(array_items: Sequence[T]) -> bool:
    return all(array_items[i] <= array_items[i+1] for i in range(len(array_items) - 1)) or \
           all(array_items[i] >= array_items[i+1] for i in range(len(array_items) - 1))


# Support for elements that can be compared by < and > operators (like numbers, strings)
class SupportsLessThan:
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...