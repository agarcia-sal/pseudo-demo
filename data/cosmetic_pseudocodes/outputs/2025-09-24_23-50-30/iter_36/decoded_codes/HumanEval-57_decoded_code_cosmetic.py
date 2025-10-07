from typing import Sequence, TypeVar

T = TypeVar("T")


def monotonic(array_of_items: Sequence[T]) -> bool:
    ascending_check = list(array_of_items) == sorted(array_of_items)
    descending_check = list(array_of_items) == sorted(array_of_items, reverse=True)
    return ascending_check or descending_check