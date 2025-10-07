from typing import Iterable, TypeVar, Sequence

T = TypeVar('T', bound=object)

def monotonic(sequence_of_items: Sequence[T]) -> bool:
    ascending_check: list[T] = sorted(sequence_of_items)
    descending_check: list[T] = sorted(sequence_of_items, reverse=True)
    if list(sequence_of_items) == ascending_check:
        return True
    if list(sequence_of_items) == descending_check:
        return True
    return False