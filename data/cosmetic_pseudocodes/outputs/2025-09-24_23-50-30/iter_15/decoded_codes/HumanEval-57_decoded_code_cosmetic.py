from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(array_of_items: Sequence[T]) -> bool:
    flag_forward: bool = True
    flag_backward: bool = True
    index: int = 0
    length: int = len(array_of_items)
    while index < length - 1:
        if not (array_of_items[index] <= array_of_items[index + 1]):
            flag_forward = False
        if not (array_of_items[index] >= array_of_items[index + 1]):
            flag_backward = False
        index += 1
    return flag_forward or flag_backward