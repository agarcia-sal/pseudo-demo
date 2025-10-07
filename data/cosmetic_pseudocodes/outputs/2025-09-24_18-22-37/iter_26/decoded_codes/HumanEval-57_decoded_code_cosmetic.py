from typing import Sequence, TypeVar

T = TypeVar('T')


def monotonic(collection: Sequence[T]) -> bool:
    is_sorted_forward: bool = True
    is_sorted_backward: bool = True
    idx: int = 0
    n: int = len(collection)

    while idx < n - 1:
        if collection[idx] > collection[idx + 1]:
            is_sorted_forward = False
        if collection[idx] < collection[idx + 1]:
            is_sorted_backward = False
        idx += 1

    if is_sorted_forward or is_sorted_backward:
        return True
    return False