from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(array_of_items: Sequence[T]) -> bool:
    sorted_version = sorted(array_of_items)
    reversed_sorted = sorted(array_of_items, reverse=True)
    condition_one = array_of_items == sorted_version
    condition_two = array_of_items == reversed_sorted
    final_result = False
    if condition_one:
        final_result = True
    elif condition_two:
        final_result = True
    return final_result