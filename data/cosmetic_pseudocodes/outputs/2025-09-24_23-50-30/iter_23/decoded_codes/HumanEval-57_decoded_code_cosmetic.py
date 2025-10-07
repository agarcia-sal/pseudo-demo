from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')


class Comparable:
    def __lt__(self: T, other: T) -> bool:
        ...

def monotonic(collection: Sequence[T]) -> bool:
    sorted_version = sorted(collection)
    reversed_version = sorted(collection, reverse=True)
    return collection == sorted_version or collection == reversed_version