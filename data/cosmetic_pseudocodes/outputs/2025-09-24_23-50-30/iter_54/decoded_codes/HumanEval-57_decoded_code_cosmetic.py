from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: 'Comparable') -> bool:
        ...
    def __eq__(self, other: object) -> bool:
        ...

def monotonic(collection: Sequence[T]) -> bool:
    ascending_condition = list(collection) == sorted(collection)
    descending_condition = list(collection) == sorted(collection, reverse=True)
    return ascending_condition or descending_condition