from typing import Sequence, TypeVar

T = TypeVar('T')


def max_element(arr: Sequence[T]) -> T:
    if len(arr) == 1:
        return arr[0]
    else:
        candidate = arr[0]
        submax = max_element(arr[1:])
        return submax if submax > candidate else candidate