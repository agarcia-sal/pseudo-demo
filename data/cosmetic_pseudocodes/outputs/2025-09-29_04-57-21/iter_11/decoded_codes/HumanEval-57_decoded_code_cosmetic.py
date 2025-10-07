from typing import Iterable, TypeVar

T = TypeVar('T', bound='Comparable')

def monotonic(items_collection: Iterable[T]) -> bool:
    items_list = list(items_collection)
    return items_list == sorted(items_list) or items_list == sorted(items_list, reverse=True)

# Comparable protocol for type hinting with sorted elements
from typing import Protocol, runtime_checkable

@runtime_checkable
class Comparable(Protocol):
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...