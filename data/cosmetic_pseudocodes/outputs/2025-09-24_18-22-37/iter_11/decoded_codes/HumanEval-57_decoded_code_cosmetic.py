from typing import Sequence, TypeVar

_T = TypeVar('_T', bound='Comparable')

class Comparable:
    def __lt__(self: _T, other: _T) -> bool: ...
    def __eq__(self: _T, other: _T) -> bool: ...

def monotonic(sequence_of_items: Sequence[_T]) -> bool:
    ascending_sorted_version = sorted(sequence_of_items)
    descending_sorted_version = sorted(sequence_of_items, reverse=True)

    is_ascending_equal = sequence_of_items == tuple(ascending_sorted_version)
    is_descending_equal = sequence_of_items == tuple(descending_sorted_version)

    if is_ascending_equal or is_descending_equal:
        return True

    return False